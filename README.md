# Solo + OMA Multi-Agent Project Starter

This template provides a declarative setup for managing projects in **Solo** with the full 14-role **OMA (Oh-My-Antigravity)** agent team and automated Turborepo/monorepo command processes.

---

## Attributions & Official Sources

This starter integrates two core agentic frameworks:

### 1. Solo (Solo Terminal)
- **Website & Documentation**: [https://soloterm.com](https://soloterm.com)
- **Official Docs**: [https://soloterm.com/docs](https://soloterm.com/docs)
- **Agent-Readable Docs API**: [https://soloterm.com/api/v1/docs](https://soloterm.com/api/v1/docs)
- **`solo.yml` Specification**: [https://soloterm.com/docs/projects/solo-yml](https://soloterm.com/docs/projects/solo-yml)
- **Agent Orchestration & Spawning**: [https://soloterm.com/docs/workflows/agents-spawning-agents](https://soloterm.com/docs/workflows/agents-spawning-agents)
- **MCP Tools Overview**: [https://soloterm.com/docs/mcp-tools/overview](https://soloterm.com/docs/mcp-tools/overview)

### 2. Oh-My-Antigravity (OMA)
- **Repository**: [https://github.com/Joonghyun-Lee-Frieren/oh-my-antigravity](https://github.com/Joonghyun-Lee-Frieren/oh-my-antigravity)
- **Framework**: Oh-My-Antigravity (`oh-my-antigravity`), the specialized multi-agent operating system and subagent suite designed for the Antigravity CLI (`agy`) ecosystem.
- **Roster & Archetypes**: Designed around specialized cognitive roles (Director, Product, Interview, Architect, Consultant, Consensus, Planner, Researcher, Executor, Debugger, Quick, Reviewer, Editor, Verifier) communicating via structured state, scratchpads, and quality-gated handoffs.

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
- `scripts/register-solo-agents.py`: Automatically syncs all 14 OMA agent tools and project launch configurations into Solo's local database.
- `scripts/bootstrap-solo.sh`: Automated setup and initialization script.

---

## Configuration & Environment Setup

### 1. Disable "AI: Out of credits" warnings (Antigravity Config)
If `agy` displays `AI: Out of credits` warnings during execution, ensure `useAiCredits` is set to `false` in your global configuration:
```json
// ~/.gemini/config/config.json
{
  "userSettings": {
    "useAiCredits": false
  }
}
```

---

## How to Use for a New Project

### Step 1: Copy Template into Your New Project
```bash
cp -R ~/Documents/solo-oma-starter/* /path/to/your-new-project/
cp -R ~/Documents/solo-oma-starter/.serena /path/to/your-new-project/
```

### Step 2: Register in Solo & Provision OMA Launch Tools
Run the bootstrap script inside your project directory:
```bash
./scripts/bootstrap-solo.sh
```
This will:
1. Initialize `.serena/config.json`.
2. Register all 14 OMA agents in Solo's tool picker with their explicit `--agent oma-...` flags.
3. Automatically re-wire project agent processes.

### Step 3: Launch OMA Director
In Solo, select **OMA Director** directly from the agent launch dropdown, or call via Solo MCP:
```json
solo/spawn_agent(
  agent_tool_id: 18,
  name: "OMA Director"
)
```

### Step 4: Interact Directly with OMA Director
Send your prompts and feature requests to **OMA Director**. The Director coordinates with the full roster of specialist agents (Architect, Product, Planner, Executor, Debugger, Reviewer, Verifier, etc.) to deliver tasks end-to-end.
