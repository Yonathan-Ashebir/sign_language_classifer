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

# Launch Jupyter notebook with main.ipynb
python -m jupyter notebook main.ipynb
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

def create_windows_environment():
    env_name = "sign_language_env"
    batch_script = """@echo off
call conda activate %s
if errorlevel 1 (
    echo Failed to activate conda environment
    exit /b 1
)

pip install poetry
if errorlevel 1 (
    echo Failed to install poetry
    exit /b 1
)

poetry install --no-root
if errorlevel 1 (
    echo Failed to install dependencies
    exit /b 1
)

python -m jupyter notebook main.ipynb
""" % env_name

    # Write the batch script to a file
    script_path = "run_windows.bat"
    with open(script_path, 'w') as f:
        f.write(batch_script)

    # Check if conda is available
    try:
        subprocess.run(["conda", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Conda not found. Please install Anaconda or Miniconda first.")
        sys.exit(1)

    # Check if environment exists, create if not
    try:
        subprocess.run(["conda", "list", "-n", env_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Using existing conda environment '{env_name}'")
    except subprocess.CalledProcessError:
        print(f"Creating conda environment '{env_name}'...")
        subprocess.run(["conda", "create", "-n", env_name, "python", "-y"], check=True)

    # Execute the batch script
    print("Running installation and notebook...")
    subprocess.run([script_path], shell=True)

def main():
    print(f"Detected system: {platform.system()}")
    
    if platform.system() == "Linux":
        create_linux_environment()
    elif platform.system() == "Windows":
        create_windows_environment()
    else:
        print(f"Unsupported operating system: {platform.system()}")
        sys.exit(1)

if __name__ == "__main__":
    main()