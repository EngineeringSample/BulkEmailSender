import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Get SMTP server information
smtp_server = input("Enter SMTP server address: ")
smtp_port = int(input("Enter SMTP server port: "))
smtp_username = input("Enter SMTP username: ")
smtp_password = input("Enter SMTP password: ")

# Create email content
subject = input("Enter email subject: ")
body = input("Enter email body: ")

# Create email object
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Get recipient information (batch)
recipients = []
while True:
    recipient = input("Enter recipient's email address (Press Enter to finish): ")
    if not recipient:
        break
    recipients.append(recipient)

# Connect to the SMTP server and send emails
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Use TLS encryption (if supported by the SMTP server)
    server.login(smtp_username, smtp_password)

    for recipient in recipients:
        msg['To'] = recipient
        server.sendmail(smtp_username, recipient, msg.as_string())
        print(f'Email sent to {recipient}')

    server.quit()
    print('Sending complete')
except Exception as e:
    print(f'Error sending emails: {str(e)}')
  
