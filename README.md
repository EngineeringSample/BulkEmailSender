# BulkEmailSender

**Tutorial: Sending Bulk Emails with Python (Using "BulkEmailSender.py")**

**Prerequisites:**
- Python installed on your computer.
- The `smtplib` and `email` libraries are available.

**Step 1: Download the "BulkEmailSender.py" Script**

You can download the script from the provided GitHub URL: [BulkEmailSender.py](https://raw.githubusercontent.com/YuanLiuchang/BulkEmailSender/main/BulkEmailSender.py). Save it to your computer.

**Step 2: Run the Script**

1. Open a terminal or command prompt.
2. Navigate to the directory where you saved "BulkEmailSender.py."
3. Run the script using Python: `python BulkEmailSender.py`.

**Step 3: Enter SMTP Server Information**

The script will prompt you to enter the following SMTP server information:

- SMTP server address: This is the address of your email service provider's SMTP server. Common addresses include "smtp.gmail.com" for Gmail or "smtp.live.com" for Outlook.
- SMTP server port: The port number for the SMTP server. The standard ports are 587 for TLS and 465 for SSL.
- SMTP username: Your email address or username.
- SMTP password: Your email account password.

**Step 4: Enter Email Content**

The script will ask you to provide the email content:

- Email subject: Enter the subject line for your email.
- Email body: Enter the email's message or content.

**Step 5: Enter Recipient Email Addresses**

You can enter the email addresses of the recipients one by one. To stop adding recipients, simply press Enter without typing an email address.

**Step 6: Send Emails**

The script will connect to the SMTP server using the provided information and start sending emails to the specified recipients. It will display a message for each email sent.

**Step 7: Finish**

Once all the emails have been sent, the script will display a message indicating that the sending process is complete.

**Additional Tips:**
- Make sure you have the correct SMTP server information, as this may vary depending on your email service provider.
- Be careful with your SMTP username and password, and never share this information or store it insecurely.
- Ensure you have permission to send emails to the recipients in your list.
