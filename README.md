# CurseForge Manifest Downloader

## Overview

This Python script is designed to fetch download URLs for mods listed in a CurseForge manifest file (`manifest.json`). It utilizes the CurseForge API to retrieve the download URLs for each mod file listed in the manifest.

## Requirements

- Python 3.x
- `requests` library (can be installed via pip: `pip install requests`)

## Usage

1. Clone or download this repository to your local machine.
2. Place your `manifest.json` file in the same directory as the script.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script using the following command: `python3 main.py`
5. The script will begin processing the mod files listed in the `manifest.json` file.
6. Once the process is completed, the script will output "Done." in the terminal.
7. The download URLs for the mods will be saved in the `mod_links.txt` file.
8. Any errors encountered during the process will be logged in the `error_log.txt` file.

## Note

- Ensure that your `manifest.json` file is correctly formatted and contains the necessary information for each mod file (e.g., `projectID`, `fileID`).
- Make sure you have a valid CurseForge API key (`x-api-key`) to authenticate your requests. You can obtain one by signing up on the CurseForge website.
- If you encounter any issues or errors, please refer to the `error_log.txt` file for more information.
