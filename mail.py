import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import time

from local.credentials import sender_adress, sender_password, recipient_adress

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # For starttls
SENDER_EMAIL = sender_adress
SENDER_PASSWORD = sender_password
RECIPIENT_EMAIL = recipient_adress

message = '''\
Subject: Hi there

This message is sent from Python.'''

def send_email(subject, body):
    try:
        # Connect to SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        # Compose email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send email
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        print('Email notification sent successfully!')

        # Close connection
        server.quit()
    except Exception as e:
        print('Error sending email notification:', e)


def main():
    while True:
        print("You will be notified on your E-mail daily by 9:00 AM")
        # Check if current time is 9:00 AM
        if datetime.datetime.now().hour == 21 and datetime.datetime.now().minute == 7:
            subject = 'Daily Notification'
            body = 'This is your daily notification. Have a great day!'
            send_email(subject, body)

        # Wait for 1 minute before checking again
        time.sleep(60)

if __name__ == '__main__':
    main()