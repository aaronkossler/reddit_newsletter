from os import getenv
from zohomail import send_zoho_email
from openrouter import generate_newsletter

if __name__ == "__main__":
    output = generate_newsletter("artificial")
    email = getenv("EMAIL")
    subject = "Newsletter"
    send_zoho_email(email, subject, output)
