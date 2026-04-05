import smtplib
import time
import os
from datetime import datetime

def send_emails(data, template):

    # Get credentials (safe for deployment)
    sender_email = os.environ.get("EMAIL") or "your_email@gmail.com"
    password = os.environ.get("PASSWORD") or "your_app_password"

    # Connect to Gmail SMTP
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    print("\n🚀 Sending emails...\n")

    for index, row in data.iterrows():
        try:
            email = str(row.get('email', '')).strip()
            name = str(row.get('name', '')).strip()
            company = str(row.get('company', '')).strip()
            role = str(row.get('role', '')).strip()

            if not email:
                continue

            # Personalize email
            message = template.replace("{{name}}", name)\
                              .replace("{{company}}", company)\
                              .replace("{{role}}", role)

            full_message = f"Subject: Opportunity\n\n{message}"

            server.sendmail(sender_email, email, full_message)

            print(f"✅ Sent to {name} ({email})")

            # Log success
            with open("logs.txt", "a") as log:
                log.write(f"{datetime.now()} SUCCESS: {email}\n")

            time.sleep(5)  # Delay to avoid spam

        except Exception as e:
            print(f"❌ Failed for {email}: {e}")

            with open("logs.txt", "a") as log:
                log.write(f"{datetime.now()} FAILED: {email}\n")

    server.quit()
    print("\n🎉 Done sending emails!")