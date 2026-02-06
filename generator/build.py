#!/usr/bin/env python3
"""
FORGED Static Site Generator
Reads framework.json and generates an ATT&CK-style interactive matrix website.
"""

import json
import os
import shutil
from pathlib import Path
from datetime import datetime

# Paths
ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
TEMPLATE_DIR = ROOT / "generator" / "templates"
THEME_DIR = ROOT / "theme"
OUTPUT_DIR = ROOT / "output"

# Tactic colors (itsbroken.ai standard accent palette — amber spectrum)
TACTIC_COLORS = {
    "FT01": {"bg": "#2a1f0a", "border": "#D4A84B", "text": "#D4A84B", "label": "Foundation"},
    "FT02": {"bg": "#2a150a", "border": "#C65D07", "text": "#C65D07", "label": "Governance"},
    "FT03": {"bg": "#2a1a0a", "border": "#e8963a", "text": "#e8963a", "label": "Team Design"},
    "FT04": {"bg": "#2a100a", "border": "#ff6b35", "text": "#ff6b35", "label": "Invocation"},
    "FT05": {"bg": "#2a1d0d", "border": "#dbb95c", "text": "#dbb95c", "label": "Execution"},
    "FT06": {"bg": "#2a1808", "border": "#d48a3b", "text": "#d48a3b", "label": "Quality"},
    "FT07": {"bg": "#2a1c0c", "border": "#c9a044", "text": "#c9a044", "label": "Knowledge"},
    "FT08": {"bg": "#2a120a", "border": "#e07828", "text": "#e07828", "label": "Evolution"},
}


def load_framework():
    """Load framework data from JSON."""
    with open(DATA_DIR / "framework.json", "r") as f:
        return json.load(f)


def ensure_output_dirs():
    """Create output directory structure."""
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    (OUTPUT_DIR / "techniques").mkdir()
    (OUTPUT_DIR / "tactics").mkdir()
    (OUTPUT_DIR / "css").mkdir()
    (OUTPUT_DIR / "js").mkdir()
    (OUTPUT_DIR / "img").mkdir()
    (OUTPUT_DIR / "fonts").mkdir()


def copy_theme_assets():
    """Copy CSS, JS, and images to output."""
    css_src = THEME_DIR / "css"
    js_src = THEME_DIR / "js"
    img_src = THEME_DIR / "img"

    if css_src.exists():
        for f in css_src.iterdir():
            shutil.copy2(f, OUTPUT_DIR / "css" / f.name)

    if js_src.exists():
        for f in js_src.iterdir():
            shutil.copy2(f, OUTPUT_DIR / "js" / f.name)

    if img_src.exists():
        for f in img_src.iterdir():
            shutil.copy2(f, OUTPUT_DIR / "img" / f.name)

    fonts_src = THEME_DIR / "fonts"
    if fonts_src.exists():
        for f in fonts_src.iterdir():
            shutil.copy2(f, OUTPUT_DIR / "fonts" / f.name)

    # Copy robots.txt and sitemap.xml to root
    for root_file in ["robots.txt", "sitemap.xml"]:
        src = THEME_DIR / root_file
        if src.exists():
            shutil.copy2(src, OUTPUT_DIR / root_file)


def read_template(name):
    """Read an HTML template file."""
    with open(TEMPLATE_DIR / name, "r") as f:
        return f.read()


def render(template_str, context):
    """Simple template rendering with {{variable}} and {%for%} support."""
    result = template_str

    # Replace simple variables
    for key, value in context.items():
        if isinstance(value, str):
            result = result.replace("{{" + key + "}}", value)
        elif isinstance(value, (int, float)):
            result = result.replace("{{" + key + "}}", str(value))

    return result


def slugify(text):
    """Convert text to URL-safe slug."""
    return text.lower().replace(" ", "-").replace("/", "-").replace("&", "and")


def build_technique_card(tech, tactic_color):
    """Build HTML for a single technique card in the matrix."""
    return f'''<a href="techniques/{tech['id'].lower()}.html" class="technique-cell" style="border-left: 3px solid {tactic_color['border']}">
        <span class="technique-id">{tech['id']}</span>
        <span class="technique-name">{tech['name']}</span>
    </a>'''


