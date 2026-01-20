import argparse
import json
import os
import sys
import shutil
from pathlib import Path
from typing import Optional

def get_gemini_settings_path(custom_path: Optional[str] = None) -> Path:
    """Get the path to the Gemini settings.json file."""
    if custom_path:
        return Path(custom_path).expanduser().resolve()
    
    # Assuming standard location; can be improved with OS detection if needed
    home = Path.home()
    return home / ".gemini" / "settings.json"

def install_server(custom_path: Optional[str] = None):
    """Register the MCP server in Gemini's settings.json."""
    settings_path = get_gemini_settings_path(custom_path)
    
    if not settings_path.exists():
        print(f"Error: Gemini settings file not found at {settings_path}")
        print("Please ensure Gemini is installed and has been run at least once.")
        sys.exit(1)

    try:
        with open(settings_path, 'r', encoding='utf-8') as f:
            settings = json.load(f)
    except Exception as e:
        print(f"Error reading settings.json: {e}")
        sys.exit(1)

    # Backup settings
    backup_path = settings_path.with_suffix('.json.backup')
    try:
        shutil.copy2(settings_path, backup_path)
        print(f"Backed up settings to {backup_path}")
    except Exception as e:
        print(f"Warning: Could not backup settings: {e}")

    # Ensure mcpServers exists
    if "mcpServers" not in settings:
        settings["mcpServers"] = {}

    # Define the server configuration
    # We use sys.executable to ensure we use the same python interpreter
    # that runs this CLI, which should be the one where the package is installed.
    # Define the server configuration
    # Use sys.executable to ensure we use the explicit python interpreter path
    # This solves issues with 'python' vs 'python3' and PATH visibility
    server_entry = {
        "command": sys.executable,
        "args": ["-m", "google_trends_mcp.cli", "run"],
        "env": {} 
    }

    settings["mcpServers"]["google-trends-mcp"] = server_entry

    try:
        with open(settings_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2)
        print("Successfully registered 'google-trends-mcp' in Gemini settings.")
        print("Please restart Gemini to load the new tool.")
    except Exception as e:
        print(f"Error writing settings.json: {e}")
        sys.exit(1)

def run_server():
    """Run the FastMCP server."""
    # Import here to avoid import errors during installation if dependencies aren't ready
    from google_trends_mcp.server import mcp
    mcp.run()

def main():
    parser = argparse.ArgumentParser(description="Google Trends MCP Server CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Install command
    parser_install = subparsers.add_parser("install", help="Register server in Gemini")
    parser_install.add_argument("--path", help="Custom path to settings.json")

    # Run command
    parser_run = subparsers.add_parser("run", help="Run the MCP server")

    args = parser.parse_args()

    if args.command == "install":
        install_server(args.path)
    elif args.command == "run":
        run_server()

if __name__ == "__main__":
    main()
