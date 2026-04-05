from flask import Flask, request, render_template, redirect
from email_sender import send_emails

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    try:
        # Get form data
        names = request.form.get("names")
        emails = request.form.get("emails")
        template = request.form.get("template")

        # Convert input into list
        names_list = names.split(",")
        emails_list = emails.split(",")

        data = []
        for i in range(len(names_list)):
            data.append({
                "name": names_list[i].strip(),
                "email": emails_list[i].strip()
            })

        # Send emails
        send_emails(data, template)

        return "✅ Emails sent successfully!"

    except Exception as e:
        return f"❌ Error: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)