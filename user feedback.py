import smtplib
from email.mime.text import MIMEText

def send_email(recipient, subject, body):
    sender = 'your_email@example.com'
    password = 'your_password'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

 with smtplib.SMTP_SSL('smtp.example.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
        print("Email sent successfully.")

send_email('applicant@example.com', 'Loan Approval Status', 'Your loan application has been approved!')

