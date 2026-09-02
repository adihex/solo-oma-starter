#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-$(pwd)}"
PROJECT_NAME="${2:-$(basename "$TARGET_DIR")}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

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

# Step 2: Register all 14 OMA agent launch tools in Solo
if [ -f "$SCRIPT_DIR/register-solo-agents.py" ]; then
  python3 "$SCRIPT_DIR/register-solo-agents.py" "$TARGET_DIR"
fi

echo ""
echo "Antigravity Settings Tip:"
echo "To prevent 'AI: Out of credits' warnings and use standard model quotas,"
echo "ensure 'useAiCredits: false' in ~/.gemini/config/config.json."
echo ""
echo "Done! You can now launch any OMA agent from Solo UI or run:"
echo "  solo/spawn_agent(agent_tool_id=18, name=\"OMA Director\")"
