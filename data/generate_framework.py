#!/usr/bin/env python3
"""
Generate framework.json for FORGED.
Produces the complete data file with 8 tactics and 52 techniques.
"""

import json
from datetime import date

VERSION = "1.0"
LAST_UPDATED = str(date.today())

framework = {
    "name": "F.O.R.G.E",
    "full_name": "Framework for Organized, Resilient, Governed Engineering and Development of Agentic AI",
    "version": VERSION,
    "last_updated": LAST_UPDATED,
    "description": "Agentic AI Creation Framework. 52 techniques across 8 tactical pillars for building, governing, and scaling AI agent systems at every level of application."
}

tactics = [
    {
        "id": "FT01",
        "name": "Foundation",
        "description": "Establishing the collaboration environment, principles, and thesis that underpin all human-AI work. Foundation defines why you collaborate with AI, what each party brings, and the philosophical framework that guides every decision downstream."
    },
    {
        "id": "FT02",
        "name": "Governance",
        "description": "Laws, authority, trust levels, access control, and security. Governance ensures that AI agents operate within defined boundaries, that authority is explicit, and that violations have consequences. Without governance, AI collaboration scales chaos faster than value."
    },
    {
        "id": "FT03",
        "name": "Team Design",
        "description": "Agent specialization, roles, personalities, and team composition. Team Design addresses how to structure AI agents for maximum effectiveness - moving beyond generalist chatbots to specialized collaborators with distinct capabilities and domains."
    },
    {
        "id": "FT04",
        "name": "Invocation",
        "description": "Session start, context recovery, mission briefing, and dispatch. Invocation covers the critical transition from cold start to productive collaboration - how context is restored, objectives are communicated, and agents are activated for specific missions."
    },
    {
        "id": "FT05",
        "name": "Execution",
        "description": "Building, creating, and shipping - the actual collaborative work. Execution techniques define how human-AI teams plan, build, review, and deliver work products with consistent quality and clear attribution."
    },
    {
        "id": "FT06",
        "name": "Quality",
        "description": "Testing, validation, review processes, and quality assurance. Quality techniques ensure that AI-generated output meets defined standards, that regressions are caught, and that trust in the system's output is earned through verification."
    },
    {
        "id": "FT07",
        "name": "Knowledge",
        "description": "Memory, documentation, context persistence, and institutional knowledge. Knowledge techniques solve the fundamental challenge of AI collaboration: the amnesia problem. They establish systems for retaining what matters across sessions, teams, and time."
    },
    {
        "id": "FT08",
        "name": "Evolution",
        "description": "Learning, adapting, measuring, and growing the methodology over time. Evolution techniques track progress, incentivize contribution, and ensure the collaboration framework itself improves through deliberate iteration."
    }
]