def build_matrix_page(data):
    """Generate the main matrix page."""
    tactics = data["tactics"]
    techniques = data["techniques"]

    # Group techniques by tactic
    by_tactic = {}
    for t in tactics:
        by_tactic[t["id"]] = {
            "tactic": t,
            "techniques": [tech for tech in techniques if tech["tactic_id"] == t["id"]]
        }

    # Build tactic columns
    columns_html = ""
    for tactic in tactics:
        tid = tactic["id"]
        color = TACTIC_COLORS[tid]
        techs = by_tactic[tid]["techniques"]

        tech_cards = "\n".join(build_technique_card(t, color) for t in techs)

        columns_html += f'''
        <div class="tactic-column">
            <a href="tactics/{tid.lower()}.html" class="tactic-header" style="background: {color['bg']}; border: 1px solid {color['border']}; color: {color['text']}">
                <span class="tactic-id">{tid}</span>
                <span class="tactic-name">{tactic['name']}</span>
                <span class="tactic-count">{len(techs)} techniques</span>
            </a>
            <div class="technique-list">
                {tech_cards}
            </div>
        </div>'''

    # Stats
    total_techniques = len(techniques)
    total_tactics = len(tactics)

    template = read_template("matrix.html")
    html = template.replace("{{COLUMNS}}", columns_html)
    html = html.replace("{{TOTAL_TECHNIQUES}}", str(total_techniques))
    html = html.replace("{{TOTAL_TACTICS}}", str(total_tactics))
    html = html.replace("{{VERSION}}", data["framework"]["version"])
    html = html.replace("{{LAST_UPDATED}}", data["framework"]["last_updated"])
    html = html.replace("{{FRAMEWORK_DESC}}", data["framework"]["description"])

    with open(OUTPUT_DIR / "index.html", "w") as f:
        f.write(html)

    print(f"  Matrix page: {total_tactics} tactics, {total_techniques} techniques")


def build_technique_pages(data):
    """Generate individual technique pages."""
    template = read_template("technique.html")
    techniques = data["techniques"]
    tactics_map = {t["id"]: t for t in data["tactics"]}
    tech_map = {t["id"]: t for t in techniques}

    for tech in techniques:
        tactic = tactics_map[tech["tactic_id"]]
        color = TACTIC_COLORS[tech["tactic_id"]]

        # Build success indicators list
        indicators_html = ""
        for ind in tech.get("success_indicators", []):
            indicators_html += f'<li>{ind}</li>\n'

        # Build failure modes list
        failures_html = ""
        for fail in tech.get("failure_modes", []):
            failures_html += f'<li>{fail}</li>\n'

        # Build related techniques links
        related_html = ""
        for rel_id in tech.get("related_techniques", []):
            if rel_id in tech_map:
                rel = tech_map[rel_id]
                related_html += f'<a href="{rel_id.lower()}.html" class="related-link">{rel_id}: {rel["name"]}</a>\n'

        # War story
        war_story = tech.get("war_story", {})
        war_story_html = ""
        if war_story and war_story.get("content"):
            war_story_html = f'''
            <section class="war-story">
                <h2>Field Report{': ' + war_story.get('title', '') if war_story.get('title') else ''}</h2>
                <div class="war-story-content">{war_story['content']}</div>
            </section>'''

        html = template.replace("{{TECH_ID}}", tech["id"])
        html = html.replace("{{TECH_NAME}}", tech["name"])
        html = html.replace("{{TACTIC_ID}}", tech["tactic_id"].lower())
        html = html.replace("{{TACTIC_NAME}}", tactic["name"])
        html = html.replace("{{TACTIC_COLOR}}", color["border"])
        html = html.replace("{{TACTIC_BG}}", color["bg"])
        html = html.replace("{{DESCRIPTION}}", tech.get("description", ""))
        html = html.replace("{{IMPLEMENTATION}}", tech.get("implementation", ""))
        html = html.replace("{{INDICATORS}}", indicators_html)
        html = html.replace("{{FAILURES}}", failures_html)
        html = html.replace("{{RELATED}}", related_html)
        html = html.replace("{{WAR_STORY}}", war_story_html)
        html = html.replace("{{VERSION}}", tech.get("added_version", "1.0"))

        filename = f"{tech['id'].lower()}.html"
        with open(OUTPUT_DIR / "techniques" / filename, "w") as f:
            f.write(html)

    print(f"  Technique pages: {len(techniques)} generated")


