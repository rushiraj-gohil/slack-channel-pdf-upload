🚀 Assignment: Sending a Document to a Slack Channel via Slack APIs
This repository contains the solution for the assignment: "Sending a Document to a Slack Channel via Slack APIs". The objective was to research, understand, and implement Slack's APIs to upload a specified document (a resume in PDF format) to a designated Slack channel.

✨ Key Technical Details
API Implementation: Utilizes the official Slack Python SDK (slack-sdk) for a robust and simplified API interaction.

API Methods: Implements the conversations_join method (to ensure the bot is present) and the modern files_upload_v2 method for uploading and sharing the file in a single, atomic operation.

Robustness: Includes logging and error handling (SlackApiError) for clean output and effective debugging.

Authentication: The script is structured to securely use the provided Slack Token.

🛠️ Local Setup and Execution
To run the solution locally, follow these steps.

Prerequisites
Python 3.x

Slack API Token: The token provided via email for this assignment.

Document: Your resume in PDF format, saved as Rushiraj_Gohil_Resume_1810.pdf in the root directory.

1. Clone the Repository
Bash

git clone <repository_url>
cd slack-file-upload-assignment
2. Install Dependencies
Install the required Python packages using pip. Note that the core dependency is the official Slack SDK.

Bash

pip install -r requirements.txt
3. Configuration
You must replace the placeholder in slack_upload.py with your assigned token:

Python

# ====== CONFIGURATION ======
SLACK_TOKEN = "<SLACK TOKEN HERE>" # <-- REPLACE THIS
CHANNEL_ID = "C093LUWB19B"
# ...
4. Execution
Run the main Python script:

Bash

python slack_upload.py
Upon successful execution, the script will output confirmation logs and the success message.

💡 Self-Correction & Robustness (Powerful Move)
To ensure 100% functionality and preemptively identify any script-related issues before using the official credentials, a critical step was taken:

Isolated Test Environment: I created a personal 30-day Slack trial workspace and set up a dedicated Slack Bot App.

Permission Validation: I thoroughly configured and tested all required scopes (permissions) for the Bot App within my test environment.

Debugging & Testing: The entire script was run, debugged, and validated end-to-end using a separate test token and channel.
