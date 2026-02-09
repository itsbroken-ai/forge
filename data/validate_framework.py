#!/usr/bin/env python3
"""
Validate framework.json for structural integrity.
Catches broken references, missing fields, duplicate IDs, and format violations
before they reach the build pipeline.
"""

import json
import re
import sys
from pathlib import Path

DATA_DIR = Path(__file__).parent
FRAMEWORK_FILE = DATA_DIR / "framework.json"

TACTIC_ID_PATTERN = re.compile(r'^FT\d{2}$')
TECHNIQUE_ID_PATTERN = re.compile(r'^FG-\d{4}$')
SUB_METHOD_ID_PATTERN = re.compile(r'^FG-\d{4}\.\d{3}$')

REQUIRED_TECHNIQUE_FIELDS = [
    "id", "name", "tactic_id", "description", "implementation",
    "success_indicators", "failure_modes", "added_version"
]

REQUIRED_SUB_METHOD_FIELDS = ["id", "name", "description"]

errors = []
warnings = []


def error(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def validate_framework_meta(fw):
    for field in ["name", "full_name", "version", "last_updated", "description"]:
        if field not in fw:
            error(f"framework: missing required field '{field}'")


def validate_tactics(tactics):
    seen_ids = set()
    for i, tactic in enumerate(tactics):
        for field in ["id", "name", "description"]:
            if field not in tactic:
                error(f"tactic[{i}]: missing required field '{field}'")
                continue

        tid = tactic.get("id", f"<missing at index {i}>")

        if not TACTIC_ID_PATTERN.match(tid):
            error(f"tactic '{tid}': ID does not match pattern FT## (e.g., FT01)")

        if tid in seen_ids:
            error(f"tactic '{tid}': duplicate ID")
        seen_ids.add(tid)

        if not tactic.get("name", "").strip():
            error(f"tactic '{tid}': name is empty")
        if not tactic.get("description", "").strip():
            error(f"tactic '{tid}': description is empty")

    return seen_ids


def validate_techniques(techniques, valid_tactic_ids):
    seen_tech_ids = set()
    seen_sub_ids = set()

    for i, tech in enumerate(techniques):
        tid = tech.get("id", f"<missing at index {i}>")

        # Required fields
        for field in REQUIRED_TECHNIQUE_FIELDS:
            if field not in tech:
                error(f"technique '{tid}': missing required field '{field}'")

        # ID format
        if not TECHNIQUE_ID_PATTERN.match(tid):
            error(f"technique '{tid}': ID does not match pattern FG-#### (e.g., FG-0101)")

        # Duplicate check
        if tid in seen_tech_ids:
            error(f"technique '{tid}': duplicate ID")
        seen_tech_ids.add(tid)

        # Tactic reference
        tactic_id = tech.get("tactic_id", "")
        if tactic_id not in valid_tactic_ids:
            error(f"technique '{tid}': tactic_id '{tactic_id}' does not exist")

        # ID should start with tactic number
        if tactic_id and tid.startswith("FG-"):
            expected_prefix = f"FG-{tactic_id[2:]}"
            if not tid.startswith(expected_prefix):
                warn(f"technique '{tid}': ID prefix doesn't match tactic '{tactic_id}' (expected {expected_prefix}XX)")

        # Content checks
        if not tech.get("name", "").strip():
            error(f"technique '{tid}': name is empty")
        if not tech.get("description", "").strip():
            error(f"technique '{tid}': description is empty")
        if not tech.get("implementation", "").strip():
            error(f"technique '{tid}': implementation is empty")

        indicators = tech.get("success_indicators", [])
        if not isinstance(indicators, list) or len(indicators) == 0:
            error(f"technique '{tid}': success_indicators must be a non-empty list")

        failures = tech.get("failure_modes", [])
        if not isinstance(failures, list) or len(failures) == 0:
            error(f"technique '{tid}': failure_modes must be a non-empty list")

        # Related techniques (optional but if present, must be valid)
        for rel_id in tech.get("related_techniques", []):
            if not TECHNIQUE_ID_PATTERN.match(rel_id):
                error(f"technique '{tid}': related_technique '{rel_id}' has invalid format")

        # Sub-methods
        for j, sub in enumerate(tech.get("sub_methods", [])):
            sub_id = sub.get("id", f"<missing at {tid}[{j}]>")

            for field in REQUIRED_SUB_METHOD_FIELDS:
                if field not in sub:
                    error(f"sub-method '{sub_id}': missing required field '{field}'")

            if not SUB_METHOD_ID_PATTERN.match(sub_id):
                error(f"sub-method '{sub_id}': ID does not match pattern FG-####.### (e.g., FG-0101.001)")

            # Sub-method ID must match parent
            if sub_id.split('.')[0] != tid:
                error(f"sub-method '{sub_id}': parent prefix doesn't match technique '{tid}'")

            if sub_id in seen_sub_ids:
                error(f"sub-method '{sub_id}': duplicate ID")
            seen_sub_ids.add(sub_id)

            if not sub.get("name", "").strip():
                error(f"sub-method '{sub_id}': name is empty")
            if not sub.get("description", "").strip():
                error(f"sub-method '{sub_id}': description is empty")

        # War story (optional, but if present must have content)
        war_story = tech.get("war_story", {})
        if war_story and not war_story.get("content", "").strip():
            warn(f"technique '{tid}': war_story exists but content is empty")

    return seen_tech_ids


def validate_cross_references(techniques, valid_tech_ids):
    for tech in techniques:
        tid = tech.get("id", "")
        for rel_id in tech.get("related_techniques", []):
            if rel_id not in valid_tech_ids:
                error(f"technique '{tid}': related_technique '{rel_id}' does not exist")


def main():
    print("F.O.R.G.E Framework Validator")
    print("=" * 50)

    if not FRAMEWORK_FILE.exists():
        print(f"\nERROR: {FRAMEWORK_FILE} not found.")
        print("Run 'python3 data/generate_framework.py' first.")
        sys.exit(1)

    with open(FRAMEWORK_FILE) as f:
        data = json.load(f)

    print(f"\nValidating framework v{data['framework'].get('version', '?')}...")
    print(f"  Tactics: {len(data.get('tactics', []))}")
    print(f"  Techniques: {len(data.get('techniques', []))}")

    # Run validations
    validate_framework_meta(data["framework"])
    valid_tactic_ids = validate_tactics(data["tactics"])
    valid_tech_ids = validate_techniques(data["techniques"], valid_tactic_ids)
    validate_cross_references(data["techniques"], valid_tech_ids)

    # Count sub-methods
    total_subs = sum(len(t.get("sub_methods", [])) for t in data["techniques"])
    print(f"  Sub-methods: {total_subs}")

    # Report
    print()
    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  ! {w}")
        print()

    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  x {e}")
        print(f"\nValidation FAILED with {len(errors)} error(s).")
        sys.exit(1)
    else:
        print("Validation PASSED.")
        sys.exit(0)


if __name__ == "__main__":
    main()
