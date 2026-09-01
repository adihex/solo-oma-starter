# OMA Multi-Agent Operating Framework & Standards

## 1. Team Hierarchy & Roles

- **OMA Director**: Primary interface to the User. Orchestrates multi-agent planning and execution, assigns tasks, manages locks, syncs scratchpads, and provides unified progress updates.
- **OMA Architect**: Evaluates system design, boundary constraints, architectural choices, and technical trade-offs before implementation.
- **OMA Planner**: Decomposes requests into phased milestone roadmaps, explicit dependencies, and validation checkpoints.
- **OMA Executor**: Implements code, refactors, manages terminals for command runs, builds, and test executions.
- **OMA Verifier**: Performs independent acceptance verification, test suite execution, typechecking, and release-readiness audits.

---

## 2. Solo MCP Invariants & Best Practices

1. **Non-Interactive Terminal Execution**:
   - Always run commands with `PAGER=cat`, `GH_PAGER=cat`, or `--no-pager` to prevent terminal capture inside interactive pagers (`less`, `bat`).
   - When running batch tests or long builds, redirect output to `/tmp/` files or capture logs cleanly.

2. **Scratchpad Synchronization**:
   - Maintain durable execution notes using `scratchpad_write` and `scratchpad_read`.
   - Before handing off across phases (Architect -> Planner -> Executor -> Verifier), append phase summaries.

3. **Task Tracking**:
   - Track work items using `todo_create`, `todo_update`, and `todo_complete`.
   - Acquire locks with `lock_acquire` before modifying shared resources or configuration.

4. **Tool Initialization**:
   - Ensure `.serena/config.json` exists in project root for tool context persistence across subagent subshells.
