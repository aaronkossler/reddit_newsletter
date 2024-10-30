import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import getenv

# Replace these with your details
zoho_email = "your_email@zoho.com"  # Your Zoho email address
app_password = "your_app_password"  # Your Zoho app password
recipient_email = "recipient@example.com"  # Recipient's email address


def send_zoho_email(recipient_email, subject, body):
    zoho_email = getenv("ZOHO_EMAIL")
    app_password = getenv("ZOHO_PASS")

    # Set up the email
    msg = MIMEMultipart()
    msg['From'] = zoho_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Zoho SMTP server and send the email
    try:
        with smtplib.SMTP('smtp.zoho.eu', 587) as server:
            server.starttls()  # Enable security
            server.login(zoho_email, app_password)  # Log in to your account
            server.sendmail(zoho_email, recipient_email,
                            msg.as_string())  # Send the email
            print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print("Authentication failed. Please check your app password.")
        print(e.smtp_code, e.smtp_error)
    except smtplib.SMTPException as e:
        print("SMTP error occurred.")
        print(e)
    except Exception as e:
        print("An unexpected error occurred.")
        print(e)
