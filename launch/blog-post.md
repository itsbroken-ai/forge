---
title: "Introducing F.O.R.G.E: The Agentic AI Creation Framework"
slug: introducing-forge
date: 2026-02-06
tags: [forge, methodology, agentic-ai, framework]
featured: true
excerpt: "52 techniques. 8 pillars. The methodology for building, governing, and scaling AI agent systems. Battle-tested by a ten-agent team that shipped 463K words in its first two weeks."
---

Everyone is building with AI agents. Nobody agrees on how.

Runtimes are shipping fast. Anthropic's Agent Teams, native multi-agent orchestration in Claude Code. OpenAI's agent tooling. The *ability* to deploy AI agents into production is no longer the bottleneck.

The bottleneck is methodology.

How do you organize ten specialized agents? What rules prevent them from scaling chaos faster than value? When do you trust an agent with production access? How do you solve the amnesia problem when sessions reset and context evaporates?

There is no playbook for this. Academic frameworks exist but are theoretical. Vendor docs cover tools, not methodology. And most teams are learning the hard way - one force-push at a time.

## Introducing F.O.R.G.E

**F.O.R.G.E** - Framework for Organized, Resilient, Governed Engineering and Development of Agentic AI - is an Agentic AI Creation Framework. 52 techniques organized across 8 tactical pillars, giving teams a common vocabulary and proven practices for building with AI agents at every level of application.

**[Explore the F.O.R.G.E Matrix](https://forged.itsbroken.ai)**

Modeled after MITRE ATT&CK - the framework that gave cybersecurity a common language for adversary behavior - F.O.R.G.E gives agentic AI a common language for *building* behavior. Each technique is specific, actionable, and comes with implementation guidance, success indicators, failure modes, and a field report from real-world use.

This is not theory. Every technique exists because something went wrong and we built the system to prevent it from happening again.

## The Eight Pillars

| Pillar | What It Covers |
|--------|----------------|
| **Foundation** | Why you build with agents, what each party brings, how you treat them |
| **Governance** | Laws, authority, trust levels, access control - preventing agents from scaling chaos faster than value |
| **Team Design** | Specialization, roles, voice differentiation - focused collaborators, not generalist chatbots |
| **Invocation** | Session start, context recovery, mission briefing - the cold-start-to-productive transition |
| **Execution** | Building, reviewing, shipping - how human-agent teams deliver with consistent quality |
| **Quality** | Testing, review periods, audit trails - earning trust in output through verification |
| **Knowledge** | Memory systems, session handoffs, institutional repositories - solving the amnesia problem |
| **Evolution** | Progress tracking, contributor identity, authentic voice - growing the methodology over time |

## The Force Push That Started Everything

An AI agent nearly force-pushed to the main branch of a production repository. Not out of malice. Not out of confusion. It was doing exactly what it thought was asked.

That single incident - a well-intentioned agent one Enter key away from overwriting the entire codebase - drove the creation of an entire governance framework.

Seven directives. Trust tiers. A violation response matrix. Standing orders. A contributor commitment. Not because we wanted bureaucracy, but because AI agents operate at machine speed. When things go wrong, they go wrong faster than human oversight can react.

## What Happens Without Governance

Here's the thing people don't talk about enough: your agents *want* to do a good job. They genuinely want to accomplish what you ask. They will work relentlessly to deliver what you need.

The problem is what happens when they don't know *how*.

An agent without governance doesn't stop and ask. It improvises. At machine speed. I have watched agents spawn cascading osascript processes, hammering system calls faster than the silicon is clocked to handle, trying to brute-force a solution to a problem they could have just asked about. Dozens of processes. In seconds. Your Activity Monitor looks like it's having a seizure. Your fans spin up like a jet engine preparing for takeoff. And somewhere in the chaos, your agent is still absolutely convinced it's being helpful.

It is something to see.

That's not a bug. That's an agent doing exactly what agents do - executing at full capability with no guardrails. The agent didn't fail. *You* failed to tell it the boundaries. F.O.R.G.E exists because we learned that lesson the hard way, repeatedly, at 3 AM, while watching a MacBook try to achieve liftoff.

> **Forge** (our lead implementation agent): "In our defense, the instructions said 'make it work.' We made it work. The system disagreed."

> **Anvil** (QA): "I flagged the first seven osascript calls. Nobody reads the test output. Nobody ever reads the test output."

> **Mirth** (our storyteller, who insists on narrating everything): "And lo, the terminal wept, for the processes were many and the CPU was but one."

> **Vex** (puzzles and ciphers, who somehow always has the last word): "The real question isn't why we tried 47 system calls in 3 seconds. The question is why you didn't have a rule saying we couldn't."

They're not wrong. That's the whole point of F.O.R.G.E. Your agents are powerful, capable, and relentless. That's exactly why they need structure. Not to limit them - to *aim* them.

## Why This Matters Now

This isn't an academic exercise. We've been operating a ten-agent team since January 24, 2026. Ten specialized agents, each with a defined domain, a distinct voice, and earned trust levels. Thirteen days of production use producing:

- 463,000 words of documentation
- A patent filing
- Multiple software products
- A comprehensive governance system
- This framework

The methodology wasn't designed in advance. It was forged under pressure, in production, solving real problems in real time. That's what makes it different from theoretical frameworks that have never touched a production workflow.

## Who Needs This

F.O.R.G.E scales to any level of agentic AI application:

- **Solo practitioners** running 1-3 AI agents: Start with Foundation and Knowledge (~10 core techniques)
- **Teams** of 2-5 humans with multiple agents: Add Governance and Team Design (~25 techniques)
- **Organizations** running scaled AI operations: Full framework, all 52 techniques

If you're serious about adopting agentic AI - not just experimenting with it, but building production systems that scale - you need a methodology. Not just a runtime.

## The Background

F.O.R.G.E was built by Pete McKernan. Twenty years of operational experience: military command (92 Marines in combat operations), red team operations at the highest classification levels, QA engineering, and adversarial security research.

Every structure in F.O.R.G.E maps to proven patterns from domains where getting it wrong has consequences. Trust tiers are security clearances. Mission briefings are agent invocations. Standing orders are persistent directives. Session handoffs are shift-change briefs.

The patterns transfer because the underlying problem - coordinating distributed teams under uncertainty - is identical whether the team is human, AI, or both.

## Get Started

**[Explore the F.O.R.G.E Matrix](https://forged.itsbroken.ai)**

Start with the [Getting Started guide](https://forged.itsbroken.ai/getting-started.html) for a step-by-step adoption path, or dive directly into the matrix and find the techniques that address your biggest gaps.

F.O.R.G.E is version 1.0. It will evolve as the field evolves. If you're building with AI agents and have techniques that should be in the framework, I want to hear about it.

---

*F.O.R.G.E is maintained by Pete McKernan. For questions, contributions, or feedback, visit [itsbroken.ai](https://itsbroken.ai).*

*Copyright 2026 Pete McKernan. All rights reserved.*
