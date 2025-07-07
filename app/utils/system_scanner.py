import os
import json
from pathlib import Path

DB_PATH = Path("app/db/tools_db.json")

def is_executable(file_path):
    """Check if a file is an executable."""
    return os.path.isfile(file_path) and os.access(file_path, os.X_OK)

def scan_directories_for_tools(directories):
    """Scan specified directories for executable tools."""
    tools = {}
    for directory in directories:
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    if is_executable(file_path):
                        if file not in tools:
                            tools[file] = file_path
    return tools

def get_system_path_directories():
    """Retrieve directories from the system PATH environment variable."""
    return os.environ.get("PATH", "").split(os.pathsep)

def save_tools_to_db(tools):
    """Save collected tools to the JSON database."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DB_PATH, "w") as f:
        json.dump(tools, f, indent=4)
    print(f"[SigurAI] Tools DB saved to {DB_PATH.resolve()}")

def main(scan_extra=True):
    directories_to_scan = get_system_path_directories()
    if scan_extra:
        directories_to_scan.extend([
            "C:\\Program Files",
            "C:\\Program Files (x86)",
            "/usr/bin",
            "/usr/local/bin",
            "/opt"
        ])

    tools = scan_directories_for_tools(directories_to_scan)

    print(f"[SigurAI] Collected {len(tools)} tools.")
    save_tools_to_db(tools)

if __name__ == "__main__":
    main()
