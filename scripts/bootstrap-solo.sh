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
echo "Next Steps to provision in Solo:"
echo "1. Register project via Solo MCP (or open folder in Solo UI):"
echo "   solo/create_project(path=\"$TARGET_DIR\", name=\"$PROJECT_NAME\")"
echo "2. Spawn OMA Agent Team (using agent_tool_id=12 for Antigravity-yolo):"
echo "   - spawn_agent(agent_tool_id=12, name=\"OMA Director\")"
echo "   - spawn_agent(agent_tool_id=12, name=\"OMA Architect\")"
echo "   - spawn_agent(agent_tool_id=12, name=\"OMA Planner\")"
echo "   - spawn_agent(agent_tool_id=12, name=\"OMA Executor\")"
echo "   - spawn_agent(agent_tool_id=12, name=\"OMA Verifier\")"
echo ""
echo "Done!"
