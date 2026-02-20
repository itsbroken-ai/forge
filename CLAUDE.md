# F.O.R.G.E.d — Context File

> **Framework for Organized, Resilient, Governed Engineering and Development of Agentic AI**

## What This Is

The public F.O.R.G.E. framework site. 58 methods across 8 tactical pillars for building, governing, and scaling AI agent systems. Modeled after MITRE ATT&CK. Every method exists because something went wrong and we built the system to prevent it from happening again.

**Live:** [forged.itsbroken.ai](https://forged.itsbroken.ai)
**Repo:** itsbroken-ai/forge (public)
**Brand:** itsbroken.ai (Amber #F59E0B, JetBrains Mono, CRT aesthetic)
**License:** Pete McKernan / Cipher Circle IP. See Terms of Use.

## The Eight Pillars

| ID | Pillar | Focus |
|----|--------|-------|
| FT01 | Foundation | Why you collaborate with AI |
| FT02 | Governance | Rules, authority, trust tiers |
| FT03 | Team Design | Agent specialization, parallel dispatch |
| FT04 | Invocation | Context recovery, session handoffs |
| FT05 | Execution | Workflow patterns, error recovery |
| FT06 | Quality | Testing, verification, standards |
| FT07 | Knowledge | Memory persistence, context management |
| FT08 | Evolution | Progress tracking, framework growth |

## Structure

```
forged/
├── data/              # Framework data (YAML)
│   ├── techniques/    # Individual technique definitions
│   └── tactics.yaml   # Pillar definitions
├── generator/         # Site generator (Python)
├── output/            # Generated HTML (deployed to Vercel)
├── theme/             # CSS, templates
├── launch/            # Launch materials
├── deploy.sh          # Deploy to Vercel
└── preview.sh         # Local preview
```

## Workflow

1. Edit technique YAML in `data/techniques/`
2. Run generator: `python3 generator/generate.py`
3. Preview: `./preview.sh`
4. Deploy: `./deploy.sh`

## Important Distinctions

- **F.O.R.G.E.d (this repo):** Public framework. Technique IDs `FG-XNNN`. Open contribution via GitHub issues.
- **SEED (separate, classified):** Internal zero-lab.ai framework. 14 tactics, 105+ techniques. Never referenced in this repo. Never shared externally.
- **FT09 (separate, classified):** Domain intelligence methods. Trade secret. Never in public repos.

## Commit Attribution

```
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

---

*"Every method exists because something broke. We built the fix."*
