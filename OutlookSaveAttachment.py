import os
import win32com.client

# Function to save attachments
def save_attachments(mail, subject):
    # Check if the subject matches
    if mail.Subject == subject:
        # Iterate through attachments
        for attachment in mail.Attachments:
            # Save attachment to current directory
            attachment.SaveAsFile(os.path.join(os.getcwd(), attachment.FileName))

# Initialize Outlook application
outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")

# Select the inbox folder
inbox = namespace.GetDefaultFolder(6)  # 6 refers to the inbox folder

# Iterate through emails in the inbox
for mail in inbox.Items:
    # Save attachments if the email has attachments
    if mail.Attachments:
        save_attachments(mail, "Your Subject Here")

print("Attachments downloaded successfully.")