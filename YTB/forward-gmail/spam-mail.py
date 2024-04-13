import smtplib
import time
import random

from email.mime.text import MIMEText
# Ensure to properly secure the email and password handling in a production environment.

sender_email = 'andrewyli@gmail.com'  # Replace with your email
recipients = ['andrewyli@gmail.com']  # Enter recipients here

# Read the email password securely, for example from an environment variable or a secured file.
# Storing plaintext passwords in files or in code is not secure.
with open('password.txt', 'r') as f:  # Assuming the password is stored as plaintext in 'password.txt'
    password = f.read().strip()

def spam_every_minute():
    while True:
        with open('message.txt', 'r', encoding='utf-8') as fp:
            msg = MIMEText(fp.read(), _subtype='plain', _charset='utf-8')

        thread_number = random.randint(0, 10000)
        msg['Subject'] = 'Minutely Spam Report (randomizer: {0})'.format(thread_number)
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipients)

        with smtplib.SMTP(host='smtp.gmail.com', port=587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender_email, password)
            s.sendmail(sender_email, recipients, msg.as_string())

        print("Email sent to: " + ', '.join(recipients))
        time.sleep(60)  # Change rate of fire here

spam_every_minute()