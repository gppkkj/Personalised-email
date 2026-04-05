import smtplib
import time
from datetime import datetime

def send_emails(data, template):

   sender_email = "your_email@gmail.com"
   password = "your_app_password"  # ⚠ Use App Password (no spaces)

    # Connect to Gmail SMTP
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    print("\n🚀 Starting email sending...\n")

    count = 1

    for index, row in data.iterrows():
        try:
            # ✅ Clean values from CSV
            email = str(row.get('email', '')).strip()
            name = str(row.get('name', '')).strip()
            company = str(row.get('company', '')).strip()
            role = str(row.get('role', '')).strip()

            # Skip if email missing
            if not email:
                print("❌ Skipping row - missing email")
                continue

            # ✅ Handle template properly (both cases)
            if "{{name}}" in template:
                message = template.replace("{{name}}", name)\
                                  .replace("{{company}}", company)\
                                  .replace("{{role}}", role)
            else:
                # Fallback template (auto-fix if user input is wrong)
                message = f"""Hi {name},

I hope you are doing well.

I saw your work at {company} as a {role}.

I would like to connect with you regarding an opportunity.

Best regards,
Your Name
"""

            full_message = f"Subject: Opportunity\n\n{message}"

            # Send email
            server.sendmail(sender_email, email, full_message)

            print(f"✅ {count}. Sent to {name} ({email})")

            # Log success
            with open("logs.txt", "a") as log:
                log.write(f"{datetime.now()} SUCCESS: {email}\n")

            count += 1

            # Delay to avoid spam detection
            time.sleep(5)

        except Exception as e:
            print(f"❌ Failed for {email} | Error: {e}")

            with open("logs.txt", "a") as log:
                log.write(f"{datetime.now()} FAILED: {email}\n")

    server.quit()

    print("\n🎉 All emails processed!")