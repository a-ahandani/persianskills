# Modified by persianskills

This folder is a copy of the upstream skill, changed on 2026-11-10 by
https://github.com/edyt-app/persianskills:

- Suggested Persian font changed from Vazirmatn to Sahel in references/web.md and its four copies under skills/*/references/; the matching inventory.json size and sha256 entries were updated. The downloads/ folder of prebuilt release zips was removed.
- The four skills under skills/*/SKILL.md and their copies in entrypoints/ were made English only: the Persian half of each bilingual description and lead line removed, frontmatter metadata added (author, source, upstream commit, version, changes), file paths marked as code, the duplicated reference in the kumihan-fa entry skill fixed, how to run runtime/check_source.py added, and the entry skill now names the other three skills. The SKILL.md entries in each skills/*/inventory.json and in the root inventory.json were updated, and the root inventory's stale checksums for the four skill inventories were corrected.
- Renamed from kumihan-fa to persian-typography to match the repo's naming rule: the folder, the four skills (kumihan-fa, kumihan-fa-web, kumihan-fa-documents, kumihan-fa-review became persian-typography, persian-typography-web, persian-typography-documents, persian-typography-review), their entrypoints/ copies, the plugin manifests and the inventory paths and checksums. The KUMIHAN display name, release tags, ZIP names and links are unchanged.

See CREDITS.md at the repo root for the source commit.
