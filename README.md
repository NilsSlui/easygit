# A Tiny Menubar Application for Git Synchronization

![Demo of App](https://github.com/NilsSlui/easygit/blob/main/demo.gif?raw=true)

## Overview

This application was created the bring the "Sync Changes 🔄" functionality from Visual Studio Code to the Menu Bar so that it can be used while working in other code editors or enviroments. 

## Features

- **Select Folder:** Allows users to choose a git repository folder via a graphical dialog. The application will remember the selected folder for future actions.
- **Auto-Verify Git Repository:** Automatically checks the git status of the selected folder every few seconds to provide real-time feedback on the repository's state.
- **Sync Changes:** Offers a quick way to fetch, pull, add, commit (with a custom message), and push changes to the remote repository. This process is initiated through a simple click and confirms the action with minimal user input.

## How It Works

1. **Selecting a Folder:** Upon clicking the "Select Folder" menu item, a dialog prompts the user to select their git folder. This path is then stored and displayed in the menu bar along with the current git branch name, if available.

2. **Verifying Git Repository Status:** The application periodically checks the git status of the selected repository to identify any changes. It updates the "Sync Changes" menu item to reflect the current state, such as "No changes detected" or indicating the number of changes to be synchronized.

3. **Synchronizing Changes:** When the user decides to sync changes, they are prompted to enter a commit message. The application then executes a series of git commands to fetch updates from the remote, pull any changes, stage all modifications, commit them with the provided message, and finally push the changes to the remote repository.

## Installation and Usage

Ensure you have Git installed and accessible via your terminal. Clone this repository and run the following commands to install the required dependencies and start the application using 'python main.py'.

## Dependencies

- **macOS:** Since this tool utilizes AppleScript for dialogues and folder selection, it is currently only compatible with macOS.
- **Git:** A working Git installation is required for the application to manage repositories.
- **Python 3:** The application is written in Python 3.11 and requires it to be installed on your system.
- **Rumps Library:** this tool uses the Rumps library to create the menubar application. Install it using 'pip install rumps'.

## Disclaimer

EasyGit is designed to provide a convenient interface for basic git operations. It is not intended to replace comprehensive git tools or GUI applications. Please use it within its capabilities and ensure you have backups of your repositories if necessary.