def build_tactic_pages(data):
    """Generate tactic overview pages."""
    template = read_template("tactic.html")
    techniques = data["techniques"]

    for tactic in data["tactics"]:
        color = TACTIC_COLORS[tactic["id"]]
        tactic_techs = [t for t in techniques if t["tactic_id"] == tactic["id"]]

        # Build technique table
        table_rows = ""
        for tech in tactic_techs:
            table_rows += f'''
            <tr>
                <td><a href="../techniques/{tech['id'].lower()}.html">{tech['id']}</a></td>
                <td><a href="../techniques/{tech['id'].lower()}.html">{tech['name']}</a></td>
                <td>{tech.get('description', '')}</td>
            </tr>'''

        html = template.replace("{{TACTIC_ID}}", tactic["id"])
        html = html.replace("{{TACTIC_NAME}}", tactic["name"])
        html = html.replace("{{TACTIC_DESC}}", tactic["description"])
        html = html.replace("{{TACTIC_COLOR}}", color["border"])
        html = html.replace("{{TACTIC_BG}}", color["bg"])
        html = html.replace("{{TECHNIQUE_COUNT}}", str(len(tactic_techs)))
        html = html.replace("{{TABLE_ROWS}}", table_rows)

        filename = f"{tactic['id'].lower()}.html"
        with open(OUTPUT_DIR / "tactics" / filename, "w") as f:
            f.write(html)

    print(f"  Tactic pages: {len(data['tactics'])} generated")


def build_about_page(data):
    """Generate the about page."""
    template = read_template("about.html")
    html = template.replace("{{VERSION}}", data["framework"]["version"])
    html = html.replace("{{LAST_UPDATED}}", data["framework"]["last_updated"])
    html = html.replace("{{TOTAL_TECHNIQUES}}", str(len(data["techniques"])))
    html = html.replace("{{TOTAL_TACTICS}}", str(len(data["tactics"])))

    with open(OUTPUT_DIR / "about.html", "w") as f:
        f.write(html)

    print("  About page generated")


def build_getting_started_page(data):
    """Generate the getting started page."""
    template = read_template("getting-started.html")
    html = template.replace("{{VERSION}}", data["framework"]["version"])

    with open(OUTPUT_DIR / "getting-started.html", "w") as f:
        f.write(html)

    print("  Getting Started page generated")


def build_terms_page(data):
    """Generate the terms of use page."""
    template = read_template("terms.html")

    with open(OUTPUT_DIR / "terms.html", "w") as f:
        f.write(template)

    print("  Terms page generated")


def main():
    print("FORGED Static Site Generator")
    print("=" * 50)

    print("\nLoading framework data...")
    data = load_framework()
    fw = data["framework"]
    print(f"  Framework: {fw['name']} v{fw['version']}")
    print(f"  Tactics: {len(data['tactics'])}")
    print(f"  Techniques: {len(data['techniques'])}")

    print("\nPreparing output directory...")
    ensure_output_dirs()

    print("\nCopying theme assets...")
    copy_theme_assets()

    print("\nGenerating pages...")
    build_matrix_page(data)
    build_technique_pages(data)
    build_tactic_pages(data)
    build_about_page(data)
    build_getting_started_page(data)
    build_terms_page(data)

    print("\n" + "=" * 50)
    print(f"Site generated at: {OUTPUT_DIR}")
    total_files = sum(1 for _ in OUTPUT_DIR.rglob("*.html"))
    print(f"Total HTML files: {total_files}")
    print("Done.")


if __name__ == "__main__":
    main()
