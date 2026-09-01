# Solo + OMA Multi-Agent Project Starter

This template provides a declarative setup for managing projects in **Solo** with a 5-role **OMA (Oh-My-Antigravity)** agent team and automated Turborepo/monorepo commands.

---

## What's Included

- `solo.yml`: Declarative background commands (`Dev Server`, `Build`, `Test`, `Typecheck`, `Lint`) with non-interactive `PAGER=cat` defaults and file change triggers (`restart_when_changed`).
- `AGENTS.md`: Operating boundaries, role descriptions, and Solo MCP invariants for all team agents.
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

### Step 3: Spawn the OMA Agent Team
From your orchestrating agent or Solo MCP client:
1. `spawn_agent(agent_tool_id: 12, name: "OMA Director")` (Your main entry point)
2. `spawn_agent(agent_tool_id: 12, name: "OMA Architect")`
3. `spawn_agent(agent_tool_id: 12, name: "OMA Planner")`
4. `spawn_agent(agent_tool_id: 12, name: "OMA Executor")`
5. `spawn_agent(agent_tool_id: 12, name: "OMA Verifier")`

### Step 4: Interact Directly with OMA Director
Send your prompts and feature requests to **OMA Director**. The Director coordinates with the Architect, Planner, Executor, and Verifier to deliver tasks end-to-end.
