# Contributing

Every skill in `skills/` follows one standard, whether we wrote it or copied
it from its author. The standard is itself a skill:
[`persian-skill-standard`](skills/persian-skill-standard/SKILL.md).

## Adding or changing a skill

1. **Prepare it with `persian-skill-standard`.** Load the skill in your agent
   and ask it to prepare or normalize the new skill. It covers the gates
   (scope, duplicates, license), the name, the folder layout, file names,
   frontmatter, body, content, credit and registration.
2. **Check it:**

   ```bash
   node scripts/check-skills.mjs
   ```

   It must report 0 problems.
3. **Evaluate it with `persian-skill-evaluation`.** Run the evaluation and
   paste its report into the pull request. A skill joins with the verdict
   Keep, or Fix once the listed fixes are made.
4. **Open a pull request** that adds the skill folder, its `catalog.json` row,
   its path in `.claude-plugin/marketplace.json`, and for a copied skill its
   CREDITS.md row.

Only skills about the Persian language are copied into the repo.
Integrations with Iranian services and general tools are added to
`catalog.json` as link-only rows.

## Listing a skill without copying it

Add a row to `catalog.json` with `here: false` and the skill's URL, author,
variety, category, license and a one-line description, then open a pull
request.
