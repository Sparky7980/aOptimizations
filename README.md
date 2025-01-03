#  aOps

This script optimizes your Windows system to boost FPS in games like Fortnite by disabling unnecessary background processes, clearing DNS cache, and performing various system optimizations. The script also allows you to manage settings such as terminating Chrome processes, disabling Windows Defender, and clearing temporary files.

## Download
aOps/download.vercel.app
## Features:
- Terminate Chrome Processes
- Disable Visual Effects
- Change DNS settings
- Clear DNS Cache
- Modify Hosts File
- Disable Telemetry
- Disable Windows Defender
- Clean Temporary Files
- Launch Windows Update
- Backup Files

## Installation/Build Yourself Guide (Ignore If You Want Exe File By Itself


### Prerequisites

To run this project, you need the following:

1. **Python 3.3+**: If you don't have Python installed, download and install it from the official [Python website](https://www.python.org/downloads/).
2. **Pygame**: A Python library for creating games and graphical applications.
3. **PyInstaller**: A tool to bundle Python scripts into stand-alone executables.

### Step 1: Clone the Repository

First, clone the repository to your local machine. Open a terminal (PowerShell or Command Prompt) and run:

```bash
git clone https://github.com/yourusername/FPSbooster.git
cd FPSbooster
```

### Step 2: Install Dependencies
Install the required Python libraries (pygame and pyinstaller) by running the following commands in PowerShell or Command Prompt:

```bash
pip install pygame pyinstaller
```

### Step 3: Convert the Script to an Executable
Once the dependencies are installed, you can convert the Python script (main.py) into a stand-alone executable using PyInstaller. Run the following command in PowerShell or Command Prompt:

```bash
pyinstaller --onefile main.py
```
This will create a single executable file in the dist/ folder within the project directory. The executable is Windows-specific, so ensure you're building it for the correct OS.

### Step 4: Running the Script
To run the script with administrator privileges (required for some optimizations like changing DNS and disabling Windows Defender), follow these steps:

Right-click on FPSbooster.exe (located in the dist/ folder).
Select "Run as administrator".

### Step 5: Using the Script
Once the script is running, change the settings in the settings page to your preference then press start.

## Contributing
To contribute sumbit a pull request explaining what each thing does and make sure it works.


 
