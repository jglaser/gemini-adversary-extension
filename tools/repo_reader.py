import os
import sys
import logging

# Setup debug logging
logging.basicConfig(filename="/tmp/gemini_mcp_debug.log", level=logging.DEBUG)

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    # Fallback for dump mode if MCP isn't installed
    FastMCP = None

# Configuration
IGNORE_DIRS = {".git", ".venv", "__pycache__", ".ruff_cache", ".pytest_cache", "build", "dist", "node_modules"}
IGNORE_EXTS = {".pyc", ".o", ".so", ".dll", ".class", ".exe", ".bin"}

def scan_repo(root_dir: str) -> str:
    """Internal logic to scan the repo."""
    output = []
    abs_root = os.path.abspath(root_dir)
    output.append(f"<repository_context root='{abs_root}'>")
    
    for dirpath, dirnames, filenames in os.walk(abs_root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        
        for f in filenames:
            if any(f.endswith(ext) for ext in IGNORE_EXTS):
                continue
                
            path = os.path.join(dirpath, f)
            rel_path = os.path.relpath(path, abs_root)
            
            try:
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                    output.append(f"<file path='{rel_path}'>\n{content}\n</file>")
            except (UnicodeDecodeError, PermissionError):
                output.append(f"<file path='{rel_path}' status='skipped_binary_or_protected' />")
                
    output.append("</repository_context>")
    return "\n".join(output)

# --- MCP SERVER SETUP ---
if FastMCP:
    mcp = FastMCP("AdversaryRepoReader")

    @mcp.tool()
    def read_repository(path: str = ".") -> str:
        """
        Reads the entire repository source code.
        
        Args:
            path: The relative path to the root of the repository (default: ".")
        """
        logging.info(f"Tool 'read_repository' called with path={path}")
        return scan_repo(path)

# --- ENTRY POINT ---
if __name__ == "__main__":
    # MODE 1: CLI DUMP (Bypass MCP)
    if "--dump" in sys.argv:
        print(scan_repo("."))
        sys.exit(0)

    # MODE 2: MCP SERVER
    if FastMCP:
        logging.info("Starting FastMCP Server...")
        mcp.run()
    else:
        print("Error: 'mcp' library not found. Install it via pip.", file=sys.stderr)
        sys.exit(1)
