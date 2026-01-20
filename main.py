import os
import sys

# Ensure the 'src' directory is in sys.path for direct execution
src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from google_trends_mcp.server import mcp

if __name__ == "__main__":
    mcp.run()
