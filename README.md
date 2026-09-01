# Solo + OMA Multi-Agent Project Starter

This template provides a declarative setup for managing projects in **Solo** with the full 14-role **OMA (Oh-My-Antigravity)** agent team and automated Turborepo/monorepo command processes.

---

## The Full 14-Agent OMA Roster

| Agent Role | Specialty |
|---|---|
| **OMA Director** | Lead orchestrator, user interface, and team coordinator |
| **OMA Product** | Scope definition, PRDs, constraints, and acceptance criteria |
| **OMA Interview** | Socratic dialogue to clarify ambiguous user requirements |
| **OMA Architect** | Systems architecture, boundaries, and trade-off analysis |
| **OMA Consultant** | Strategic analysis, decision matrices, and recommendation framing |
| **OMA Consensus** | Comparing technical approaches and converging on solutions |
| **OMA Planner** | Phased execution roadmaps, milestone planning, and dependencies |
| **OMA Researcher** | Tech research, API comparisons, and documentation lookup |
| **OMA Executor** | Feature implementation, refactoring, and build/terminal execution |
| **OMA Debugger** | Root-cause analysis, stack traces, and flaky test fixes |
| **OMA Quick** | Fast, low-risk edits (typos, formatting, one-line fixes) |
| **OMA Reviewer** | Code review, security auditing, and regression prevention |
| **OMA Editor** | Content synthesis, report formatting, and deliverables |
| **OMA Verifier** | Independent test suite execution, quality gates, and release readiness |

---

## What's Included in this Template

- `solo.yml`: Declarative background commands (`Dev Server`, `Build`, `Test`, `Typecheck`, `Lint`) with non-interactive `PAGER=cat` defaults and file change triggers (`restart_when_changed`).
- `AGENTS.md`: Full 14-agent role catalog, operating boundaries, and Solo MCP tool invariants.
- `.serena/config.json`: Pre-configured workspace definitions to ensure code intelligence works seamlessly across subshells.
- `package.json` & `turbo.json`: Monorepo script baseline.
- `scripts/bootstrap-solo.sh`: Helper initialization script.

---

## How to Use for a New Project

### Step 1: Copy Template into Your New Project
```bash
cp -R ~/Documents/solo-oma-starter/* /path/to/your-new-project/
cp -R ~/Documents/solo-oma-starter/.serena /path/to/your-new-project/
```

### Step 2: Register in Solo
In Solo (or via your agent session):
```json
solo/create_project(
  path: "/path/to/your-new-project",
  name: "Your Project Name"
)
```
Solo will automatically parse `solo.yml` and register all background commands.

### Step 3: Spawn OMA Director
From Solo UI or via Solo MCP:
```json
solo/spawn_agent(
  agent_tool_id: 12,
  name: "OMA Director"
)
```

### Step 4: Interact Directly with OMA Director
Send your prompts and feature requests to **OMA Director**. The Director coordinates with the full roster of specialist agents (Architect, Product, Planner, Executor, Debugger, Reviewer, Verifier, etc.) to deliver tasks end-to-end.
