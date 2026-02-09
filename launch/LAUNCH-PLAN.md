# FORGED Launch Plan — February 6, 2026

## The Moment

Anthropic released Agent Teams (Opus 4.6) on February 5. They built the engine.
We release the methodology on February 6. We provide the mission briefing.

---

## LAUNCH CHECKLIST

### 1. Deploy Site to forged.itsbroken.ai

**Status:** Ready to deploy. 63 static HTML files in `/Projects/forged/output/`.

**Steps:**
- [ ] Initialize git repo in `/Projects/forged/`
- [x] Push to GitHub (itsbroken-ai org, transferred from TheCipherCircle 2026-02-09)
- [ ] Connect repo to Vercel
- [ ] Add custom domain `forged.itsbroken.ai` in Vercel project settings
- [ ] Add DNS record in Cloudflare: `forged` CNAME → `cname.vercel-dns.com`
- [ ] Verify SSL auto-provisions (~15 min)
- [ ] Test all pages load at `https://forged.itsbroken.ai`

**Vercel config:** Already created at `/Projects/forged/vercel.json`
- Build: `python3 data/generate_framework.py && python3 generator/build.py`
- Output: `output/`

### 2. Publish Blog Post

**Status:** Draft complete at `/Projects/forged/launch/blog-post.md`

**Steps:**
- [ ] Log into Ghost admin: `https://itsbroken-ai.ghost.io/ghost/`
- [ ] Create new post, paste blog content
- [ ] Set featured image (FORGED matrix screenshot or logo)
- [ ] Set tags: `forged`, `methodology`, `agentic-ai`, `framework`
- [ ] Set excerpt (from frontmatter)
- [ ] Mark as featured post
- [ ] Update all links to use `https://forged.itsbroken.ai` (confirm site is live first)
- [ ] Publish

### 3. Cross-Link

- [ ] FORGED site footer links to itsbroken.ai (already done)
- [ ] Blog post links to forged.itsbroken.ai (in draft)
- [ ] Add FORGED link to itsbroken.ai main navigation or about page
- [ ] Update itsbroken.ai homepage if appropriate

### 4. Social Announcement

**LinkedIn post (Pete's voice):**
> Yesterday Anthropic shipped Agent Teams — native multi-agent orchestration in Claude.
>
> Today I'm releasing the methodology for how to actually build with them.
>
> FORGED: 52 techniques across 8 pillars for building, governing, and scaling agentic AI systems. Modeled after MITRE ATT&CK. Battle-tested by a ten-agent team that shipped 463K words in 13 days.
>
> Not theory. Practice.
>
> forged.itsbroken.ai

**Twitter/X post:**
> Anthropic shipped the engine. We're releasing the mission briefing.
>
> FORGED — 52 techniques for agentic AI development. The ATT&CK matrix for building with AI agents.
>
> forged.itsbroken.ai

### 5. Verify

- [ ] Matrix page loads with all 8 tactics and 52 techniques
- [ ] Every technique cell is clickable
- [ ] Technique pages display all sections
- [ ] Search works (/ shortcut, Escape to clear)
- [ ] Mobile responsive
- [ ] Favicon shows in browser tab
- [ ] OG meta tags render in social preview (use https://www.opengraph.xyz/)
- [ ] Blog post links resolve correctly
- [ ] No broken links anywhere

---

## DEPLOYMENT ORDER

1. **Git init + push** (5 min)
2. **Vercel deploy** (5 min)
3. **Cloudflare DNS** (5 min + 15 min SSL)
4. **Verify site** (5 min)
5. **Publish blog** (10 min)
6. **Social posts** (5 min)

**Total estimated time: ~45 minutes from go.**

---

## POST-LAUNCH

- Monitor for broken links, rendering issues
- Watch for social engagement, respond to comments
- Capture launch as a war story for the book
- File trademark intent-to-use for "FORGED" (can do within the week)
  - Nice Class 41 (education/training): ~$250-350
  - Nice Class 42 (technology services): ~$250-350
  - Total: ~$500-700 for both classes
