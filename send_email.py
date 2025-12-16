import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from config import EMAIL_USER, EMAIL_PASSWORD, GM_EMAIL

def send_report(file_path):
    msg = MIMEMultipart()
    msg["Subject"] = "Monthly Sales Report"
    msg["From"] = EMAIL_USER
    msg["To"] = GM_EMAIL

    msg.attach(MIMEText("Dear GM,\n\nFind attached the compiled monthly sales report.\n\nRegards,\nAutomation Bot"))

    with open(file_path, "rb") as f:
        attachment = MIMEApplication(f.read(), _subtype="xlsx")
        attachment.add_header("Content-Disposition", "attachment", filename=file_path)
        msg.attach(attachment)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)

    print("Report sent successfully to GM.")
