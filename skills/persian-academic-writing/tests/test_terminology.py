from __future__ import annotations

import tempfile
import unittest
import unicodedata
from pathlib import Path

from scripts import terminology


SIGNED_KL_GLOSSARY = '''[glossary]
schema_version = 1
name = "Thesis terminology"

[[entries]]
id = "signed_kl_policy_guidance"
concept_id = "signed_kl_policy_guidance"
preferred_fa = "هدایت سیاستیِ KL علامت‌دار"
acronym = "KL"
definition_or_scope = "An optional post-selector policy transform whose positive coefficients attract behavior toward a head policy and whose negative coefficients repel behavior from it without making deployment weights negative."
first_use_form = "هدایت سیاستیِ KL علامت‌دار (signed-KL policy guidance)"
source_or_authority = "thesis/structure/terminology.toml; approved thesis usage; Virastar terminology guidance"
grammatical_behavior = "Persian technical noun phrase; use «هدایت KL علامت‌دار» only as the compact contextual form."
capitalization = "Preserve the Latin acronym KL."
category = "arbitration"
notes = ["A negative signed coefficient is not a negative deployment weight."]
english = "signed-KL policy guidance"
persian = "هدایت سیاستیِ KL علامت‌دار"
plural_english = "signed-KL policy-guidance transforms"
definition_ref = "terms.signed_kl_policy_guidance.definition"
accepted_variants = ["هدایت KL علامت‌دار", "همجوشی علامت‌دار"]
rejected_variants = ["وزن استقرار منفی"]
first_use = "هدایت سیاستیِ KL علامت‌دار (signed-KL policy guidance)"
status = "approved"
'''


class TerminologyTests(unittest.TestCase):
    def write_glossary(self, directory: str, text: str = SIGNED_KL_GLOSSARY) -> Path:
        path = Path(directory) / "terms.toml"
        path.write_text(text, encoding="utf-8")
        return path

    def test_loads_rich_custom_entry(self):
        with tempfile.TemporaryDirectory() as directory:
            entry = terminology.load_glossary(self.write_glossary(directory))[0]
        self.assertEqual(entry.id, "signed_kl_policy_guidance")
        self.assertEqual(entry.concept_id, entry.id)
        self.assertEqual(entry.preferred_fa, "هدایت سیاستیِ KL علامت‌دار")
        self.assertEqual(entry.notes, ("A negative signed coefficient is not a negative deployment weight.",))
        self.assertEqual(entry.accepted_variants, ("هدایت KL علامت‌دار", "همجوشی علامت‌دار"))
        self.assertEqual(entry.definition_ref, "terms.signed_kl_policy_guidance.definition")

    def test_hyphen_and_case_normalization(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_glossary(directory)
            response = terminology.lookup_english_to_persian(
                "SIGNED KL POLICY GUIDANCE",
                path,
                include_builtin=False,
            )
        self.assertEqual(response.source, "custom")
        self.assertEqual(response.matches[0].id, "signed_kl_policy_guidance")

    def test_custom_match_overrides_builtin_and_missing_custom_falls_back(self):
        custom = '''[glossary]
schema_version = 1

[[entries]]
id = "custom_accuracy"
english = "Accuracy"
persian = "دقت سفارشی"
preferred_fa = "دقت سفارشی"
status = "approved"
'''
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_glossary(directory, custom)
            overridden = terminology.lookup_english_to_persian("accuracy", path)
            fallback = terminology.lookup_english_to_persian("precision", path)
        self.assertEqual(overridden.source, "custom")
        self.assertEqual(overridden.matches[0].persian, "دقت سفارشی")
        self.assertEqual(fallback.source, "builtin")
        self.assertEqual(fallback.matches[0].english, "Precision")

    def test_builtin_preserves_duplicates_and_untranslated_source_row(self):
        unary = terminology.lookup_english_to_persian("Unary")
        prepend = terminology.lookup_english_to_persian("Prepend")
        acronym = terminology.lookup_english_to_persian("FoV")
        self.assertEqual(len(unary.matches), 2)
        self.assertEqual(prepend.matches[0].translations, ())
        self.assertIn("no Persian equivalent", prepend.matches[0].notes[0])
        self.assertEqual(acronym.matches[0].english, "Field-of-View (FoV)")

    def test_builtin_schema_and_unicode_integrity(self):
        entries = terminology.load_glossary(terminology.BUILTIN_GLOSSARY)
        self.assertEqual(len(entries), 1814)
        self.assertEqual(len({entry.id for entry in entries}), 1814)
        controls = [
            character
            for entry in entries
            for character in entry.persian
            if unicodedata.category(character) == "Cf"
        ]
        self.assertEqual(controls, [])

    def test_no_exact_match_returns_suggestions_only(self):
        response = terminology.lookup_english_to_persian("Accurcy")
        self.assertFalse(response.matches)
        self.assertIn("Accuracy", response.suggestions)

    def test_duplicate_ids_are_rejected(self):
        text = '''[glossary]
schema_version = 1
[[entries]]
id = "same"
english = "One"
persian = "یک"
status = "approved"
[[entries]]
id = "same"
english = "Two"
persian = "دو"
status = "approved"
'''
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_glossary(directory, text)
            with self.assertRaisesRegex(ValueError, "duplicate id"):
                terminology.load_glossary(path)

    def test_legacy_csv_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "terms.csv"
            path.write_text("id,english,persian\none,One,یک\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                terminology.load_glossary(path)


if __name__ == "__main__":
    unittest.main()