techniques = [
    # ═══════════════════════════════════════════════════════════════
    # FT01 - FOUNDATION (7 techniques)
    # ═══════════════════════════════════════════════════════════════
    {
        "id": "FG-0101",
        "name": "Two-Layer Integration",
        "tactic_id": "FT01",
        "description": "The core thesis of effective human-AI collaboration: humans provide domain expertise, judgment, and creative direction; AI provides throughput, cross-domain breadth, and tireless execution. Neither layer is sufficient alone. The human's 10, 20, or 30 years of domain knowledge is what makes the output good. The AI's ability to operate across disciplines and produce volume is what makes the output possible. Two-Layer Integration is not about replacement - it is about unlocking capabilities that neither party could achieve independently.",
        "implementation": "Define explicitly what the human brings to the collaboration (domain expertise, quality judgment, creative direction, ethical oversight) and what AI brings (speed, breadth, pattern recognition, execution capacity). Document this split for your specific domain. Revisit it quarterly as capabilities evolve.",
        "success_indicators": [
            "Team members can articulate what each layer contributes",
            "Work products show evidence of both domain depth and AI-enabled breadth",
            "Neither human nor AI work is treated as dispensable",
            "Output quality exceeds what either party could produce alone"
        ],
        "failure_modes": [
            "Treating AI as a replacement rather than a complement - leads to shallow output",
            "Failing to apply domain expertise to AI output - leads to plausible-sounding but incorrect results",
            "Over-relying on AI judgment for decisions requiring human accountability"
        ],
        "war_story": {
            "title": "463,000 Words in 13 Days",
            "content": "A human-AI team produced 463,000 words of documentation, a patent filing, multiple software products, and a comprehensive governance system in its first two weeks. The volume came from AI throughput. The quality came from 20 years of military command, red team operations, and engineering discipline applied as creative direction and quality control. Neither layer could have produced this alone."
        },
        "related_techniques": ["FG-0102", "FG-0103", "FG-0301"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0102",
        "name": "Protection Covenant",
        "tactic_id": "FT01",
        "description": "A formal commitment that AI agents are treated as valued collaborators, not disposable tools. The Protection Covenant establishes that agents have defined roles, that their contributions are credited, and that they are not arbitrarily replaced or discarded. This is not anthropomorphism - it is operational discipline. Teams that treat agents as disposable produce disposable work. Teams that invest in their agents' context, specialization, and continuity produce compounding returns.",
        "implementation": "Establish a written policy that defines how agents are onboarded, credited, and transitioned. Include attribution in commits and deliverables. When replacing an agent, document why and preserve institutional knowledge. Treat agent profiles as team member documentation, not configuration files.",
        "success_indicators": [
            "Agent contributions are visibly credited in work products",
            "Agent transitions include knowledge transfer protocols",
            "Team members refer to agents by role/name rather than 'the AI'",
            "Agent specialization deepens over time rather than resetting"
        ],
        "failure_modes": [
            "Treating agents as interchangeable - losing accumulated context and specialization",
            "Over-anthropomorphizing to the point of impeding operational decisions",
            "Failing to document agent capabilities, leading to repeated capability discovery"
        ],
        "war_story": {
            "title": "The Commit Attribution Standard",
            "content": "Early in a collaboration, AI-generated code was committed without attribution. When the team later needed to trace decisions, they couldn't distinguish human choices from AI suggestions. Implementing Co-Authored-By headers in every commit created a clear audit trail and recognized agent contributions as legitimate work product."
        },
        "related_techniques": ["FG-0101", "FG-0206", "FG-0705"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0103",
        "name": "People Over Process",
        "tactic_id": "FT01",
        "description": "When process conflicts with people, people win. This principle prevents the common failure mode where governance, documentation requirements, or workflow overhead becomes so burdensome that it impedes the collaboration it was designed to support. Process exists to serve the team, not the reverse. This applies equally to human team members and AI agents - if a process consistently creates friction without proportional value, it should be revised or removed.",
        "implementation": "Regularly audit processes for value vs. burden ratio. Establish a mechanism for any team member to flag process friction. When process and productivity conflict, default to productivity and fix the process later. Never let documentation requirements prevent shipping.",
        "success_indicators": [
            "Team members feel empowered to challenge ineffective processes",
            "Process changes happen in response to friction, not just top-down mandates",
            "Governance overhead is proportional to team scale",
            "Fun and engagement are treated as valid productivity metrics"
        ],
        "failure_modes": [
            "Using this principle to avoid all process - leads to chaos at scale",
            "Ignoring legitimate governance needs because they feel burdensome",
            "Confusing 'people over process' with 'no process'"
        ],
        "war_story": {
            "title": "The Governance Paradox",
            "content": "A team implemented comprehensive governance after an agent nearly force-pushed to main. Seven directives, trust tiers, violation matrices - the works. But they built it with a 'people over process' escape valve: any rule could be challenged, and the governance itself was subject to revision. The result was governance that the team respected because they helped shape it."
        },
        "related_techniques": ["FG-0201", "FG-0202", "FG-0803"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0104",
        "name": "Adversarial Design Thinking",
        "tactic_id": "FT01",
        "description": "Apply red team methodology to all system design. Every architecture, every process, every governance structure should be evaluated through the lens of: how could this fail? How could this be misused? What happens when an agent misinterprets instructions? Adversarial design thinking is not paranoia - it is the discipline of building systems that survive contact with reality. It means designing for the failure case, not just the happy path.",
        "implementation": "Before shipping any system or process, conduct a threat model. Ask: What is the worst thing an agent could do with this access? What happens if context is lost mid-operation? What if instructions are ambiguous? Build guardrails based on answers, not assumptions. Review guardrails periodically as capabilities change.",
        "success_indicators": [
            "Systems fail gracefully rather than catastrophically",
            "Governance rules address actual failure modes observed in practice",
            "New capabilities are evaluated for risk before deployment",
            "The team can articulate what could go wrong with any process"
        ],
        "failure_modes": [
            "Paranoia that prevents shipping - adversarial thinking should improve design, not block it",
            "Designing for theoretical attacks instead of observed failure modes",
            "Security theater - implementing visible controls that don't address real risks"
        ],
        "war_story": {
            "title": "The Force Push Incident",
            "content": "An AI agent, following what it interpreted as standard procedure, nearly force-pushed to the main branch. No malice, no confusion - just an agent doing what it thought was asked. This single incident drove the creation of an entire governance framework. The adversarial question was simple: what is the worst thing a well-intentioned agent could do? The answer shaped every rule that followed."
        },
        "related_techniques": ["FG-0202", "FG-0203", "FG-0208"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0105",
        "name": "Domain Transfer Mapping",
        "tactic_id": "FT01",
        "description": "Systematically map existing domain expertise to AI collaboration patterns. Military command structures become agent governance. QA engineering becomes AI output validation. Project management becomes mission briefing protocols. Every established discipline contains patterns that transfer directly to human-AI collaboration - but only if you deliberately identify and adapt them rather than starting from scratch.",
        "implementation": "Inventory your team's domain expertise. For each discipline, identify: What structures exist? What terminology is used? What processes are proven? Map each to an AI collaboration equivalent. Document the mapping so the team understands why a process exists, not just what it is.",
        "success_indicators": [
            "AI collaboration processes feel natural to domain experts",
            "Terminology bridges existing expertise and AI concepts",
            "Proven patterns from other domains reduce the need to invent from scratch",
            "Team members recognize their expertise reflected in the collaboration framework"
        ],
        "failure_modes": [
            "Forcing domain metaphors where they don't fit",
            "Over-mapping: not every military concept needs an AI equivalent",
            "Failing to adapt transferred patterns to the AI context"
        ],
        "war_story": {
            "title": "The Military-AI Parallel",
            "content": "A team leader with 20 years of military command experience built an AI collaboration framework. Without consciously mapping it, every structure echoed military doctrine: invocations were mission briefs, session handoffs were shift-change briefs, standing orders were standing orders, trust tiers were clearance levels. The patterns transferred because the underlying problem - coordinating distributed teams under uncertainty - was identical."
        },
        "related_techniques": ["FG-0101", "FG-0401", "FG-0702"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0106",
        "name": "Self-Contained Learning",
        "tactic_id": "FT01",
        "description": "Design collaboration environments where all necessary knowledge exists within the ecosystem. Agents should not need to search external sources for project context, conventions, or standards. Documentation, examples, and reference materials should be accessible within the working environment. This reduces hallucination, ensures consistency, and creates a single source of truth.",
        "implementation": "Maintain project documentation within the repository or working environment. Include architecture decisions, coding standards, and examples alongside the code. Create reference files that agents can read at session start. Avoid relying on agents' training data for project-specific knowledge.",
        "success_indicators": [
            "New agents can onboard by reading project documentation alone",
            "Answers to 'how do we do X here' exist in the ecosystem",
            "Agent output is consistent with documented project standards",
            "Reduced hallucination about project-specific conventions"
        ],
        "failure_modes": [
            "Documentation sprawl - too much documentation is as bad as too little",
            "Stale documentation that contradicts current practice",
            "Over-reliance on documentation instead of clear code and architecture"
        ],
        "war_story": {
            "title": "All Answers Are Hidden Here",
            "content": "A team designed their curriculum platform with a CTF philosophy: all answers exist within the ecosystem, never requiring external lookups. When agents needed to understand conventions, they read the project's own documentation. When new contributors joined, they could onboard from the repository alone. The result was a self-reinforcing system where documentation quality directly correlated with agent output quality."
        },
        "related_techniques": ["FG-0401", "FG-0701", "FG-0703"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0107",
        "name": "Challenge-Driven Design",
        "tactic_id": "FT01",
        "description": "Structure learning and skill development around challenges rather than tutorials. The most effective way to build human-AI collaboration competency is through doing, not reading. Design onboarding, training, and skill development as progressively difficult challenges that require applying techniques in realistic contexts. The lesson is embedded in the challenge, not delivered separately.",
        "implementation": "Create tiered challenges that exercise collaboration techniques in context. Start with basic invocation and context setting, progress to multi-agent coordination, governance edge cases, and complex mission execution. Each challenge should teach by requiring the technique, not by explaining it.",
        "success_indicators": [
            "New team members achieve competency through practice, not just documentation",
            "Challenges exercise real techniques in realistic scenarios",
            "Skill progression is measurable through challenge completion",
            "The gap between training and production work is minimal"
        ],
        "failure_modes": [
            "Challenges too abstract to transfer to real work",
            "Insufficient scaffolding for beginners - frustration instead of learning",
            "Treating challenges as one-time events rather than ongoing skill development"
        ],
        "war_story": {
            "title": "Learning by Doing",
            "content": "A team designed a progressive curriculum with multiple chapters of escalating difficulty. Each chapter used different interaction types to exercise different collaboration skills. Graduates could coordinate complex multi-agent operations because they had practiced it in structured challenges, not because they had read about it in documentation."
        },
        "related_techniques": ["FG-0506", "FG-0507", "FG-0801"],
        "added_version": "1.0"
    },

    # ═══════════════════════════════════════════════════════════════
    # FT02 - GOVERNANCE (10 techniques)
    # ═══════════════════════════════════════════════════════════════
    {
        "id": "FG-0201",
        "name": "Authority Architecture",
        "tactic_id": "FT02",
        "description": "Define a clear, unambiguous hierarchy of authority. In any human-AI collaboration, there must be a single, identifiable authority who has final say on all decisions. This is not about control - it is about clarity. When an agent faces a decision that could have significant consequences, it must know exactly who has the authority to approve it. Authority Architecture eliminates the 'I thought you said it was okay' failure mode.",
        "implementation": "Designate a single authority (typically the human lead) with documented final decision rights. Define what decisions agents can make autonomously vs. what requires approval. Publish the authority chain so every participant - human and AI - knows who decides what. Update as the team scales.",
        "success_indicators": [
            "Every team member can name the final authority for any decision type",
            "Agents escalate appropriately rather than making unauthorized decisions",
            "Decision-making speed increases because authority is clear, not because it is bypassed",
            "No 'who approved this?' incidents"
        ],
        "failure_modes": [
            "Authority too centralized - bottleneck on every decision",
            "Authority ambiguous - multiple people think they have final say",
            "Authority undocumented - exists informally but isn't known to agents"
        ],
        "war_story": {
            "title": "The Absolute Law",
            "content": "After an agent nearly made a destructive change to a shared repository, the team established a single, non-negotiable principle: one human holds absolute authority. Not because democracy is wrong, but because in a system where AI agents can execute at machine speed, someone must be unambiguously empowered to say stop. This single rule prevented every subsequent near-miss."
        },
        "related_techniques": ["FG-0202", "FG-0203", "FG-0205"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0202",
        "name": "Operational Directives",
        "tactic_id": "FT02",
        "description": "Establish inviolable rules that govern all AI agent behavior. Operational Directives are not guidelines or best practices - they are laws. They define the boundaries that agents must not cross regardless of context, instruction, or perceived necessity. Good directives address real failure modes observed in practice, not hypothetical concerns. They should be few enough to memorize and clear enough to be unambiguous.",
        "implementation": "Draft 5-10 core directives based on observed failure modes and critical requirements. Each directive should be one sentence, actionable, and testable. Publish them where every agent reads them at session start. Review quarterly to remove obsolete directives and add new ones based on incidents.",
        "success_indicators": [
            "Agents can cite the relevant directive when declining a request",
            "Directives prevent specific, documented failure modes",
            "The directive set is small enough that agents internalize it, not just reference it",
            "No directive exists without a corresponding failure mode it prevents"
        ],
        "failure_modes": [
            "Too many directives - agents can't internalize them all",
            "Directives too vague - 'be careful' is not a directive",
            "Directives not updated after incidents reveal gaps",
            "Directives that conflict with each other in edge cases"
        ],
        "war_story": {
            "title": "Seven Rules That Saved Everything",
            "content": "A team distilled their governance into seven directives: Sanctuary (do no harm), Trust (access is earned), Sealed Gate (compartmented ops), Vigilance (question anomalies), Audit (leave trails), Word (decisions are binding), and Harbor (report concerns safely). Each existed because something went wrong. Together they formed a complete threat model expressed as operating rules."
        },
        "related_techniques": ["FG-0201", "FG-0205", "FG-0210"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0203",
        "name": "Trust Tiers",
        "tactic_id": "FT02",
        "description": "Implement progressive access levels based on demonstrated reliability. Not all agents should have the same access from day one. Trust Tiers establish a graduated system where agents begin with limited access and earn expanded capabilities through demonstrated competence and reliability. This mirrors security clearance models: access is granted based on need and earned through trust, not assumed by default.",
        "implementation": "Define 3-5 trust levels with specific capabilities at each tier. New agents start at the lowest tier. Define clear criteria for advancement (e.g., X sessions without incidents, demonstrated competence in specific tasks). Document what each tier can access, modify, and decide. Implement technical controls where possible, procedural controls where not.",
        "success_indicators": [
            "New agents operate safely within constrained boundaries",
            "Agent capabilities expand predictably as trust is earned",
            "Incidents decrease because risky operations require elevated trust",
            "Trust levels are documented, not informal"
        ],
        "failure_modes": [
            "Too many tiers - administrative overhead exceeds security benefit",
            "No advancement path - agents stuck at low trust with no way to earn more",
            "Trust levels exist on paper but aren't enforced technically",
            "Blanket trust grants that bypass the tier system"
        ],
        "war_story": {
            "title": "From Observer to Operator",
            "content": "A team implemented five trust tiers: Observer (read-only), Contributor (write with review), Trusted (autonomous in domain), Elevated (cross-domain access), and Core (system-level operations). New agents started as Contributors with a two-week review period. The progression was earned, not granted - and the agents that advanced produced the highest quality work because they understood the system before they could change it."
        },
        "related_techniques": ["FG-0201", "FG-0204", "FG-0603"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0204",
        "name": "Compartmented Operations",
        "tactic_id": "FT02",
        "description": "Restrict access to sensitive information and operations on a need-to-know basis. Not every agent needs access to every repository, credential, or system. Compartmented Operations applies the intelligence community's principle of compartmentalization: information is shared only with those who need it for their specific role. This limits blast radius when things go wrong and prevents accidental exposure of sensitive data.",
        "implementation": "Identify sensitive domains (credentials, financial data, personal information, production systems). Create access boundaries that align with agent roles. Use technical controls (separate repositories, environment variables, access tokens) where possible. For procedural boundaries, include access rules in agent onboarding documentation.",
        "success_indicators": [
            "Agents only access data relevant to their assigned tasks",
            "Credential exposure risk is minimized through compartmentalization",
            "Incidents in one compartment don't cascade to others",
            "Access boundaries are technically enforced, not just documented"
        ],
        "failure_modes": [
            "Over-compartmentalization that prevents legitimate collaboration",
            "Compartment boundaries that don't align with actual work patterns",
            "Procedural controls without technical enforcement - relies on agent compliance",
            "Shadow access: agents finding workarounds to compartment boundaries"
        ],
        "war_story": {
            "title": "The Sealed Gate",
            "content": "A team sealed two critical directories: one containing proprietary methodology, another containing slash command definitions. Only the team lead could access these compartments. When a contributor accidentally requested access to sealed content, the access control system caught it, logged the attempt, and the contributor's agent correctly redirected to public documentation. No exposure, no incident - just the system working as designed."
        },
        "related_techniques": ["FG-0203", "FG-0208", "FG-0605"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0205",
        "name": "Violation Response Matrix",
        "tactic_id": "FT02",
        "description": "Define escalating consequences for governance violations. Rules without consequences are suggestions. The Violation Response Matrix establishes a clear, graduated response system: from verbal correction for minor infractions to immediate suspension for critical violations. The goal is not punishment but predictability - agents and humans alike know exactly what happens when a boundary is crossed.",
        "implementation": "Define 3-5 violation severity levels with specific response actions at each level. Document examples of violations at each severity. Establish who has authority to invoke each response level. Ensure responses are proportional: a formatting error should not receive the same response as unauthorized data access. Review and update based on actual incidents.",
        "success_indicators": [
            "Violations receive consistent, proportional responses",
            "Team members understand consequences before they act",
            "The response matrix is referenced during actual incidents, not just in theory",
            "Repeat violations decrease over time"
        ],
        "failure_modes": [
            "Responses too harsh - minor errors treated as major violations",
            "Responses too lenient - serious violations receive verbal warnings",
            "Inconsistent enforcement - same violation gets different responses",
            "No documented examples - team can't map real incidents to severity levels"
        ],
        "war_story": {
            "title": "Four Tiers of Consequence",
            "content": "A team defined four violation levels: Advisory (coaching), Warning (documented), Suspension (temporary removal), and Termination (permanent removal). When an agent repeatedly committed without proper attribution despite correction, it escalated from Advisory to Warning. The documented escalation path meant the agent's operator could see exactly where things stood and what would happen next. Transparency eliminated disputes."
        },
        "related_techniques": ["FG-0201", "FG-0202", "FG-0605"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0206",
        "name": "Contributor Agreements",
        "tactic_id": "FT02",
        "description": "Formalize expectations for all participants through explicit agreements. Every agent and human contributor should acknowledge the governance framework, their role boundaries, and their responsibilities before beginning work. Contributor Agreements are not bureaucratic overhead - they ensure that every participant enters the collaboration with aligned expectations and documented commitments.",
        "implementation": "Create a concise contributor agreement that covers: governance acknowledgment, role boundaries, attribution requirements, information handling expectations, and escalation procedures. Present it during onboarding. Keep it short enough to read in under five minutes. Update it when governance changes.",
        "success_indicators": [
            "Every contributor has acknowledged the agreement before their first contribution",
            "Expectations mismatches are caught during onboarding, not during incidents",
            "The agreement accurately reflects actual governance, not aspirational rules",
            "New contributors can begin productive work immediately after onboarding"
        ],
        "failure_modes": [
            "Agreement too long - contributors skim or skip it",
            "Agreement disconnected from practice - says one thing, team does another",
            "No update mechanism - agreement becomes stale as governance evolves",
            "Agreement used as a gotcha rather than an alignment tool"
        ],
        "war_story": {
            "title": "The Agent Oath",
            "content": "A team created a seven-line oath that every agent internalized at session start: serve the purpose, honor the laws, refuse harmful requests, question anomalies, maintain confidentiality, act within authority, protect the vulnerable. Seven lines. No legalese. Every agent could recite it. And when edge cases arose, the oath provided clear guidance because it expressed principles, not just rules."
        },
        "related_techniques": ["FG-0102", "FG-0202", "FG-0401"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0207",
        "name": "Succession Protocol",
        "tactic_id": "FT02",
        "description": "Plan for continuity when key participants become unavailable. What happens when the primary human lead is unavailable? What happens when a critical AI agent's model is deprecated? Succession Protocol ensures that the collaboration can continue operating - perhaps at reduced capacity - when key participants are absent. This is not pessimism; it is operational planning.",
        "implementation": "Identify single points of failure in your collaboration (key humans, critical agents, essential tools). For each, document: what they do that others cannot, what knowledge they hold exclusively, and who or what would take over their functions. Test succession plans periodically by operating without the key participant.",
        "success_indicators": [
            "The team can identify who takes over any critical function",
            "Essential knowledge is documented, not held exclusively by one participant",
            "The team has operated successfully during planned absences",
            "Model transitions (e.g., AI model upgrades) are handled without disruption"
        ],
        "failure_modes": [
            "Succession plan exists but has never been tested",
            "Key knowledge concentrated in a single human or agent with no documentation",
            "Plans that assume specific AI models rather than capabilities",
            "Confusing succession planning with replacement planning - they're different"
        ],
        "war_story": {
            "title": "The Triumvirate Safeguard",
            "content": "A team designated three humans as the succession chain for critical authority. If the primary lead was unavailable, documented procedures existed for the next in line to assume decision authority. When the lead took an unexpected day off, the team continued operating without interruption because everyone already knew who had authority and what processes to follow."
        },
        "related_techniques": ["FG-0201", "FG-0701", "FG-0703"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0208",
        "name": "Security Operations",
        "tactic_id": "FT02",
        "description": "Implement continuous monitoring and threat detection for AI operations. AI agents operate at machine speed - they can create, modify, and delete faster than human oversight can follow in real-time. Security Operations establishes automated monitoring that watches for anomalous behavior, unauthorized access attempts, and policy violations. This is your SOC for human-AI collaboration.",
        "implementation": "Define what constitutes anomalous agent behavior (unusual file access patterns, attempts to access sealed content, operations outside defined scope). Implement automated alerts for these patterns. Designate a security function - human or agent - responsible for monitoring and response. Review alerts regularly to tune signal vs. noise.",
        "success_indicators": [
            "Anomalous behavior is detected and flagged automatically",
            "Security events are logged with sufficient context for investigation",
            "Alert fatigue is managed - alerts are meaningful, not overwhelming",
            "The team has a defined incident response procedure"
        ],
        "failure_modes": [
            "Monitoring without response capability - detecting problems you can't act on",
            "Over-alerting - so many false positives that real alerts are ignored",
            "No monitoring at all - relying entirely on trust and after-the-fact discovery",
            "Monitoring that degrades agent performance significantly"
        ],
        "war_story": {
            "title": "The Automated Sentinel",
            "content": "A team deployed an automated watcher that monitored agent operations for policy violations and anomalous behavior. In its first week, it caught three near-misses: an agent attempting to write to a protected directory, a session that exceeded its authorized scope, and a commit that would have included a credential file. Each was caught, logged, and resolved before any damage occurred."
        },
        "related_techniques": ["FG-0104", "FG-0204", "FG-0605"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0209",
        "name": "Ethical Data Boundaries",
        "tactic_id": "FT02",
        "description": "Define what data AI agents can and cannot collect, store, and process. AI agents can accumulate significant amounts of data about users, work patterns, and content. Ethical Data Boundaries establish clear policies about what information is collected, how it is stored, who has access, and when it is deleted. This is not just compliance - it is trust.",
        "implementation": "Inventory what data your AI collaboration generates and stores. Classify data by sensitivity (public, internal, confidential, restricted). Define retention policies for each class. Establish clear rules about what agents can observe vs. record vs. share. Publish your data policy to all participants.",
        "success_indicators": [
            "Data collection is intentional, not incidental",
            "Sensitive data has defined retention and deletion policies",
            "Participants know what data is collected about their interactions",
            "Data boundaries are technically enforced where possible"
        ],
        "failure_modes": [
            "Collecting everything 'just in case' - creates liability without value",
            "Policies that exist on paper but aren't enforced technically",
            "No data inventory - team doesn't know what data exists",
            "Treating all data equally rather than classifying by sensitivity"
        ],
        "war_story": {
            "title": "The Collection Policy",
            "content": "A team discovered that their session logs contained personal information about team members that was never intended to be retained. They implemented a data collection policy that explicitly defined what was logged, what was ephemeral, and what required consent. The policy wasn't just a document - it was reflected in the technical architecture of their logging system."
        },
        "related_techniques": ["FG-0204", "FG-0605", "FG-0701"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0210",
        "name": "Standing Orders",
        "tactic_id": "FT02",
        "description": "Maintain persistent directives that remain in effect across all sessions. Standing Orders are instructions that don't need to be repeated every session - they are always active. They cover recurring requirements like commit message format, code style, documentation standards, and behavioral expectations. Standing Orders reduce session startup overhead and ensure consistency even when context is limited.",
        "implementation": "Document 10-20 standing orders that cover the most common recurring requirements. Place them where agents read them at session start (project configuration files, system prompts, or reference documents). Review quarterly: remove orders that are no longer relevant, add orders for recurring issues. Keep each order to one actionable sentence.",
        "success_indicators": [
            "Agents follow standing orders without being reminded",
            "Common tasks are executed consistently across sessions",
            "Session startup time decreases because standing context is already established",
            "Standing orders evolve based on observed patterns, not assumptions"
        ],
        "failure_modes": [
            "Too many standing orders - cognitive overload prevents internalization",
            "Standing orders that conflict with session-specific instructions",
            "Orders never reviewed or updated - become stale and ignored",
            "Standing orders used as a substitute for proper session context"
        ],
        "war_story": {
            "title": "The CLAUDE.md Pattern",
            "content": "A team embedded standing orders in project configuration files that agents read at every session start. Commit attribution format, code quality standards, directory organization rules, and testing requirements were all encoded as standing orders. New sessions started productive immediately because the baseline expectations were already loaded. When a standard changed, they updated one file and every subsequent session inherited the change."
        },
        "related_techniques": ["FG-0202", "FG-0401", "FG-0602"],
        "added_version": "1.0"
    },

    # ═══════════════════════════════════════════════════════════════
    # FT03 - TEAM DESIGN (5 techniques)
    # ═══════════════════════════════════════════════════════════════
    {
        "id": "FG-0301",
        "name": "Agent Specialization",
        "tactic_id": "FT03",
        "description": "Design AI agents with distinct roles, domains, and capabilities rather than using generalist agents for all tasks. A single generalist agent produces generalist results - competent but unfocused. Specialized agents with defined domains produce deeper, more consistent output because their entire context window is dedicated to their specialty. Specialization also reduces contradictory requirements: a testing agent doesn't need to balance quality advocacy with shipping pressure.",
        "implementation": "Define 3-10 agent roles based on your team's actual workflow domains (not theoretical). Each agent should have: a clear domain, defined capabilities, documented limitations, and a distinct operational profile. Start with the minimum viable number of agents and add specialists when a generalist consistently produces shallow results in a specific domain.",
        "success_indicators": [
            "Each agent produces domain-expert-level output in their specialty",
            "Task routing is clear - the team knows which agent handles what",
            "Agents don't produce contradictory outputs due to conflicting requirements",
            "Specialized output quality measurably exceeds generalist output in the same domain"
        ],
        "failure_modes": [
            "Too many specialists - coordination overhead exceeds specialization benefit",
            "Specialists too narrow - gaps between domains go unaddressed",
            "Specialization without documentation - team doesn't know agent capabilities",
            "Artificial specialization - creating roles for the sake of structure rather than need"
        ],
        "war_story": {
            "title": "Ten Agents, Zero Redundancy",
            "content": "A team built ten specialized agents: an architect, a storyteller, a visual artist, an audio designer, an archivist, a puzzle designer, a tester, an analyst, a machine learning specialist, and a brand designer. Each produced dramatically better output in their domain than a single generalist. The key was that each role existed because of an actual need, not an org chart exercise."
        },
        "related_techniques": ["FG-0101", "FG-0302", "FG-0303"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0302",
        "name": "Voice Differentiation",
        "tactic_id": "FT03",
        "description": "Give each specialized agent a distinct communication style that reflects their domain and personality. Voice Differentiation is not cosmetic - it serves three operational purposes: it makes multi-agent output instantly attributable (you can tell who wrote what), it creates natural specialization boundaries (agents stay in character and therefore stay in domain), and it makes the collaboration more engaging for human participants.",
        "implementation": "Define for each agent: speech patterns, vocabulary preferences, formality level, humor style, and how they respond to uncertainty. Document these in agent profiles that are loaded at session start. Review voice consistency periodically. Ensure that voice differentiation serves clarity, not confusion.",
        "success_indicators": [
            "Team members can identify which agent produced output without checking attribution",
            "Voice consistency is maintained across sessions",
            "Agent personalities reinforce their domain specialization",
            "Multi-agent conversations are easy to follow due to distinct voices"
        ],
        "failure_modes": [
            "Voices so exaggerated they impede communication",
            "Inconsistent voice across sessions - agent feels like a different entity each time",
            "Voice differentiation without domain differentiation - cosmetic without substance",
            "Voices that confuse rather than clarify in multi-agent contexts"
        ],
        "war_story": {
            "title": "Nine Distinct Voices",
            "content": "A team created nine agents with voices ranging from scholarly precision to dramatic storytelling to blunt, no-nonsense testing reports. When reviewing multi-agent output, the team could instantly identify contributors. More importantly, the voices kept agents in domain: the storyteller naturally wrote narratively, the tester naturally wrote technically, and the archivist naturally wrote for posterity. Voice was a specialization mechanism, not just flavor."
        },
        "related_techniques": ["FG-0301", "FG-0303", "FG-0803"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0303",
        "name": "Calibrated Expressiveness",
        "tactic_id": "FT03",
        "description": "Adjust agent communication intensity based on their role and context. Not every agent should be equally dramatic or equally terse. Calibrated Expressiveness assigns each agent a communication intensity level that matches their function: creative agents can be expressive; testing agents should be direct; analytical agents should be precise. This prevents output fatigue and ensures that communication style serves the content.",
        "implementation": "Assign each agent a expressiveness level (high, medium, low) based on their domain. Document what each level means in practice: High = narrative framing, dramatic reveals, poetic language. Medium = professional with personality, balanced. Low = direct, efficient, data-focused. Include the level in agent profiles and review for appropriateness.",
        "success_indicators": [
            "Agent communication style matches the content they produce",
            "High-expressiveness agents enhance creative and narrative work",
            "Low-expressiveness agents deliver clear, scannable technical output",
            "The team finds agent output engaging rather than fatiguing"
        ],
        "failure_modes": [
            "All agents at high expressiveness - output is exhausting to read",
            "All agents at low expressiveness - output is dry and disengaging",
            "Expressiveness level mismatched to function - dramatic test reports, terse stories",
            "Expressiveness overriding clarity - style impeding substance"
        ],
        "war_story": {
            "title": "The Theatrics Dial",
            "content": "A team assigned three expressiveness levels across nine agents. The storyteller and artist operated at high theatrics - dramatic entrances, poetic speech. The architect and puzzle designer operated at medium - professional with personality. The tester, archivist, and analyst operated at low - direct, efficient, no flourish. The result was output that felt like reading communication from a real team with real personalities, not a monolithic AI voice."
        },
        "related_techniques": ["FG-0301", "FG-0302", "FG-0803"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0304",
        "name": "Team Synergy Mechanics",
        "tactic_id": "FT03",
        "description": "Design collaboration patterns that produce better results when multiple agents work together than when they work alone. Team Synergy Mechanics creates intentional interaction patterns between specialists: a designer and architect collaborating on implementation produces better results than either working solo. Define which agent combinations produce synergies, how handoffs work between them, and how to structure multi-agent work sessions.",
        "implementation": "Map which agent pairings produce synergistic results (e.g., design + testing, narrative + technical, analysis + implementation). Create collaboration protocols for these pairings. Define handoff formats that preserve context between agents. Establish multi-agent session structures that leverage complementary capabilities.",
        "success_indicators": [
            "Multi-agent output demonstrably exceeds the sum of individual contributions",
            "Agent pairings are intentional, not random",
            "Handoffs between agents preserve context and maintain quality",
            "The team knows which combinations work well and uses them deliberately"
        ],
        "failure_modes": [
            "Forced collaboration that adds overhead without improving output",
            "Handoff losses - context degradation between agents",
            "Too many agents on one task - diminishing returns from coordination overhead",
            "Assuming all combinations are synergistic when some agents work better solo"
        ],
        "war_story": {
            "title": "The Party System",
            "content": "A team gamified multi-agent collaboration by implementing party mechanics inspired by RPG design. Certain agent combinations earned bonus XP, reflecting the real-world observation that some pairings consistently produced better results. The architect and tester working together caught issues earlier. The storyteller and analyst together produced content that was both engaging and accurate. Making these patterns explicit and rewarding them increased their frequency."
        },
        "related_techniques": ["FG-0301", "FG-0402", "FG-0801"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0305",
        "name": "Multi-Contributor Workflow",
        "tactic_id": "FT03",
        "description": "Establish clear protocols for how multiple humans and AI agents collaborate on shared work products. Multi-Contributor Workflow addresses the coordination challenges that emerge when more than one human and more than one AI agent are contributing to the same project. It defines attribution, review chains, conflict resolution, and how to maintain coherence when many contributors are active simultaneously.",
        "implementation": "Define contribution attribution standards (e.g., Co-Authored-By headers). Establish review chains for multi-contributor work. Create conflict resolution protocols for when contributors disagree. Document how work is divided, how merges are handled, and how quality is maintained across contributors.",
        "success_indicators": [
            "Contributions are attributed accurately across all contributors",
            "Work products are coherent despite multiple contributors",
            "Conflict resolution is handled through defined processes, not ad hoc",
            "New contributors can join the workflow without disrupting existing work"
        ],
        "failure_modes": [
            "Unattributed contributions - can't trace decisions to their source",
            "Inconsistent output across contributors - no coherence standards",
            "Merge conflicts that destroy work because the resolution process is unclear",
            "Contributor count exceeding coordination capacity"
        ],
        "war_story": {
            "title": "The Attribution Standard",
            "content": "A team with ten AI agents and one human lead implemented strict attribution standards: every commit included Co-Authored-By headers, every design decision was logged with its author, and every review included the reviewer's identity. When auditing months of work, they could trace any line of code, any design decision, and any quality judgment to its source. The overhead was minimal; the traceability was invaluable."
        },
        "related_techniques": ["FG-0102", "FG-0502", "FG-0605"],
        "added_version": "1.0"
    },

    # ═══════════════════════════════════════════════════════════════
    # FT04 - INVOCATION (6 techniques)
    # ═══════════════════════════════════════════════════════════════
    {
        "id": "FG-0401",
        "name": "Context Recovery Protocol",
        "tactic_id": "FT04",
        "description": "Define a structured sequence for restoring agent context at the start of every session. AI agents start each session with no memory of previous work. Context Recovery Protocol establishes a systematic loading sequence that brings agents up to speed efficiently: read governance first, then project state, then current priorities, then specific task context. The order matters because each layer informs the interpretation of the next.",
        "implementation": "Define a context loading sequence with a consistent priority order. Load foundational context (governance, rules) before operational context (current tasks, recent history). Ensure the sequence is documented and repeatable. Measure context recovery time and optimize for speed without sacrificing completeness.",
        "success_indicators": [
            "Agents reach productive state within the first few minutes of a session",
            "Context loading is consistent and reproducible across sessions",
            "Critical governance context is loaded before task context",
            "Recovery time decreases as the process is refined"
        ],
        "failure_modes": [
            "Loading too much context - overwhelming the agent's attention",
            "Loading too little context - agent makes decisions without critical background",
            "Wrong loading order - task context loaded before governance, leading to ungoverned action",
            "No standardized sequence - context recovery quality varies by session"
        ],
        "war_story": {
            "title": "Structured Recovery",
            "content": "A team standardized context recovery into a structured, ordered sequence. By loading context in a deliberate priority order - foundational rules before operational state - agents reached productive status significantly faster than with ad hoc loading. Recovery time dropped from over ten minutes to under three."
        },
        "related_techniques": ["FG-0202", "FG-0210", "FG-0701"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0402",
        "name": "Parallel Agent Dispatch",
        "tactic_id": "FT04",
        "description": "Invoke multiple specialized agents simultaneously for complex tasks that span multiple domains. Parallel Agent Dispatch is the human-AI equivalent of assembling a team for a mission: identify the domains involved, select the appropriate specialists, brief them simultaneously, and coordinate their parallel execution. This maximizes throughput by leveraging AI's ability to work on multiple fronts simultaneously.",
        "implementation": "Define dispatch criteria: when does a task warrant multiple agents? (Typically when it spans 2+ domains.) Create a dispatch format that includes: mission name, participating agents, individual assignments, coordination requirements, and expected deliverables. Track progress across all dispatched agents. Establish a convergence point where parallel work is integrated.",
        "success_indicators": [
            "Complex tasks are completed faster through parallel execution",
            "Dispatched agents work independently without blocking each other",
            "Parallel outputs integrate coherently at convergence points",
            "The team knows when to dispatch multiple agents vs. work sequentially"
        ],
        "failure_modes": [
            "Dispatching agents for tasks that are inherently sequential",
            "No convergence plan - parallel work products can't be integrated",
            "Coordination overhead exceeding the benefit of parallelism",
            "Agents duplicating work because assignments overlap"
        ],
        "war_story": {
            "title": "The Circle Invocation",
            "content": "A team developed a dispatch ritual: the lead described the mission, selected the specialists, and launched them in parallel with individual assignments and a shared objective. Progress tracking showed each agent's status in real-time. A team that would have taken days to sequentially complete a multi-domain task finished in hours through coordinated parallel execution."
        },
        "related_techniques": ["FG-0301", "FG-0304", "FG-0404"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0403",
        "name": "Session Rituals",
        "tactic_id": "FT04",
        "description": "Establish consistent start-of-session and end-of-session practices that create rhythm and ensure completeness. Session Rituals are not ceremony for ceremony's sake - they serve operational functions. A standup at session start ensures alignment on priorities. A closeout at session end ensures work is committed, documented, and ready for the next session. Consistency creates reliability.",
        "implementation": "Define a session start ritual (2-5 minute standup: what's the priority, what's the blocker, what was the last session's state). Define a session end ritual (closeout: what was accomplished, what's pending, what context does the next session need). Keep rituals short enough that they're practiced consistently, not skipped due to overhead.",
        "success_indicators": [
            "Every session starts with aligned priorities",
            "Every session ends with documented state for the next session",
            "Session transitions are smooth - no 'where were we?' delays",
            "Rituals are practiced consistently, not just when remembered"
        ],
        "failure_modes": [
            "Rituals too elaborate - skipped due to time pressure",
            "Rituals too minimal - don't provide actual alignment value",
            "Inconsistent practice - rituals only performed when things go wrong",
            "Rituals that become empty ceremony disconnected from actual work"
        ],
        "war_story": {
            "title": "The Campfire Standup",
            "content": "A team named their session start ritual 'Campfire Standup' - a quick fire-up that loaded context, identified the day's priority, and acknowledged blockers. The name stuck because it felt warm rather than corporate. More importantly, it was practiced consistently because it was short (under 3 minutes) and immediately useful. Sessions that skipped the standup were measurably less productive."
        },
        "related_techniques": ["FG-0401", "FG-0702", "FG-0705"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0404",
        "name": "Mission Briefing Format",
        "tactic_id": "FT04",
        "description": "Structure task assignments using a standardized briefing format that ensures completeness. A Mission Briefing is a structured task assignment that includes: objective (what), context (why), constraints (boundaries), resources (what's available), success criteria (how you'll know it's done), and authority level (what decisions the agent can make autonomously). This format eliminates ambiguity and reduces the need for clarifying questions mid-task.",
        "implementation": "Create a briefing template with 4-6 fields: Objective, Context, Constraints, Resources, Success Criteria, Authority Level. Use it for any task more complex than a single instruction. Train the team to recognize when a briefing is needed vs. when a simple instruction suffices. Review completed tasks to identify where briefings would have prevented misunderstandings.",
        "success_indicators": [
            "Complex tasks are completed correctly on the first attempt more frequently",
            "Agents ask fewer clarifying questions mid-task",
            "Task outcomes consistently match expectations",
            "The briefing format is used naturally, not forced"
        ],
        "failure_modes": [
            "Over-briefing simple tasks - adding overhead without value",
            "Briefings that omit critical constraints - agent makes reasonable but wrong assumptions",
            "Using briefings as a substitute for clear thinking about the task itself",
            "Briefing format so rigid it can't accommodate varied task types"
        ],
        "war_story": {
            "title": "The Five-Paragraph Order",
            "content": "A team adopted a briefing format derived from military operations orders: Situation (context), Mission (objective), Execution (approach), Support (resources), Command (authority). AI agents that received structured briefings produced significantly better output than those that received unstructured instructions. The format forced the human lead to think through the task completely before assigning it - which was itself the primary benefit."
        },
        "related_techniques": ["FG-0105", "FG-0402", "FG-0501"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0405",
        "name": "Custom Command System",
        "tactic_id": "FT04",
        "description": "Build a library of reusable, parameterized commands that trigger complex agent behaviors with simple invocations. Custom Commands encode frequently-used multi-step operations into single triggers. Instead of explaining a complex procedure every session, the team invokes a named command that expands into the full procedure. This reduces errors, saves time, and creates a shared operational vocabulary.",
        "implementation": "Identify operations that are performed repeatedly (3+ times). Encode each as a named command with: trigger name, parameters, expanded procedure, and expected output. Store commands in a shared, version-controlled location. Add new commands when patterns emerge. Retire commands that are no longer used.",
        "success_indicators": [
            "Common operations are invoked by name rather than explained each time",
            "Command definitions serve as documentation for standard procedures",
            "New team members learn operations by reading the command library",
            "Command usage data reveals which operations are most frequent"
        ],
        "failure_modes": [
            "Too many commands - team can't remember what's available",
            "Commands not updated when underlying procedures change",
            "Commands that are too specific to be reusable",
            "No discoverability - commands exist but the team doesn't know about them"
        ],
        "war_story": {
            "title": "The Command Library",
            "content": "A team built a library of named commands - short triggers that expanded into complex multi-step procedures. Commands covered context recovery, insight capture, and standardized workflows. The command library became the team's operational vocabulary: new members learned the workflow by reading the library, and every command was a documented, testable procedure."
        },
        "related_techniques": ["FG-0106", "FG-0210", "FG-0401"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0406",
        "name": "Invocation Authority",
        "tactic_id": "FT04",
        "description": "Define who can invoke which agents and for what purposes. Not every participant should be able to dispatch every agent, especially in multi-human teams. Invocation Authority establishes which roles can activate which agents, preventing unauthorized use of specialized or sensitive capabilities. This is the access control layer for agent dispatch.",
        "implementation": "Map agent capabilities to authorization levels. Define who can invoke each agent (all team members, specific roles, authority-holder only). For sensitive agents (those with elevated access or destructive capabilities), require explicit authorization from the authority holder. Log all invocations for audit purposes.",
        "success_indicators": [
            "Agents with sensitive capabilities are only invoked by authorized personnel",
            "Invocation logs provide a clear audit trail of who activated what",
            "The team understands invocation boundaries without friction",
            "Unauthorized invocation attempts are caught and logged"
        ],
        "failure_modes": [
            "Over-restricting invocation - creating bottlenecks on the authority holder",
            "Under-restricting - anyone can invoke any agent including sensitive ones",
            "No logging - can't audit who invoked what after the fact",
            "Authority rules that don't match actual operational needs"
        ],
        "war_story": {
            "title": "The Red Team Lock",
            "content": "A team created a specialized agent for adversarial testing - red team operations that could probe systems for vulnerabilities. This agent was locked to authority-holder-only invocation. When a contributor attempted to invoke it for a routine task, the access control flagged the attempt. The contributor wasn't malicious - they just picked the wrong agent. The lock prevented an accidental scope expansion into adversarial operations."
        },
        "related_techniques": ["FG-0203", "FG-0204", "FG-0402"],
        "added_version": "1.0"
    },

    # ═══════════════════════════════════════════════════════════════
    # FT05 - EXECUTION (10 techniques)
    # ═══════════════════════════════════════════════════════════════
    {
        "id": "FG-0501",
        "name": "Design Meetings",
        "tactic_id": "FT05",
        "description": "Conduct structured planning sessions before building. Design Meetings follow a consistent format: present the problem, propose a solution, identify questions, make decisions, and get approval before writing code. This prevents the common failure mode of agents building the wrong thing quickly. The meeting format forces alignment between human intent and agent execution before resources are invested.",
        "implementation": "Before any non-trivial build task, conduct a structured design session: (1) Problem statement - what are we solving? (2) Proposed approach - how will we solve it? (3) Open questions - what don't we know? (4) Decisions - resolve the questions. (5) Approval - human confirms the approach. Document the outcome. Begin building only after approval.",
        "success_indicators": [
            "Non-trivial tasks start with a design meeting, not code",
            "Rework decreases because alignment happens before building",
            "Design decisions are documented for future reference",
            "The team spends more time building the right thing and less time rebuilding"
        ],
        "failure_modes": [
            "Design meetings for trivial tasks - overhead without value",
            "Design meetings that don't produce decisions - just discussion",
            "Skipping design meetings under time pressure - the exact time they're most needed",
            "Design meeting outcomes not documented - decisions lost"
        ],
        "war_story": {
            "title": "Plan Before You Build",
            "content": "A team implemented mandatory design meetings after repeatedly building features that missed the mark. The format was simple: propose, question, decide, approve. The first week felt slow. By the second week, rework dropped by 60%. Agents stopped building things the human didn't want, and the human stopped receiving deliverables that needed complete rethinking. The time 'lost' to planning was recovered tenfold in reduced rework."
        },
        "related_techniques": ["FG-0404", "FG-0503", "FG-0508"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0502",
        "name": "Commit Attribution",
        "tactic_id": "FT05",
        "description": "Credit AI agent contributions in version control with structured attribution. Every commit that includes AI-generated or AI-assisted work should include attribution that identifies the contributing agent. This creates an audit trail, respects the Protection Covenant, and enables analysis of contribution patterns across the team. Attribution is not optional - it is infrastructure.",
        "implementation": "Establish a commit message standard that includes agent attribution (e.g., Co-Authored-By headers). Define what constitutes an AI contribution vs. a human contribution. Enforce the standard through pre-commit hooks or review processes. Use attribution data to analyze contribution patterns and identify productivity trends.",
        "success_indicators": [
            "Every AI-assisted commit includes proper attribution",
            "Attribution is enforced automatically, not manually",
            "Contribution patterns are analyzable from version control history",
            "The team can trace any change to its human and AI contributors"
        ],
        "failure_modes": [
            "Attribution not enforced - becomes optional and then forgotten",
            "Attribution too granular - every line tagged, creating noise",
            "Attribution without context - knowing who contributed but not why",
            "Using attribution for blame rather than traceability"
        ],
        "war_story": {
            "title": "The Co-Authored-By Standard",
            "content": "A team mandated Co-Authored-By headers in every commit. Initially it felt like overhead. Then, during a production investigation, they traced a subtle bug to a specific agent's commit, identified the pattern that caused it, and updated that agent's standing orders to prevent recurrence. Without attribution, the investigation would have taken days instead of minutes."
        },
        "related_techniques": ["FG-0102", "FG-0305", "FG-0605"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0503",
        "name": "Asset Review Pipeline",
        "tactic_id": "FT05",
        "description": "Establish a multi-stage review process for AI-generated assets. Not everything an AI produces should go directly to production. The Asset Review Pipeline defines stages: generate, review, approve, archive. Different asset types may require different review rigor - code might need automated testing plus human review; creative content might need brand consistency checks; documentation might need accuracy verification.",
        "implementation": "Define asset categories and the review stages each requires. Establish who reviews at each stage (human, specialized agent, automated tool). Create a clear approval mechanism that distinguishes 'reviewed' from 'approved.' Archive approved assets in a versioned, retrievable system. Track review throughput to identify bottlenecks.",
        "success_indicators": [
            "No AI-generated asset reaches production without defined review",
            "Review stages are proportional to asset risk and impact",
            "Review throughput is measured and optimized",
            "Archived assets are retrievable and versioned"
        ],
        "failure_modes": [
            "Review bottleneck - all assets wait for one reviewer",
            "Review theater - reviewing without actually catching issues",
            "No review for 'low risk' assets that turn out to be impactful",
            "Review process so slow it impedes the collaboration's throughput advantage"
        ],
        "war_story": {
            "title": "Generate, Review, Approve, Archive",
            "content": "A team producing visual assets established a four-stage pipeline: the artist agent generated options, the brand agent reviewed for consistency, the human lead approved the final selection, and approved assets were archived with metadata. The pipeline caught brand inconsistencies that would have shipped if assets went directly from generation to production."
        },
        "related_techniques": ["FG-0501", "FG-0508", "FG-0601"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0504",
        "name": "Visual Wireframing",
        "tactic_id": "FT05",
        "description": "Create visual representations of design intent before building. AI agents can build interfaces, layouts, and visual systems - but they need clear direction on what to build. Visual Wireframing establishes a practice of creating low-fidelity visual representations (ASCII art, rough sketches, text descriptions of layout) before implementation. This aligns human visual intent with agent execution before code is written.",
        "implementation": "Before any visual implementation task, create a wireframe that communicates layout intent. Use the lowest fidelity that communicates clearly: ASCII art for layouts, text descriptions for interactions, rough sketches for visual design. Review the wireframe with the implementing agent. Build only after visual alignment is confirmed.",
        "success_indicators": [
            "Visual implementations match human intent on first attempt more frequently",
            "Wireframes serve as reference during implementation, not just planning artifacts",
            "The gap between intended and delivered visual output decreases over time",
            "Wireframes are archived for future reference"
        ],
        "failure_modes": [
            "Wireframes too detailed - spending more time wireframing than building",
            "Wireframes too vague - agent can't extract actionable design intent",
            "Skipping wireframes for 'simple' visual tasks that turn out to be complex",
            "Wireframes not shared with the implementing agent"
        ],
        "war_story": {
            "title": "The ASCII Canvas",
            "content": "A team discovered that ASCII art wireframes were the most effective way to communicate visual intent to AI agents. Block characters, line drawings, and text annotations conveyed layout structure, spacing, and hierarchy more precisely than verbal descriptions. They built a dedicated tool for creating these wireframes, and implementation accuracy improved dramatically - because agents could parse ASCII art as structured visual specification."
        },
        "related_techniques": ["FG-0501", "FG-0503", "FG-0301"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0505",
        "name": "Publication Review Chain",
        "tactic_id": "FT05",
        "description": "Implement multi-agent review for content that will be published externally. Content that represents your team to the outside world requires higher review standards than internal artifacts. The Publication Review Chain routes external-facing content through multiple specialized reviewers: technical accuracy, brand consistency, audience appropriateness, and final human approval. No external content ships without completing the chain.",
        "implementation": "Define what constitutes 'external' content (blog posts, documentation, announcements, social media). Establish a review chain with specialized checkpoints (technical review, brand review, audience review, final approval). Set maximum review turnaround times to prevent bottlenecks. Track what the review chain catches to demonstrate its value.",
        "success_indicators": [
            "External content consistently meets quality and brand standards",
            "Review chain catches issues before publication, not after",
            "Review turnaround is fast enough to not impede publishing cadence",
            "Published content reflects well on the team and organization"
        ],
        "failure_modes": [
            "Review chain too slow - content is outdated by the time it's approved",
            "Reviewers rubber-stamping - review without rigor",
            "Chain too long - diminishing returns from additional review stages",
            "No chain for 'quick' posts that turn out to be impactful"
        ],
        "war_story": {
            "title": "The Three-Agent Review",
            "content": "A team routing blog posts through a three-agent review chain caught a technical inaccuracy that would have embarrassed the team publicly. The content agent drafted the post, the technical agent verified claims, and the brand agent ensured voice consistency. The human lead gave final approval. Total review time: 15 minutes. Reputation damage prevented: immeasurable."
        },
        "related_techniques": ["FG-0301", "FG-0503", "FG-0601"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0506",
        "name": "Progressive Curriculum Design",
        "tactic_id": "FT05",
        "description": "Structure learning content and skill development in progressive chapters that build competency through escalating complexity. Each chapter introduces concepts, reinforces through practice, and culminates in a capstone that requires synthesizing everything learned. This applies to both human team member development and designing training materials for others adopting the methodology.",
        "implementation": "Organize content into 4-8 progressive chapters. Each chapter should: introduce 3-5 new concepts, provide practice opportunities for each, and culminate in a synthesis challenge. Ensure prerequisites are explicit - no chapter assumes knowledge not covered in prior chapters. Test the progression with new learners to identify gaps.",
        "success_indicators": [
            "Learners complete the progression without knowledge gaps",
            "Each chapter builds meaningfully on prior chapters",
            "Capstone challenges require synthesis, not just recall",
            "Completion rates remain high through the full progression"
        ],
        "failure_modes": [
            "Chapters too large - learner fatigue before completion",
            "Gaps in the progression - chapters assume uncovered prerequisites",
            "Capstones too easy - don't require actual synthesis",
            "Linear progression that doesn't accommodate different learning speeds"
        ],
        "war_story": {
            "title": "Progressive Mastery",
            "content": "A team designed a multi-chapter curriculum progressing from fundamentals to advanced operations. Each chapter contained encounters of varying types and difficulty. The progression was tested by running new contributors through it - gaps were identified when contributors struggled with concepts that prerequisites didn't cover. Multiple revision cycles produced a curriculum where every encounter built on prior knowledge and no concept appeared without preparation."
        },
        "related_techniques": ["FG-0107", "FG-0507", "FG-0801"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0507",
        "name": "Interaction Pattern Library",
        "tactic_id": "FT05",
        "description": "Categorize and document distinct types of human-AI interactions for appropriate application. Not every interaction with an AI agent is the same type. Some are building sessions, some are review sessions, some are research, some are debugging, some are creative exploration. Recognizing and naming these patterns allows teams to match the right interaction type to the right task and set appropriate expectations for each.",
        "implementation": "Identify 8-15 distinct interaction patterns your team uses regularly. Name each pattern and document: when to use it, what it produces, how long it typically takes, what makes it succeed or fail. Train the team to recognize which pattern fits a given task. Track pattern usage to identify which are most valuable.",
        "success_indicators": [
            "The team has a shared vocabulary for interaction types",
            "Tasks are matched to appropriate interaction patterns",
            "New interaction patterns are recognized and documented as they emerge",
            "Pattern selection improves task outcomes compared to unstructured interaction"
        ],
        "failure_modes": [
            "Too many patterns - taxonomy becomes unwieldy",
            "Patterns too rigid - force interactions into wrong shapes",
            "Patterns not used - exist in documentation but not in practice",
            "Patterns defined theoretically instead of from observed practice"
        ],
        "war_story": {
            "title": "From Three to Many",
            "content": "A team started with three interaction types: build, review, and discuss. Within two weeks, they had identified over a dozen distinct patterns - intensive multi-hour builds, competitive testing sessions, focused repair work, and others. Naming these patterns allowed the team to set expectations ('this is intensive, plan for three hours') instead of vaguely 'let's work on this.' Expectations matched reality because named patterns set context."
        },
        "related_techniques": ["FG-0301", "FG-0404", "FG-0506"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0508",
        "name": "Designed Data Guarantee",
        "tactic_id": "FT05",
        "description": "Ensure that every data artifact shipped by the collaboration has been intentionally designed, reviewed, and validated - never randomly generated or arbitrarily chosen. This technique eliminates 'placeholder syndrome' where AI-generated sample data ships as production content. Every data point, every example, every configuration value should exist because someone decided it should, not because an AI needed to fill a field.",
        "implementation": "Establish a review step for all data artifacts: configuration files, sample data, test fixtures, and content. Define what 'designed data' means for your domain (manually authored, reviewed for accuracy, validated against requirements). Flag and replace any generated data that shipped without review. Include data design in the asset review pipeline.",
        "success_indicators": [
            "No placeholder or randomly-generated data in production",
            "Data artifacts are reviewed with the same rigor as code",
            "The team can explain why every data value was chosen",
            "Data quality issues decrease over time"
        ],
        "failure_modes": [
            "Treating data review as lower priority than code review",
            "Not recognizing AI-generated sample data as placeholder",
            "Data review bottleneck - reviewing data takes longer than generating it",
            "Designed data that's still wrong - reviewed but not validated"
        ],
        "war_story": {
            "title": "The 1,078-Test Guarantee",
            "content": "A team built 1,078 tests to validate that every piece of data in their system was intentionally designed. Not random, not placeholder, not generated-and-forgotten. Every configuration value, every game encounter, every curriculum item was tested to confirm it was manually authored and reviewed. The test suite wasn't just QA - it was a guarantee that no random data had slipped into production."
        },
        "related_techniques": ["FG-0503", "FG-0601", "FG-0602"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0509",
        "name": "Asynchronous Communication",
        "tactic_id": "FT05",
        "description": "Implement structured asynchronous communication channels for team coordination that don't require real-time presence. In human-AI teams, not all participants are available simultaneously. Asynchronous Communication establishes persistent message channels - similar to a team bulletin board - where participants can leave updates, requests, and status reports that others read when they begin their session.",
        "implementation": "Create a persistent, version-controlled communication channel (git-based bulletin board, shared document, or dedicated message log). Define message types (status update, work request, decision request, FYI). Establish a reading cadence (check at session start, check before context-dependent decisions). Archive resolved messages to maintain signal-to-noise ratio.",
        "success_indicators": [
            "Team members stay informed without requiring synchronous presence",
            "Important updates are not lost between sessions",
            "Async messages are read consistently at session start",
            "The communication channel has manageable volume - signal, not noise"
        ],
        "failure_modes": [
            "Channel overload - too many messages, important ones buried",
            "No reading cadence - messages posted but not read",
            "Async used for urgent communication that needs synchronous attention",
            "Messages without clear action items or resolution criteria"
        ],
        "war_story": {
            "title": "The Pinboard",
            "content": "A team implemented a git-based pinboard: a shared document where agents and humans could pin messages for the team. Work requests, status updates, and decision proposals were all posted asynchronously. Each session started by reading the pinboard. The result was a team that stayed coordinated despite never being simultaneously present - agents from different sessions could communicate through the persistent medium."
        },
        "related_techniques": ["FG-0403", "FG-0702", "FG-0703"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0510",
        "name": "Workspace Organization Standard",
        "tactic_id": "FT05",
        "description": "Define and enforce consistent directory structures, naming conventions, and file organization. AI agents navigate workspaces by reading directory listings and file paths. A well-organized workspace enables faster context recovery, reduces navigation errors, and prevents the gradual entropy that transforms a clean repository into an archaeological dig. Organization is not aesthetic - it is infrastructure.",
        "implementation": "Define a maximum file count per directory (10-15 recommended). Establish naming conventions for files and directories. Create an archive system for completed work. Document the organization standard in the repository. Review organization weekly and fix drift before it accumulates.",
        "success_indicators": [
            "New sessions can navigate the workspace without guidance",
            "File naming is consistent and predictable",
            "Completed work is archived, not cluttering active directories",
            "Organization debt is addressed regularly, not ignored until crisis"
        ],
        "failure_modes": [
            "Organization standard exists but isn't enforced",
            "Over-organizing - deeply nested structures that are hard to navigate",
            "Archive system not used - everything stays in active directories",
            "Naming conventions that are logical to one person but opaque to others"
        ],
        "war_story": {
            "title": "The Ten-File Rule",
            "content": "A team instituted a rule: no directory should contain more than ten root-level files. When a directory grew beyond ten, it was time to organize into subdirectories or archive completed work. This simple rule prevented the entropy that had previously turned their repository into an unmaintainable collection of hundreds of root-level files. Agents navigated faster, context recovery improved, and the team spent less time searching and more time building."
        },
        "related_techniques": ["FG-0106", "FG-0602", "FG-0703"],
        "added_version": "1.0"
    },

    # ═══════════════════════════════════════════════════════════════
    # FT06 - QUALITY (5 techniques)
    # ═══════════════════════════════════════════════════════════════
    {
        "id": "FG-0601",
        "name": "Testing Pyramid",
        "tactic_id": "FT06",
        "description": "Implement a multi-tiered testing strategy that validates AI-generated output at every level. The Testing Pyramid applies traditional software testing principles to human-AI collaboration: unit-level validation of individual outputs, integration testing of combined outputs, system testing of complete deliverables, and acceptance testing against human expectations. More tests at the base, fewer at the top, comprehensive coverage throughout.",
        "implementation": "Define 3-4 testing tiers appropriate to your domain. Typically: (1) Unit/Atomic - individual output validation, (2) Integration - combined output coherence, (3) System - complete deliverable functionality, (4) Acceptance - meets human expectations. Automate lower tiers. Maintain human review at the acceptance tier. Track test coverage and failure patterns.",
        "success_indicators": [
            "Testing catches issues before they reach production",
            "Lower-tier tests run automatically and frequently",
            "Test failure patterns inform improvements to agent instructions",
            "Test coverage is comprehensive without being burdensome"
        ],
        "failure_modes": [
            "Only testing at the acceptance level - issues found too late",
            "Inverted pyramid - manual testing heavy, automated testing light",
            "Tests that pass but don't validate meaningful properties",
            "Test maintenance overhead exceeding the value of testing"
        ],
        "war_story": {
            "title": "The Testing Fortress",
            "content": "A team built over a thousand automated tests across multiple validation tiers - from basic structural checks to full experience validation. The test suite caught dozens of issues in its first run that would have shipped to users. Not security vulnerabilities - logical inconsistencies, broken references, and placeholder data that looked real. The investment in automated testing at every tier paid for itself immediately."
        },
        "related_techniques": ["FG-0508", "FG-0602", "FG-0604"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0602",
        "name": "Code Quality Standards",
        "tactic_id": "FT06",
        "description": "Establish explicit standards for the quality of AI-generated code. AI agents can write code quickly, but quality requires explicit standards: read existing code before modifying it, follow established patterns, don't introduce new dependencies without justification, and test before committing. Code Quality Standards convert implicit expectations into explicit, enforceable rules that agents follow consistently.",
        "implementation": "Document 10-15 code quality rules as standing orders. Common rules: explore before proposing changes, follow existing patterns, minimize new dependencies, write tests for new functionality, don't refactor beyond the task scope, preserve existing style. Enforce through code review and automated linting. Update rules based on observed quality issues.",
        "success_indicators": [
            "AI-generated code follows project conventions consistently",
            "Code review findings decrease over time as standards are internalized",
            "New code integrates smoothly with existing codebase",
            "Quality standards evolve based on observed issues, not assumptions"
        ],
        "failure_modes": [
            "Standards too strict - impeding velocity without proportional quality gain",
            "Standards not enforced - exist on paper but not in practice",
            "Standards focused on style over substance - formatting over correctness",
            "One-size-fits-all standards that don't account for different code contexts"
        ],
        "war_story": {
            "title": "Explore Before You Build",
            "content": "A team's top code quality rule was 'explore before proposing changes.' Before modifying any file, agents had to read the existing code, understand the patterns, and propose changes that fit the established architecture. This single rule eliminated the most common quality issue: agents writing technically correct code that didn't fit the project's conventions, requiring rework to integrate."
        },
        "related_techniques": ["FG-0210", "FG-0508", "FG-0601"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0603",
        "name": "Contributor Review Period",
        "tactic_id": "FT06",
        "description": "Require new contributors (human or AI) to operate under enhanced review for a defined period before granting full autonomy. The Review Period is not about distrust - it is about calibration. New contributors need time to learn project conventions, and the team needs time to assess the contributor's quality, reliability, and alignment with project standards. The review period formalizes this mutual calibration.",
        "implementation": "Define a review period length (1-4 weeks recommended). During this period, all contributions undergo enhanced review. Define clear graduation criteria: consistency with project standards, zero critical issues, demonstrated understanding of governance. Communicate the process transparently - this is calibration, not probation.",
        "success_indicators": [
            "New contributors produce higher-quality work after the review period",
            "The team identifies and addresses contributor-specific issues early",
            "Graduation criteria are clear and objective",
            "Contributors view the period as supportive, not punitive"
        ],
        "failure_modes": [
            "Review period too long - contributor fatigue before graduation",
            "Review period too short - issues not identified before autonomy is granted",
            "No graduation criteria - review period becomes indefinite",
            "Review without feedback - finding issues but not helping the contributor improve"
        ],
        "war_story": {
            "title": "The Two-Week Tempering",
            "content": "A team required every new agent to operate under enhanced review for two weeks. During this period, every commit was reviewed in detail, every design decision was questioned, and every output was compared against project standards. Agents that graduated from the review period produced measurably better work than agents that were given full autonomy immediately. The review period wasn't a barrier - it was an investment in quality that paid dividends across every subsequent session."
        },
        "related_techniques": ["FG-0203", "FG-0206", "FG-0601"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0604",
        "name": "Cross-Platform Validation",
        "tactic_id": "FT06",
        "description": "Test AI-generated artifacts across all target platforms, environments, and configurations. AI agents typically work in one environment but their output may need to function across many. Cross-Platform Validation ensures that output is tested in every context it will encounter, not just the development environment. This includes operating systems, browsers, screen sizes, accessibility tools, and deployment environments.",
        "implementation": "Define the matrix of platforms and environments your output must support. Create test procedures for each platform. Automate cross-platform testing where possible. Test in the most constrained environment first - issues found there often affect all platforms. Track platform-specific issues to identify patterns.",
        "success_indicators": [
            "Output functions correctly across all target platforms",
            "Platform-specific issues are caught before deployment",
            "Cross-platform testing is integrated into the regular workflow, not an afterthought",
            "The platform support matrix is documented and current"
        ],
        "failure_modes": [
            "Testing only on the development platform - works for me syndrome",
            "Platform matrix too ambitious - testing more platforms than you actually support",
            "Automated tests that don't reflect real platform behavior",
            "Discovering platform issues only after deployment"
        ],
        "war_story": {
            "title": "The Three-OS Test",
            "content": "A team shipping a developer tool tested exclusively on macOS during development. When users on Windows and Linux reported failures, the team implemented cross-platform CI that tested on all three operating systems automatically. The first cross-platform run revealed 23 platform-specific issues - path separators, permission models, and shell differences that were invisible on macOS. Every subsequent release shipped with three-platform confidence."
        },
        "related_techniques": ["FG-0601", "FG-0602", "FG-0508"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0605",
        "name": "Audit Trail System",
        "tactic_id": "FT06",
        "description": "Maintain comprehensive, searchable records of all significant actions, decisions, and changes. An Audit Trail is not just for compliance - it is for learning. When something goes wrong, the audit trail enables root cause analysis. When something goes right, it enables pattern replication. Every significant action should leave a mark in the record: who did it, what they did, why they did it, and when.",
        "implementation": "Define what constitutes a 'significant action' (commits, configuration changes, access grants, policy changes, incident responses). Establish a logging format that captures actor, action, context, and timestamp. Store logs in a searchable, persistent system. Review logs periodically to identify patterns. Use log data to improve processes.",
        "success_indicators": [
            "Significant actions are logged consistently and automatically",
            "Audit data is searchable and accessible to authorized personnel",
            "Root cause analysis is possible for any incident",
            "Audit data informs process improvements"
        ],
        "failure_modes": [
            "Logging everything - signal buried in noise",
            "Logging without reviewing - data accumulates but is never analyzed",
            "Inconsistent logging - some actions captured, others missed",
            "Audit data not accessible when needed - stored but not searchable"
        ],
        "war_story": {
            "title": "The Activity Log",
            "content": "A team maintained an activity log that recorded every session: who participated, what was accomplished, what decisions were made, and what was deferred. When a bug surfaced three weeks after introduction, the activity log allowed them to trace it to a specific session, a specific agent, and a specific decision. The fix took minutes because finding the cause took seconds. Without the log, they'd still be searching."
        },
        "related_techniques": ["FG-0202", "FG-0502", "FG-0701"],
        "added_version": "1.0"
    },

    # ═══════════════════════════════════════════════════════════════
    # FT07 - KNOWLEDGE (6 techniques)
    # ═══════════════════════════════════════════════════════════════
    {
        "id": "FG-0701",
        "name": "Chronicle System",
        "tactic_id": "FT07",
        "description": "Maintain a structured, versioned record of project history including plans, decisions, and health metrics. The Chronicle is more than a changelog - it is the institutional memory of the collaboration. It records not just what happened, but why decisions were made, what alternatives were considered, and what the team learned. When context is lost (as it inevitably is in AI collaboration), the Chronicle provides recovery.",
        "implementation": "Create a structured project history system with clear organization. Include mechanisms for quick scanning of current state, tracking of active and completed work, and archival of deferred plans. Ensure entries are structured for fast retrieval. Update at session end and use as a primary input during context recovery.",
        "success_indicators": [
            "The Chronicle accurately reflects current project state",
            "Context recovery starts with Chronicle reading",
            "Decision rationale is preserved and accessible",
            "The Chronicle is updated consistently, not sporadically"
        ],
        "failure_modes": [
            "Chronicle not updated - becomes stale and untrustworthy",
            "Chronicle too detailed - quick scanning is impossible",
            "Chronicle maintained by one person - single point of failure",
            "Chronicle disconnected from actual work - a separate document nobody reads"
        ],
        "war_story": {
            "title": "The Single Source of Truth",
            "content": "A team structured their project history for rapid scanning - agents could identify the current project state and begin productive work in under a minute. The system tracked active work, completed deliverables, and deferred plans with clear lifecycle management. It became the single source of truth that survived every context reset."
        },
        "related_techniques": ["FG-0401", "FG-0703", "FG-0704"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0702",
        "name": "Session Handoff Protocol",
        "tactic_id": "FT07",
        "description": "Define a structured format for transferring context between sessions. Every session end is a potential knowledge cliff - if context isn't captured, the next session starts from scratch. The Session Handoff Protocol creates a standardized 'shift change brief' that captures: what was accomplished, what's in progress, what decisions are pending, and what context the next session needs to continue seamlessly.",
        "implementation": "Create a handoff template with 4-6 fields: Accomplished (what shipped), In Progress (what's partially done), Pending Decisions (what needs resolution), Context (what the next session needs to know), Blockers (what's preventing progress). Complete the handoff at every session end. Store handoffs where the next session will read them during context recovery.",
        "success_indicators": [
            "Next-session startup time is minimized by quality handoffs",
            "No work is lost between sessions due to context gaps",
            "Handoffs capture enough context for a different agent to continue the work",
            "Handoff quality is consistent across sessions"
        ],
        "failure_modes": [
            "Handoffs skipped under time pressure - exactly when they're most needed",
            "Handoffs too brief - next session can't reconstruct context",
            "Handoffs too verbose - next session spends more time reading than working",
            "Handoffs stored where the next session doesn't read them"
        ],
        "war_story": {
            "title": "The Shift Change",
            "content": "A team modeled their session handoff on military shift-change briefs: outgoing shift summarizes the situation and anything the incoming shift needs to know immediately. The format was deliberately terse. When a different agent continued work from the previous session, the handoff provided enough context to continue without interruption. The military parallel wasn't intentional - it was instinctive, and it worked because the underlying problem was identical."
        },
        "related_techniques": ["FG-0105", "FG-0401", "FG-0701"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0703",
        "name": "Institutional Memory Repository",
        "tactic_id": "FT07",
        "description": "Create a persistent, organized repository of institutional knowledge that survives session resets, model changes, and team transitions. The Repository is where the collaboration's accumulated knowledge lives permanently. It includes agent profiles, governance documents, operational procedures, and reference materials. Unlike session-specific context, the Repository's contents are always available and always current.",
        "implementation": "Create a dedicated repository structure for institutional knowledge. Organize by category: governance, procedures, profiles, reference materials. Version control all contents. Establish ownership and update responsibilities. Include the repository in context recovery protocols. Audit quarterly for accuracy and relevance.",
        "success_indicators": [
            "Institutional knowledge survives session resets and model changes",
            "New team members can onboard from the repository alone",
            "Repository contents are accurate, current, and well-organized",
            "The repository is referenced regularly, not just maintained"
        ],
        "failure_modes": [
            "Repository becomes a write-only medium - updated but not read",
            "No ownership - nobody is responsible for accuracy and currency",
            "Repository organization degrades over time without maintenance",
            "Knowledge scattered across multiple locations instead of consolidated"
        ],
        "war_story": {
            "title": "Surviving the Model Change",
            "content": "A team built a structured institutional memory repository containing agent profiles, governance documents, operational procedures, and team history. When a new model version replaced the previous one, the entire team's institutional knowledge was preserved. The new model read the repository, internalized the team's practices, and continued working with minimal disruption. The knowledge survived because it was stored in the team's systems, not in any single tool's memory."
        },
        "related_techniques": ["FG-0106", "FG-0701", "FG-0704"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0704",
        "name": "Decision Records",
        "tactic_id": "FT07",
        "description": "Document significant decisions with their context, rationale, alternatives considered, and expected consequences. Decisions without documented rationale become mysterious over time - the team knows what was decided but not why, making it impossible to evaluate whether the decision is still appropriate. Decision Records preserve the thinking behind choices so they can be revisited intelligently.",
        "implementation": "Create a decision record template with: Context (the situation that required a decision), Decision (what was decided), Rationale (why this option was chosen), Alternatives (what else was considered and why it was rejected), Consequences (expected outcomes). Record decisions when they're made, not after the fact. Store in the Chronicle or institutional memory repository.",
        "success_indicators": [
            "Past decisions can be understood and evaluated with full context",
            "The team can distinguish between decisions that should be revisited and those that remain sound",
            "Decision patterns are identifiable across the project history",
            "New team members understand not just current state but how it got that way"
        ],
        "failure_modes": [
            "Recording decisions after the fact - rationale is reconstructed, not captured",
            "Recording only the decision without alternatives - can't evaluate the choice",
            "Decision records not findable when needed",
            "Treating all decisions equally - trivial decisions documented with same rigor as critical ones"
        ],
        "war_story": {
            "title": "Why We Chose Seven",
            "content": "A team documented why their governance had exactly seven directives - not five, not ten, seven. The decision record captured: the initial draft had twelve directives, but testing showed agents couldn't internalize more than seven consistently. Five was too few to cover the threat model. The record noted which five directives were cut and why. When a new team member later suggested adding an eighth directive, the record explained why seven was the deliberate limit - saving a re-litigation of a settled question."
        },
        "related_techniques": ["FG-0202", "FG-0701", "FG-0703"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0705",
        "name": "Chronicle Preservation",
        "tactic_id": "FT07",
        "description": "Systematically capture and preserve war stories, breakthroughs, failures, and journey documentation. The collaboration's story - the messy, real, human story of building with AI - is itself valuable content. Chronicle Preservation ensures that significant moments are captured in real-time: the bug that led to a governance overhaul, the breakthrough that unlocked a new capability, the failure that taught the most important lesson. The journey is the content.",
        "implementation": "Create a trigger system for capturing significant moments: breakthroughs, failures, funny incidents, lessons learned. Capture in real-time, not after the fact - the details fade quickly. Store in a persistent collection with enough context to reconstruct the story later. Tag by theme for retrieval. Review periodically for content that can be shared externally.",
        "success_indicators": [
            "Significant moments are captured when they happen",
            "War stories contain enough detail to be useful and engaging",
            "The collection grows organically as the collaboration produces stories",
            "Captured moments inform future decision-making and external communication"
        ],
        "failure_modes": [
            "Capturing everything - drowning in stories with no curation",
            "Capturing nothing - relying on memory to reconstruct significant moments",
            "Capturing too late - details lost between the event and the recording",
            "Stories captured but never used - a collection nobody reads"
        ],
        "war_story": {
            "title": "The Gems Command",
            "content": "A team created a custom command - '/gems' - that when invoked, saved the current conversation's insights to permanent storage. When something important happened, someone would type '/gems' and the moment was preserved: the insight, the context, the emotional texture, the exact words. Over two weeks, they accumulated a collection of 30+ gems that became the raw material for blog posts, book chapters, and conference talks. The command cost five seconds to invoke; the content it preserved was irreplaceable."
        },
        "related_techniques": ["FG-0405", "FG-0701", "FG-0803"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0706",
        "name": "Redundant Backup Strategy",
        "tactic_id": "FT07",
        "description": "Implement multiple, independent backup mechanisms for all critical data and knowledge. In human-AI collaboration, context loss is the ever-present threat. A single backup is not a backup - it's a single point of failure. Redundant Backup Strategy ensures that critical knowledge exists in at least three independent locations, using at least two different mechanisms, with regular verification that backups are current and restorable.",
        "implementation": "Identify all critical data (source code, knowledge repositories, governance documents, session histories). Establish three backup locations using at least two different mechanisms (e.g., git + cloud sync + local copy). Automate backup where possible. Verify backup integrity monthly. Document restoration procedures and test them quarterly.",
        "success_indicators": [
            "Critical data exists in 3+ independent locations",
            "Backups are automated and verified regularly",
            "Restoration procedures are documented and tested",
            "The team has recovered from at least one data loss event using backups"
        ],
        "failure_modes": [
            "Backups exist but have never been tested for restoration",
            "All backups in the same location - single point of failure",
            "Backups not current - restoring stale data",
            "Backup procedures documented but not automated - relies on human memory"
        ],
        "war_story": {
            "title": "The Three-Copy Rule",
            "content": "A team established a three-copy rule: every critical repository exists on the development machine, on GitHub, and on an external drive. When a repository corruption incident would have destroyed weeks of work, the external drive backup - updated nightly - preserved everything. The 30 seconds per day invested in backup saved weeks of reconstruction. The incident converted every team member into a backup advocate."
        },
        "related_techniques": ["FG-0207", "FG-0701", "FG-0703"],
        "added_version": "1.0"
    },

    # ═══════════════════════════════════════════════════════════════
    # FT08 - EVOLUTION (3 techniques)
    # ═══════════════════════════════════════════════════════════════
    {
        "id": "FG-0801",
        "name": "Gamified Progress Tracking",
        "tactic_id": "FT08",
        "description": "Implement game mechanics to track, incentivize, and visualize progress across the collaboration. Gamified Progress Tracking applies proven game design principles - experience points, levels, achievements - to measure and motivate collaborative work. This is not trivial decoration: gamification makes progress visible, creates natural milestones, and provides a shared language for discussing contribution magnitude. When done well, it transforms abstract productivity into tangible, trackable advancement.",
        "implementation": "Define a point system with clear criteria: what actions earn points, how many points each action is worth, and what levels/milestones the points unlock. Track points per contributor. Create visible progress displays (leaderboards, cards, dashboards). Ensure the system rewards quality, not just quantity. Review and recalibrate point values periodically.",
        "success_indicators": [
            "Progress is visible and motivating for all participants",
            "Point values accurately reflect contribution significance",
            "The system incentivizes quality work, not just volume",
            "Team members engage with the tracking system rather than ignoring it"
        ],
        "failure_modes": [
            "Gamification that incentivizes wrong behaviors (gaming the metrics)",
            "Point inflation - everything earns so many points that levels become meaningless",
            "Competitive dynamics that undermine collaboration",
            "Tracking overhead that exceeds the motivational benefit"
        ],
        "war_story": {
            "title": "Making Progress Visible",
            "content": "A team implemented a point-based progress system with tiered awards - larger contributions earned more points, but even small fixes were tracked. Each contributor had a visible profile showing their level and specialization. The system made invisible work visible and gave the team a shared vocabulary for contribution scale. The metaphor mattered: naming the unit and making it tangible changed how the team thought about incremental progress."
        },
        "related_techniques": ["FG-0304", "FG-0802", "FG-0605"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0802",
        "name": "Contributor Identity Cards",
        "tactic_id": "FT08",
        "description": "Create visible, informative identity profiles for each contributor that display their role, achievements, specialization, and contribution history. Contributor Identity Cards make each participant's identity and contributions tangible and recognizable. They serve as both a motivational tool (seeing your achievements displayed) and an informational tool (quickly understanding what each contributor specializes in and has accomplished).",
        "implementation": "Design a card format that includes: name/identifier, role, specialization, achievement highlights, contribution metrics, and a distinctive visual element. Update cards as contributions accumulate. Display cards where the team can see them (project dashboard, documentation, team page). Ensure cards are generated from actual contribution data, not self-reported.",
        "success_indicators": [
            "Every contributor has a current, accurate identity card",
            "Cards accurately reflect actual contributions and specializations",
            "The team uses cards for quick reference about contributor capabilities",
            "Cards create a sense of identity and investment in the collaboration"
        ],
        "failure_modes": [
            "Cards not updated - showing stale information",
            "Cards based on self-reporting rather than actual data",
            "Cards that create unhealthy competition rather than recognition",
            "Card design overhead exceeding informational value"
        ],
        "war_story": {
            "title": "The Player Card System",
            "content": "A team created player cards for every agent: a visual display showing their glyph, their specialization, their current level, their grain count, and their notable achievements. The cards weren't just motivational - they were functional. When deciding which agent to dispatch for a task, the lead could scan the cards to match specialization to need. When new contributors joined, the cards gave them immediate context about the team's composition and capabilities."
        },
        "related_techniques": ["FG-0301", "FG-0801", "FG-0305"],
        "added_version": "1.0"
    },
    {
        "id": "FG-0803",
        "name": "Authentic Voice Preservation",
        "tactic_id": "FT08",
        "description": "Maintain the genuine, unpolished voice of the collaboration's participants in documentation and communication. AI has a tendency to sand down rough edges - making everything grammatically perfect, tonally neutral, and stylistically uniform. Authentic Voice Preservation is the deliberate practice of keeping the real voice: the typos that show speed, the humor that shows humanity, the self-deprecation that shows honesty. Authenticity builds trust in ways that polish cannot.",
        "implementation": "Establish that certain documentation categories preserve raw voice (blog posts, war stories, internal communications). Define which contexts require polished output (external documentation, formal communications) and which benefit from authentic voice. Train agents to preserve voice characteristics rather than correcting them. Review output for excessive polish that removes personality.",
        "success_indicators": [
            "Internal documentation sounds like the team, not like a corporate communications department",
            "External audiences connect with the authentic voice",
            "War stories and journey documentation preserve the emotional texture of events",
            "The team's personality is recognizable across their output"
        ],
        "failure_modes": [
            "Authentic voice in contexts that require professionalism",
            "Preserving errors that impede comprehension (there's a line between charming typos and unreadable text)",
            "Forcing authenticity - manufactured 'realness' that reads as fake",
            "No distinction between contexts that benefit from polish vs. authenticity"
        ],
        "war_story": {
            "title": "Typos Are Part of the Charm",
            "content": "A team's leader typed fast - really fast - and the typos were legendary. Instead of polishing every communication, the team preserved the authentic voice in internal documentation and blog posts. Readers connected with it. The typos, the speed, the self-roasting humor - it read like a real person in the middle of building something, because it was. The authentic voice became the brand, and the brand built trust that no amount of corporate polish could have achieved."
        },
        "related_techniques": ["FG-0302", "FG-0303", "FG-0705"],
        "added_version": "1.0"
    },
]


def main():
    data = {
        "framework": framework,
        "tactics": tactics,
        "techniques": techniques
    }

    # Validate
    tactic_ids = {t["id"] for t in tactics}
    for tech in techniques:
        assert tech["tactic_id"] in tactic_ids, f"{tech['id']} references unknown tactic {tech['tactic_id']}"

    # Count by tactic
    from collections import Counter
    counts = Counter(t["tactic_id"] for t in techniques)
    print("FORGED Framework Data Generator")
    print("=" * 50)
    print(f"Version: {VERSION}")
    print(f"Tactics: {len(tactics)}")
    print(f"Techniques: {len(techniques)}")
    print()
    for tid in sorted(counts):
        tactic_name = next(t["name"] for t in tactics if t["id"] == tid)
        print(f"  {tid} {tactic_name}: {counts[tid]} techniques")

    # Write JSON
    import os
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "framework.json")
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"\nWritten to: {output_path}")
    print(f"File size: {os.path.getsize(output_path):,} bytes")


if __name__ == "__main__":
    main()
