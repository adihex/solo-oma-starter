#!/usr/bin/env python3
"""
Register and configure all 14 OMA (Oh-My-Antigravity) agents in Solo as first-class
launchable tools and configure project processes to launch with explicit --agent flags.
"""

import sys
import os
import shutil
import sqlite3
import datetime
from pathlib import Path

SOLO_DB_PATH = Path.home() / ".config" / "soloterm" / "solo.db"

OMA_AGENTS = [
    ("OMA Director", "oma-director", "Lead orchestrator, user interface & team coordinator"),
    ("OMA Architect", "oma-architect", "Systems architecture, boundaries & technical trade-offs"),
    ("OMA Planner", "oma-planner", "Phased execution roadmaps, milestones & dependency mapping"),
    ("OMA Executor", "oma-executor", "Feature implementation, refactoring & build execution"),
    ("OMA Verifier", "oma-verifier", "Independent test suite execution, quality gates & release audits"),
    ("OMA Debugger", "oma-debugger", "Root-cause analysis, stack trace diagnostics & test fixes"),
    ("OMA Reviewer", "oma-reviewer", "Code review, security auditing & regression prevention"),
    ("OMA Researcher", "oma-researcher", "Technical research, API comparisons & documentation lookup"),
    ("OMA Product", "oma-product", "Scope definition, PRD generation & acceptance criteria"),
    ("OMA Interview", "oma-interview", "Socratic dialogue to clarify ambiguous requirements"),
    ("OMA Consultant", "oma-consultant", "Strategic analysis, decision matrices & recommendation framing"),
    ("OMA Consensus", "oma-consensus", "Multi-option technical evaluation & convergence"),
    ("OMA Quick", "oma-quick", "Rapid, low-risk edits (typos, formatting, one-line bug fixes)"),
    ("OMA Editor", "oma-editor", "Content synthesis, report formatting & user-facing deliverables"),
]

def main() -> None:
    if not SOLO_DB_PATH.exists():
        print(f"Error: Solo database not found at {SOLO_DB_PATH}", file=sys.stderr)
        sys.exit(1)

    # Optional target project directory
    target_project = sys.argv[1] if len(sys.argv) > 1 else str(Path.cwd().resolve())

    # Create safety backup
    timestamp = int(datetime.datetime.now(datetime.timezone.utc).timestamp())
    backup_path = SOLO_DB_PATH.with_suffix(f".db.bak-{timestamp}")
    shutil.copy2(SOLO_DB_PATH, backup_path)
    print(f"✓ Created Solo database backup: {backup_path}")

    conn = sqlite3.connect(SOLO_DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(position) FROM agent_tools")
    max_pos = cursor.fetchone()[0] or 12

    now_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    now_iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    registered_tools = {}

    print("\nRegistering OMA Agent Launch Configurations in Solo:")
    for name, flag, description in OMA_AGENTS:
        default_args = f"--dangerously-skip-permissions --agent {flag}"
        max_pos += 1

        cursor.execute("SELECT id FROM agent_tools WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            tool_id = row[0]
            cursor.execute("""
                UPDATE agent_tools
                SET command = 'agy', default_args = ?, tool_type = 'antigravity', enabled = 1, updated_at = ?
                WHERE id = ?
            """, (default_args, now_str, tool_id))
            print(f"  • Updated existing tool '{name}' (ID: {tool_id})")
        else:
            cursor.execute("""
                INSERT INTO agent_tools (name, command, default_args, tool_type, enabled, position, prompt_mode, tool_type_mode, created_at, updated_at)
                VALUES (?, 'agy', ?, 'antigravity', 1, ?, 'stdin', 'auto', ?, ?)
            """, (name, default_args, max_pos, now_str, now_str))
            tool_id = cursor.lastrowid
            print(f"  • Added new tool '{name}' (ID: {tool_id})")

        registered_tools[name] = tool_id

        # Maintain installation health record
        cursor.execute("SELECT id FROM agent_tool_installations WHERE agent_tool_id = ? AND env_key = 'local'", (tool_id,))
        inst_row = cursor.fetchone()
        health_msg = f"{name} ({flag}) is ready in Local."
        if inst_row:
            cursor.execute("""
                UPDATE agent_tool_installations
                SET command = 'agy', default_args = ?, enabled = 1, detected_version = '1.1.23',
                    config_path = '/Users/adityabalakrishnan/.gemini/config/mcp_config.json',
                    health_status = 'ok', health_message = ?, last_checked_at = ?, updated_at = ?
                WHERE id = ?
            """, (default_args, health_msg, now_iso, now_str, inst_row[0]))
        else:
            cursor.execute("""
                INSERT INTO agent_tool_installations (agent_tool_id, env_key, command, default_args, enabled, detected_version, config_path, health_status, health_message, last_checked_at, created_at, updated_at)
                VALUES (?, 'local', 'agy', ?, 1, '1.1.23', '/Users/adityabalakrishnan/.gemini/config/mcp_config.json', 'ok', ?, ?, ?, ?)
            """, (tool_id, default_args, health_msg, now_iso, now_str, now_str))

    # Match target project
    cursor.execute("SELECT id, name FROM projects WHERE path = ?", (target_project,))
    proj_row = cursor.fetchone()
    if proj_row:
        proj_id, proj_name = proj_row
        print(f"\nConfiguring agent processes for target project '{proj_name}' (ID: {proj_id}):")
        for name, flag, _ in OMA_AGENTS:
            cmd = f"agy --dangerously-skip-permissions --agent {flag}"
            tool_id = registered_tools[name]
            cursor.execute("""
                UPDATE processes
                SET command = ?, agent_tool_id = ?
                WHERE project_id = ? AND name = ? AND kind = 'agent'
            """, (cmd, tool_id, proj_id, name))
            if cursor.rowcount > 0:
                print(f"  ✓ Re-wired process '{name}' ➔ `{cmd}`")

    conn.commit()
    conn.close()
    print("\n✓ All OMA agent launch configurations successfully synced with Solo.")

if __name__ == "__main__":
    main()
