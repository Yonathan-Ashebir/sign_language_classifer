import os
import sys
import subprocess
import platform
from pathlib import Path

def create_linux_environment():
    # Create .venv if it doesn't exist
    if not Path(".venv").exists():
        print("Creating Python virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
    
    # Determine the correct pip and python paths
    venv_pip = os.path.join(".venv", "bin", "pip")
    venv_python = os.path.join(".venv", "bin", "python")
    
    # Install poetry in the virtual environment
    print("Installing poetry...")
    subprocess.run([venv_pip, "install", "poetry"], check=True)
    
    # Run poetry install --no-root
    print("Running poetry install...")
    subprocess.run([venv_python, "-m", "poetry", "install", "--no-root"], check=True)
    
    # Launch Jupyter notebook
    print("Starting Jupyter notebook...")
    subprocess.run([venv_python, "-m", "jupyter", "notebook", "main.ipynb"], check=True)

def create_windows_environment():
    env_name = "my_env"
    
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
    
    # Activate environment and install packages
    print("Installing poetry and dependencies...")
    commands = [
        f"conda activate {env_name}",
        "pip install poetry",
        "poetry install --no-root",
        "python -m jupyter notebook main.ipynb"
    ]
    
    # On Windows, we need to run these commands in a shell
    subprocess.run(["cmd", "/c", " & ".join(commands)], check=True)

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