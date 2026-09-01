#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-$(pwd)}"
PROJECT_NAME="${2:-$(basename "$TARGET_DIR")}"

echo "=========================================="
echo "Initializing Solo OMA Setup for: $PROJECT_NAME"
echo "Target Directory: $TARGET_DIR"
echo "=========================================="

mkdir -p "$TARGET_DIR/.serena"
if [ ! -f "$TARGET_DIR/.serena/config.json" ]; then
  cat <<EOF > "$TARGET_DIR/.serena/config.json"
{
  "name": "$PROJECT_NAME",
  "languages": ["typescript", "javascript", "python", "json"]
}
EOF
  echo "✓ Created .serena/config.json"
fi

echo ""
echo "Full 14-Agent OMA Roster ready to spawn in Solo (agent_tool_id=12):"
echo "  1. OMA Director    (Lead orchestrator & user interface)"
echo "  2. OMA Product     (Scope, constraints & acceptance criteria)"
echo "  3. OMA Interview   (Socratic requirement clarification)"
echo "  4. OMA Architect   (Architecture decisions & boundaries)"
echo "  5. OMA Consultant  (Decision criteria & strategic framing)"
echo "  6. OMA Consensus   (Technical option evaluation & convergence)"
echo "  7. OMA Planner     (Phased roadmap & dependency mapping)"
echo "  8. OMA Researcher  (Documentation lookup & API discovery)"
echo "  9. OMA Executor    (Feature implementation & builds)"
echo " 10. OMA Debugger    (Root-cause analysis & diagnostics)"
echo " 11. OMA Quick       (Rapid small edits & formatting)"
echo " 12. OMA Reviewer    (Code review & security audit)"
echo " 13. OMA Editor      (Deliverable synthesis & reporting)"
echo " 14. OMA Verifier    (Acceptance verification & release gate)"
echo ""
echo "Next Steps in Solo:"
echo "1. Register project: solo/create_project(path=\"$TARGET_DIR\", name=\"$PROJECT_NAME\")"
echo "2. Spawn OMA Director: solo/spawn_agent(agent_tool_id=12, name=\"OMA Director\")"
echo "   (OMA Director will spawn other specialist agents on-demand, or you can pre-spawn the full team)"
echo ""
echo "Done!"
