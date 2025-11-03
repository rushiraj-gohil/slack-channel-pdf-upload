### 🚀 Assignment: Sending a Document to a Slack Channel via Slack APIs

This repository contains the solution for the assignment: **"Sending a Document to a Slack Channel via Slack APIs"**. The objective was to research, understand, and implement Slack's REST APIs to upload a specified document (in PDF format) to a designated Slack channel.

-----

### ✨ Key Features

  * **API Utilization:** Successful use of the appropriate Slack REST API method for file upload and sharing.
  * **Authentication:** Secure handling of the provided Slack Token for authenticating API requests.
  * **Modularity:** A simple, executable Python script (`slack_upload.py`) for the file upload process.
  * **Comprehensive Documentation:** Detailed technical documentation explaining the approach, API choices, and workflow (`docs/DOCUMENTATION.md`).

-----

### 🛠️ Local Setup and Execution

To run the solution locally, follow these steps.

#### Prerequisites

  * **Python 3.x**
  * **Slack API Token:** The token provided via email for this assignment.
  * **Document:** Your resume in PDF format (e.g., `Rushiraj_Gohil_Resume_1810.pdf`).

#### 1\. Clone the Repository

```bash
git clone <repository_url>
cd slack-file-upload-assignment
```

#### 2\. Install Dependencies

Install the required Python packages (primarily the `requests` library for making HTTP calls) using `pip`:

```bash
pip install -r requirements.txt
```

#### 3\. Execution

The script requires the **Slack Token** and the **Channel ID** to be passed, either as environment variables or by editing the placeholder variables in `slack_upload.py`.

  * **Designated Channel ID:** `C093LUWB19B`
  * **Document Path:** `./Rushiraj_Gohil_Resume_1810.pdf`

The `slack_upload.py` script executes the API call to upload the file to the channel.

-----

### 💡 Self-Correction & Robustness (Powerful Move)

Before running the final code with the interviewer's provided credentials, a **critical step** was taken to ensure the script's reliability and to preemptively debug any permission or formatting issues:

  * **Personal Test Environment:** I set up my own **30-day Slack trial workspace** and created a dedicated **Slack Bot App**.
  * **Permission Configuration:** I carefully configured all necessary permissions (scopes) for the Bot App within my test environment.
  * **End-to-End Testing:** The entire workflow was thoroughly tested and debugged in this isolated environment using a separate test token and channel.
  * **Outcome:** This proactive approach guaranteed the script's functionality, confirmed the necessary API scopes, and ensured that any failure with the official token would be due to an external factor (e.g., token scope) rather than an error in the implementation logic.

-----

### 📂 Repository Structure

```
slack-channel-pdf-upload/
├── README.md                      ← This file.
├── slack_upload.py                ← The core Python script that executes the API call.
├── requirements.txt               ← List of necessary Python dependencies.
├── .gitignore                     ← Standard Git ignore rules.
├── LICENSE                        ← MIT License (as an example of best practice).
├── Rushiraj_Gohil_Resume_1810.pdf ← The document to be uploaded.
├── docs/
│   └── DOCUMENTATION.md           ← Detailed technical write-up (The required deliverable 2).
└── screenshots/ (optional)
    └── slack_message.png          ← Proof of successful upload (Implementation Output).
```
