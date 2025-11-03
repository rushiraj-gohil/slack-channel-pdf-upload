# 🚀 Assignment: *Sending a Document to a Slack Channel via Slack APIs*

This repository contains the solution for the assignment **“Sending a Document to a Slack Channel via Slack APIs.”**  
The objective is to **research, understand, and implement Slack’s APIs** to upload a specified document *(a resume in PDF format)* to a designated Slack channel.

---

## ✨ Key Technical Details

### 🔧 API Implementation

- Utilizes the official [Slack Python SDK (`slack-sdk`)](https://pypi.org/project/slack-sdk/) for robust and streamlined API interaction.

### 📡 API Methods

- `conversations_join` &rarr; Ensures the bot is present in the target channel.
- `files_upload_v2` &rarr; Uploads and shares the file in a *single, atomic operation* (modern and recommended method).

### ⚙️ Robustness

- Implements detailed **logging** and structured **error handling** using `SlackApiError` for clean output and efficient debugging.

### 🔐 Authentication

- Script is structured to securely handle and use the provided **Slack API Token**.

---

## 🛠️ Local Setup & Execution

Follow these steps to run the solution locally:

### ✅ Prerequisites

- **Python 3.x**
- **Slack API Token**
- **PDF Document:** `Rushiraj_Gohil_Resume_1810.pdf` placed in the project’s root directory

### 1️⃣ Clone the Repository

```bash
git clone <repository_url>
cd slack-file-upload-assignment
```

### 2️⃣ Install Dependencies

Install required Python packages (the key dependency is the official Slack SDK):

```bash
pip install -r requirements.txt
```

### 3️⃣ Configuration

Edit the configuration section in `slack_upload.py` and replace the placeholder with your Slack token:

```python
# ====== CONFIGURATION ======
SLACK_TOKEN = "<SLACK TOKEN HERE>"  # <-- REPLACE THIS
CHANNEL_ID = "<CHANNEL ID HERE>" # <-- REPLACE THIS
# ...
```

### 4️⃣ Run the Script

Execute the main Python script:

```bash
python slack_upload.py
```

Upon successful execution, you’ll see **confirmation logs** and a **success message** in your console.

---

## 💡 Self-Correction & Robustness

To guarantee *100% functionality* and preemptively catch issues before using official credentials, an **isolated testing workflow** was followed:

### 🧪 1. Isolated Test Environment

- Created a **personal 30-day Slack trial workspace**
- Set up a **dedicated Slack Bot App** for controlled testing

### 🔑 2. Permission Validation

- Verified and configured all necessary **OAuth scopes** and **bot permissions**

### 🧰 3. Debugging & End-to-End Testing

- Thoroughly ran, debugged, and validated the entire script using a **test token and channel**
- Confirmed full functionality before connecting to the official workspace.
