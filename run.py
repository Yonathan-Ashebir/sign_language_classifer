import os
import sys
import subprocess
import platform
from pathlib import Path

def create_linux_environment():
    # Create shell script that will be executed
    script_content = """#!/bin/bash
# Activate the virtual environment
source .venv/bin/activate

# Install poetry if not present
if ! command -v poetry &> /dev/null; then
    pip install poetry
fi

# Install dependencies
poetry install --no-root

# Launch Jupyter notebook
python -m jupyter notebook main.py
"""

    # Write the script to a file
    script_path = "run_linux.sh"
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    # Make the script executable
    os.chmod(script_path, 0o755)
    
    # Create .venv if it doesn't exist
    if not Path(".venv").exists():
        print("Creating Python virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
    
    # Execute the script
    print("Running installation and notebook...")
    subprocess.run(["./" + script_path], check=True)

def main():
    if platform.system() == "Linux":
        create_linux_environment()
    else:
        print("This script is only for Linux systems.")
        sys.exit(1)

if __name__ == "__main__":
    main()