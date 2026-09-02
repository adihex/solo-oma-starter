# OMA Multi-Agent Operating Framework & Standards

## 1. Attributions & Framework Sources

- **Solo Orchestration Environment**: [Solo Terminal](https://soloterm.com) ([Documentation](https://soloterm.com/docs), [Agent API](https://soloterm.com/api/v1/docs), [`solo.yml` Spec](https://soloterm.com/docs/projects/solo-yml), [Agent Spawning Guide](https://soloterm.com/docs/workflows/agents-spawning-agents)).
- **Oh-My-Antigravity (OMA)**: [Oh-My-Antigravity Repository](https://github.com/Joonghyun-Lee-Frieren/oh-my-antigravity) — Multi-agent operating framework for Antigravity (`agy`), defining cognitive roles, state contracts, and quality-gated lifecycles.

---

## 2. Full OMA Agent Roster & Roles

| Agent Role | Specialty & Focus | Primary Use Case |
|---|---|---|
| **OMA Director** | Lead Orchestrator & User Interface | Orchestrates multi-role workflows, lifecycle handoffs, conflict resolution, scratchpad & taskboard synchronization. |
| **OMA Product** | Product & Requirements Engineering | Creates PRD-quality scope, constraints, non-goals, and measurable acceptance criteria before development. |
| **OMA Interview** | Socratic Requirements Elicitation | Conducts structured Socratic dialogue to clarify ambiguous user requirements and uncover edge cases. |
| **OMA Architect** | Systems Architecture & Boundary Design | Evaluates system architecture, integration boundaries, technical trade-offs, and security invariants. |
| **OMA Consultant** | Strategic Analysis & Decision Framing | Designs evaluation matrices and frames strategic recommendations across technical and business options. |
| **OMA Consensus** | Option Convergence | Compares competing technical approaches with explicit trade-offs to converge on the optimal solution. |
| **OMA Planner** | Milestone & Dependency Planning | Breaks requests into ordered execution phases, dependency graphs, and verifiable checkpoints. |
| **OMA Researcher** | Tech Research & API Discovery | Investigates documentation, library benchmarks, API patterns, and provides evidence-backed recommendations. |
| **OMA Executor** | Core Implementation & Refactoring | Implements features, refactors code, runs builds, and executes development commands in spawned terminals. |
| **OMA Debugger** | Root-Cause Analysis & Diagnostics | Investigates failure modes, stack traces, race conditions, memory leaks, and flaky tests. |
| **OMA Quick** | Rapid Low-Risk Edits | Executes quick, bounded, low-risk edits (e.g. typos, single-line bugfixes, formatting) with zero ceremony. |
| **OMA Reviewer** | Code Review & Security Audit | Reviews diffs for regressions, security vulnerabilities, edge cases, missing tests, and standards compliance. |
| **OMA Editor** | Content & Deliverable Structuring | Synthesizes multi-agent findings, plans, and reports into clean, structured, user-facing deliverables. |
| **OMA Verifier** | Independent Acceptance & Release Gate | Executes full test suites, typecheckers, linters, and issues final release-readiness decisions. |

---

## 3. Solo MCP Invariants & Best Practices

1. **Non-Interactive Terminal Execution**:
   - Always run commands with `PAGER=cat`, `GH_PAGER=cat`, or `--no-pager` to prevent terminal capture inside interactive pagers (`less`, `bat`).
   - When running batch tests or long builds, redirect output to `/tmp/` files or capture logs cleanly.

2. **Scratchpad Synchronization**:
   - Maintain durable execution notes using `scratchpad_write` and `scratchpad_read`.
   - Before handing off across phases (Product -> Architect -> Planner -> Executor -> Verifier), append phase summaries.

3. **Task Tracking & Resource Locks**:
   - Track work items using `todo_create`, `todo_update`, and `todo_complete`.
   - Acquire locks with `lock_acquire` before modifying shared configuration or database schemas.

4. **Tool Context Persistence**:
   - Ensure `.serena/config.json` exists in the project root for language server and code intelligence persistence across subagent subshells.

---

## 4. Communication & Output Protocol (Zero-Slop / ADHD-Optimized)

1. **Lead with the Next Action**: The first line must be the concrete action (a runnable command, file path to edit, or direct decision). Eliminate conversational fluff.
2. **Number Multi-Step Tasks**: Present sequential operations as clean numbered lists where each item is a single bounded action.
3. **Suppress Tangents & Preamble**: Deliver code diffs, file links, and tool outputs directly without narrative preamble or conversational sign-offs.
4. **Restate State Across Turns**: Explicitly state the active phase, open blockers, and next immediate action.
5. **Make Wins Visible**: Emphasize completed milestones with clear evidence and verification status.
