import re
import smtplib
import os
from email.mime.text import MIMEText    
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(recipient_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")  
        

def analyze_logs(file_path,keywords):
    pattern = re.compile(r'|'.join(keywords))
    
    try:
        with open(file_path, 'r') as file:
        for line in file:
           match = pattern.search(line)
                if match:
                    match.group()
                    print(f"Keyword '{match.group()}' found in line: {line.strip()}")
    except FileNotFoundError:
        print(f"Log file '{file_path}' not found.")
        
analyze_logs("/var/log/syslog", ["ERROR", "WARNING","CRITICAL"])

if __name__ == "__main__":
        recipient_email = "vaibhavkamble6496@gmail.com"
        subject = "Log Analysis:Critical Errors Detected on ip-172-31-6-144"   
        body = "The log analysis has detected critical errors in the system logs."
        send_email(recipient_email, subject, body)