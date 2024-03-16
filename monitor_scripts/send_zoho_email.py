from utils.email_utils import send_email
from dotenv import load_dotenv
import os

load_dotenv(".env")

sender_email = os.getenv("SENDER_EMAIL")
zoho_password = os.getenv("ZOHO_APP_PASSWORD")
mail_group_email = os.getenv("MAIL_GROUP_EMAIL")

def send_zoho_email(subject, body):
    smtp_server = "smtp.zoho.com"
    smtp_port = 587
    send_email(sender_email, zoho_password, mail_group_email, subject, body, smtp_server, smtp_port)
