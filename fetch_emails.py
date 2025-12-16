import imaplib
import email
import os
from config import EMAIL_USER, EMAIL_PASSWORD, IMAP_SERVER, OUTLET_EMAILS

def fetch_reports(download_folder="downloads"):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_USER, EMAIL_PASSWORD)
    mail.select("inbox")

    # Search for mails from the outlet emails
    for outlet in OUTLET_EMAILS:
        status, messages = mail.search(None, f'(FROM "{outlet}")')

        email_ids = messages[0].split()
        for msg_id in email_ids:
            status, msg_data = mail.fetch(msg_id, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])

            # Look for attachments
            for part in msg.walk():
                if part.get_content_disposition() == "attachment":
                    filename = part.get_filename()

                    if filename.endswith(".xlsx"):
                        filepath = os.path.join(download_folder, filename)
                        with open(filepath, "wb") as f:
                            f.write(part.get_payload(decode=True))
                        print(f"Downloaded: {filename}")
    mail.logout()
    return download_folder
