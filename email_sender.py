import smtplib
import os

def send_emails(data, template):
    # Connect to Brevo SMTP
    server = smtplib.SMTP("smtp-relay.brevo.com", 587)
    server.starttls()

    # Login using environment variables
    server.login(
        os.getenv("SMTP_USER"),
        os.getenv("SMTP_PASS")
    )

    for user in data:
        # Personalize message
        message = template.replace("{name}", user["name"])

        msg = f"Subject: Personalized Email\n\n{message}"

        server.sendmail(
            os.getenv("SMTP_USER"),
            user["email"],
            msg
        )

    server.quit()