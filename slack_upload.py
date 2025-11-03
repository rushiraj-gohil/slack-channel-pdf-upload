import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Set up basic logging to output info and errors
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ====== CONFIGURATION ======
SLACK_TOKEN = "<SLACK TOKEN HERE>"
CHANNEL_ID = "<CHANNEL ID HERE>"
PDF_PATH = "Rushiraj_Gohil_Resume_1810.pdf"
MESSAGE_TEXT = "Hey team! This is Rushiraj Gohil, sending his resume via slack_sdk for the assignment for the post of APM - Bengaluru"
# ============================

# Instantiate the Slack WebClient with your token
client = WebClient(token=SLACK_TOKEN)

try:
    # Optional: Ensure the bot is a member of the channel
    logger.info("Step 1️⃣ Joining channel (if not already a member)...")
    join_response = client.conversations_join(channel=CHANNEL_ID)
    logger.info("✅ Joined channel successfully")
except SlackApiError as join_error:
    # If already in the channel, ignore the "already_in_channel" error
    if join_error.response.get("error") == "already_in_channel":
        logger.info("✅ Already a member of the channel")
    else:
        logger.warning("⚠️ Error joining channel: %s", join_error.response.get("error"))

try:
    # Upload the file using files_upload_v2
    logger.info("Step 2️⃣ Uploading file to Slack channel...")
    response = client.files_upload_v2(
        file=PDF_PATH,
        title="Rushiraj Gohil - Resume",
        channel=CHANNEL_ID,
        initial_comment=MESSAGE_TEXT,
    )
    
    logger.info("✅ File uploaded successfully!")
    logger.info("📄 File ID: %s", response.get("file", {}).get("id"))
    logger.info("🔗 Permalink: %s", response.get("file", {}).get("permalink"))
    
    print("\n" + "="*50)
    print("✅ SUCCESS! File and message posted to Slack channel.")
    print("="*50)
    
except SlackApiError as upload_error:
    logger.error("❌ Error uploading file: %s", upload_error.response.get("error"))
    print("\n" + "="*50)
    print("❌ FAILED TO UPLOAD FILE")
    print(f"Error: {upload_error.response.get('error')}")
    print("="*50)
