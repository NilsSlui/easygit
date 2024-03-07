# EasyGit - A Simple Menubar Application for Git Management

## Overview

EasyGit is a lightweight menubar application designed to streamline the git management process directly from your macOS menu bar. This application facilitates the selection of a git repository folder, the verification of git status, and the synchronization of changes with the remote repository, all through an intuitive graphical interface. It leverages macOS's native AppleScript and Git commands to perform these actions efficiently.

## Features

- **Select Folder:** Allows users to choose a git repository folder via a graphical dialog. The application will remember the selected folder for future actions.
- **Auto-Verify Git Repository:** Automatically checks the git status of the selected folder every few seconds to provide real-time feedback on the repository's state.
- **Sync Changes:** Offers a quick way to fetch, pull, add, commit (with a custom message), and push changes to the remote repository. This process is initiated through a simple click and confirms the action with minimal user input.

## How It Works

1. **Selecting a Folder:** Upon clicking the "Select Folder" menu item, a dialog prompts the user to select their git folder. This path is then stored and displayed in the menu bar along with the current git branch name, if available.

2. **Verifying Git Repository Status:** The application periodically checks the git status of the selected repository to identify any changes. It updates the "Sync Changes" menu item to reflect the current state, such as "No changes detected" or indicating the number of changes to be synchronized.

3. **Synchronizing Changes:** When the user decides to sync changes, they are prompted to enter a commit message. The application then executes a series of git commands to fetch updates from the remote, pull any changes, stage all modifications, commit them with the provided message, and finally push the changes to the remote repository.

## Installation and Usage

To use EasyGit, ensure you have Git installed and accessible via your terminal. Download the script and run it on your macOS device. The application icon will appear in your menu bar, offering quick access to its features.

## Dependencies

- **macOS:** Since EasyGit utilizes AppleScript for dialogues and folder selection, it is currently only compatible with macOS.
- **Git:** A working Git installation is required for the application to manage repositories.

## Disclaimer

EasyGit is designed to provide a convenient interface for basic git operations. It is not intended to replace comprehensive git tools or GUI applications. Please use it within its capabilities and ensure you have backups of your repositories if necessary.
