# Contributing to F.O.R.G.E

F.O.R.G.E is an open framework maintained by [Pete McKernan](https://itsbroken.ai) and the Cipher Circle. We welcome community contributions that make the framework more complete and useful.

## What You Can Contribute

### Sub-Methods (Most Common)

Many techniques are missing sub-methods. These are the specific, actionable breakdowns of how to implement a technique. If you've built with AI agents and have a method that maps to an existing technique, this is the highest-value contribution.

**Example:** FG-0501 (Sprint Planning Integration) has sub-methods for AI Capacity Estimation, Task Decomposition Protocol, etc. If you have a specific approach to sprint planning with AI that isn't covered, propose it as a sub-method.

### New Techniques

If you have a method that doesn't fit any existing technique, propose a new technique under the appropriate tactic. New techniques need the full structure: description, implementation guidance, success indicators, and failure modes.

### Edits and Refinements

Improvements to existing descriptions, implementation guidance, indicators, or failure modes. If something is unclear, incomplete, or wrong, fix it.

## How to Contribute

### 1. Open an Issue First

Before writing code, open an Issue using the appropriate template:

- **Sub-Method Proposal** for new sub-methods on existing techniques
- **Technique Proposal** for entirely new techniques

Describe what you want to add and why. We'll discuss scope, placement, and naming before you write the PR.

### 2. Fork and Edit

All framework content lives in `data/generate_framework.py`. This is the single source of truth. The JSON and HTML are generated from it.

```bash
# Fork the repo, then:
git clone https://github.com/YOUR_USERNAME/forge.git
cd forge

# Make your edits to data/generate_framework.py

# Validate and build
python3 data/validate_framework.py
python3 data/generate_framework.py
python3 generator/build.py
```

### 3. Submit a PR

- Reference the Issue number in your PR description
- Include only changes to `data/generate_framework.py`
- Do NOT include generated `output/` files (CI rebuilds these)
- Do NOT include changes to `data/framework.json` (CI regenerates this)

## Content Standards

### Descriptions

Write in plain English. No jargon without explanation. Describe the "what" and "why" clearly enough that someone who hasn't done this before understands the concept.

### Implementation Guidance

Practical, actionable steps. Not theory. "Do X, then Y, then Z" beats "consider the implications of X."

### Success Indicators

Observable outcomes that tell you the technique is working. Prefer specific and measurable over vague.

### Failure Modes

Real ways this goes wrong. Not hypothetical edge cases. If you've seen it fail, describe how it failed and why.

### Sub-Methods

Each sub-method needs:
- **name**: Short, descriptive (3-6 words)
- **description**: 2-4 sentences. What is it, why does it matter, how do you do it.

### Voice

Direct and practical. This is a field manual, not an academic paper. Write like you're explaining it to a peer who's about to go do it.

## ID Numbering

You do NOT need to assign IDs. The maintainers will assign the correct ID when merging. If you want to suggest placement:

- **Techniques:** `FG-XXYY` where `XX` = tactic number, `YY` = sequence (e.g., FG-0108 would be the 8th technique in FT01)
- **Sub-Methods:** `FG-XXYY.ZZZ` where `ZZZ` = sequence under the parent (e.g., FG-0101.004)

## Validation

Run the validator before submitting:

```bash
python3 data/validate_framework.py
```

This checks:
- All required fields are present on every technique and sub-method
- ID formats are correct
- No duplicate IDs
- All `related_techniques` references point to real techniques
- All `tactic_id` references point to real tactics
- Sub-method IDs match their parent technique

## Intellectual Property

F.O.R.G.E is proprietary (see LICENSE). By submitting a contribution, you agree that:

1. Your contribution becomes part of F.O.R.G.E under the existing license
2. You have the right to submit the contribution (it's your original work)
3. You grant Pete McKernan / Cipher Circle full rights to the contributed content

Contributors are credited in the technique's `added_version` field and in the git history. We do not remove attribution.

## Code of Conduct

Be constructive. Disagree on methods, not on people. If you think a technique is wrong, explain why with evidence from your experience. "I tried X and it failed because Y" is worth more than "X is bad."

## Questions

Open a Discussion on the repo or email [Human_P@itsbroken.ai](mailto:Human_P@itsbroken.ai).
