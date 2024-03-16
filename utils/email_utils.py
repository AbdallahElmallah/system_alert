import smtplib
from email.mime.text import MIMEText
import logging

def send_email(sender_email, app_password, mail_group_email, subject, body, smtp_server, smtp_port):
    try:
        message = MIMEText(body)
        message["From"] = sender_email
        message["To"] = mail_group_email
        message["Subject"] = subject

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, mail_group_email, message.as_string())

        logging.info(f"Email sent successfully via {smtp_server}.")
    except Exception as e:
        logging.error(f"Error sending email: {str(e)}")
