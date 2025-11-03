🚀 Assignment: Sending a Document to a Slack Channel via Slack APIs

This repository contains the solution for the assignment “Sending a Document to a Slack Channel via Slack APIs.”
The goal was to research, understand, and implement Slack’s APIs to upload a specified document (a resume in PDF format) to a designated Slack channel.

✨ Key Technical Details
🔧 API Implementation

Uses the official Slack Python SDK (slack-sdk)
 for a robust and simplified API interaction.

📡 API Methods

conversations_join: Ensures the bot joins the target channel before uploading.

files_upload_v2: Performs file upload and sharing as a single atomic operation (modern and recommended approach).

⚙️ Robustness

Integrated logging and error handling (SlackApiError) for clean output and effective debugging.

🔐 Authentication

The script securely uses the provided Slack API Token.

🛠️ Local Setup and Execution

Follow these steps to run the solution locally:

✅ Prerequisites

Python 3.x

Slack API Token (provided via email for this assignment)

Resume PDF named Rushiraj_Gohil_Resume_1810.pdf placed in the project root directory

1. Clone the Repository
git clone <repository_url>
cd slack-file-upload-assignment

2. Install Dependencies

Install the required Python packages (core dependency: Slack SDK):

pip install -r requirements.txt

3. Configuration

Open slack_upload.py and replace the placeholder with your assigned Slack token:

# ====== CONFIGURATION ======
SLACK_TOKEN = "<SLACK TOKEN HERE>"  # <-- REPLACE THIS
CHANNEL_ID = "C093LUWB19B"
# ...

4. Execution

Run the main script:

python slack_upload.py


If successful, you’ll see confirmation logs and a success message in the console.

💡 Self-Correction & Robustness (Powerful Move)

To ensure 100% functionality and avoid any issues before using official credentials, an isolated testing workflow was implemented:

🧪 Isolated Test Environment

Created a personal 30-day Slack trial workspace

Set up a dedicated Slack Bot App for experimentation

🔑 Permission Validation

Verified and configured all required OAuth scopes and permissions for the bot app

🧰 Debugging & Testing

Fully tested and debugged the script using a separate test token and channel

Validated end-to-end functionality prior to submission
