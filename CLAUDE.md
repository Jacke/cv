# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal CV management and automation tool that applies structured CV data to Google Docs templates. Python 3.14+, no external dependencies (stdlib only).

## Commands

```bash
# Apply CV to Google Doc
python scripts/cv_structured_apply_refactored.py --data templates/cv.hard_skills.en.json --doc "Resume"

# Apply with Russian labels
python scripts/cv_structured_apply_refactored.py --data templates/cv.default.ru.json --lang ru --doc "Resume"

# Dry run (preview without changes)
python scripts/cv_structured_apply_refactored.py --data cv.json --doc "Resume" --dry-run

# Reset document to placeholders
python scripts/cv_structured_apply_refactored.py --reset --doc "Resume"

# Run unit tests
python scripts/cv_apply/test_formatters.py
```

## CV Profiles

Available CV profiles in `templates/`:

| Profile | EN | RU |
|---------|----|----|
| Default (balanced) | `cv.replacements.stanislav_sobolev.json` | `cv.default.ru.json` |
| Hard Skills (Principal/Staff) | `cv.hard_skills.en.json` | `cv.hard_skills.ru.json` |
| Soft Skills (EM/VP) | `cv.soft_skills.en.json` | `cv.soft_skills.ru.json` |

Use `--lang en` or `--lang ru` to set label language (Email/Почта, Tech/Технологии, etc.)

## Architecture

The main entry point is `scripts/cv_structured_apply_refactored.py` which orchestrates the `scripts/cv_apply/` package:

```
CV JSON Data → formatters.py (transform sections)
            → document.py (find Google Doc by name)
            → gdocs_cli.py (apply replacements via API)
            → styling.py (add bullets, links, headers)
            → state.py (persist for reset capability)
```

**Module responsibilities:**
- `constants.py` - Regexes, OAuth scopes, system constants
- `utils.py` - JSON I/O, logging, text normalization
- `formatters.py` - Transform CV sections (summary, skills, experience, education, publications)
- `translations.py` - Label translations for EN/RU support
- `document.py` - Parse `docs/resources/GOOGLE_DOCS_LINKS.md` for doc URLs, extract IDs
- `styling.py` - Apply bullet formatting, hyperlinks, H2 headers
- `state.py` - Track applied changes in `.cv_apply_state.json` for reset
- `cli.py` - CLI utilities, Google authentication
- `reset.py` - Invert replacements to restore placeholders

## Key Files

- `docs/resources/GOOGLE_DOCS_LINKS.md` - Document registry mapping names to URLs
- `templates/cv.replacements.*.json` - CV data files
- `.cv_apply_state.json` - State tracking for reset operations
- `.secrets/` - OAuth credentials (gitignored)
- `scripts/gdocs_cli.py` - Low-level Google Docs API wrapper (1,654 lines)

## CV Data Format

```json
{
  "summary": "Text or {paragraph, about}",
  "skills": [{"title": "Category", "bullets": ["skill1"]}],
  "experiences": [{
    "company": "Name", "dates": "...", "duration": "...",
    "role": "Title", "bullets": ["achievement"], "technologies": "..."
  }],
  "education": [...],
  "publications": [...]
}
```

Template placeholders: `{{fullname}}`, `{{email}}`, `{{SUMMARY}}`, `{{skills}}`, `{{exps}}`, `{{entrepreneurship}}`, `{{education}}`, `{{publications}}`

## Notes

- Uses marker-based styling (`<<SKILL_BULLET>>`, `<<EXP_BULLET>>`) for post-processing
- Auto-reauth on token expiry via gdocs_cli.py OAuth flow
- Legacy script `cv_structured_apply.py` exists but use the refactored version
