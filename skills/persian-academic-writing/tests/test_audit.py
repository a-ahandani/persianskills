from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "audit.py"
SPEC = importlib.util.spec_from_file_location("audit", SCRIPT_PATH)
assert SPEC and SPEC.loader
apa = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = apa
SPEC.loader.exec_module(apa)


class AuditTests(unittest.TestCase):
    def make_args(self, *, targets=(), root=None, profile=None, terms=None, fix_safe=False, write=False):
        return argparse.Namespace(
            targets=[str(item) for item in targets],
            root=str(root) if root else None,
            profile=str(profile) if profile else None,
            terms=str(terms) if terms else None,
            format="json",
            output=None,
            fix_safe=fix_safe,
            write=write,
        )

    def test_safe_normalization_is_narrow_and_protects_keys_and_quotes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.tex"
            path.write_text(
                "اين يك متن فارسي با كاف و ــ کشیده است.\n"
                "\\cite{keyك}\n"
                "«نقل قول عربي و كاف»\n",
                encoding="utf-8",
            )
            text = path.read_text(encoding="utf-8")
            source = apa.SourceText.build(
                path,
                text,
                set(apa.DEFAULT_PROTECTED_COMMANDS),
                set(apa.DEFAULT_PROTECTED_ENVIRONMENTS),
            )
            normalized = apa.safe_normalize(source)
            self.assertIn("این یک متن فارسی با کاف و  کشیده است.", normalized)
            self.assertIn("\\cite{keyك}", normalized)
            self.assertIn("«نقل قول عربي و كاف»", normalized)

    def test_markdown_code_is_protected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.md"
            text = "متن كاف\n\n```python\nvalue = 'ك'\n```\n`ك`\n"
            path.write_text(text, encoding="utf-8")
            source = apa.SourceText.build(
                path,
                text,
                set(apa.DEFAULT_PROTECTED_COMMANDS),
                set(apa.DEFAULT_PROTECTED_ENVIRONMENTS),
            )
            normalized = apa.safe_normalize(source)
            self.assertTrue(normalized.startswith("متن کاف"))
            self.assertIn("value = 'ك'", normalized)
            self.assertIn("`ك`", normalized)

    def test_workspace_integrity_findings(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "chapters").mkdir()
            main = root / "main.tex"
            main.write_text(
                "\\documentclass{article}\n"
                "\\begin{document}\n"
                "\\label{dup}\n"
                "\\input{chapters/a}\n"
                "\\input{chapters/missing}\n"
                "\\bibliography{refs}\n"
                "\\end{document}\n",
                encoding="utf-8",
            )
            (root / "chapters" / "a.tex").write_text(
                "\\section{آزمون}\\label{dup}\n"
                "به بخش \\ref{sec:missing} بنگرید \\cite{missing}.\n",
                encoding="utf-8",
            )
            (root / "refs.bib").write_text(
                "@article{same, title={A}}\n"
                "@book{same, title={B}}\n",
                encoding="utf-8",
            )

            result = apa.run_audit(self.make_args(root=main))
            rules = {finding.rule for finding in result.findings}
            self.assertIn("missing-input", rules)
            self.assertIn("duplicate-label", rules)
            self.assertIn("missing-label", rules)
            self.assertIn("duplicate-bib-key", rules)
            self.assertIn("missing-bib-key", rules)

    def test_terminology_register_rejected_variant(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manuscript = root / "chapter.txt"
            manuscript.write_text("در این پژوهش از یادگیری تقویت‌شده استفاده شد.", encoding="utf-8")
            terms = root / "terms.toml"
            terms.write_text(
                """[glossary]
schema_version = 1
name = "Test terms"

[[entries]]
id = "RL"
concept_id = "RL"
english = "reinforcement learning"
persian = "یادگیری تقویتی"
preferred_fa = "یادگیری تقویتی"
acronym = "RL"
rejected_variants = ["یادگیری تقویت‌شده"]
status = "approved"
""",
                encoding="utf-8",
            )
            result = apa.run_audit(self.make_args(targets=[manuscript], terms=terms))
            term_findings = [finding for finding in result.findings if finding.prefix == "TERM"]
            self.assertTrue(term_findings)
            self.assertEqual(term_findings[0].severity, "MAJOR")
            self.assertIn("یادگیری تقویتی", term_findings[0].proposed_repair)

    def test_profile_enables_digit_and_quote_policy_checks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manuscript = root / "chapter.txt"
            manuscript.write_text('نتیجه "قابل قبول" بود و مقدار 12 گزارش شد.', encoding="utf-8")
            profile = root / "profile.toml"
            profile.write_text(
                "[orthography]\nquotation_marks = \"guillemets\"\ndigit_policy = \"persian-prose\"\n",
                encoding="utf-8",
            )
            result = apa.run_audit(self.make_args(targets=[manuscript], profile=profile))
            rules = {finding.rule for finding in result.findings}
            self.assertIn("straight-quotes", rules)
            self.assertIn("digit-policy-persian-prose", rules)

    def test_json_output_is_utf8_and_has_stable_ids(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_text("اين متن كاف دارد.", encoding="utf-8")
            result1 = apa.run_audit(self.make_args(targets=[path]))
            result2 = apa.run_audit(self.make_args(targets=[path]))
            ids1 = [finding.id for finding in result1.findings]
            ids2 = [finding.id for finding in result2.findings]
            self.assertEqual(ids1, ids2)
            payload = json.loads(apa.render_json(result1))
            self.assertGreater(payload["summary"]["total"], 0)
            self.assertIn("ك", apa.render_json(result1))


if __name__ == "__main__":
    unittest.main()
