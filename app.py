from flask import Flask, render_template, request
import pandas as pd
from email_sender import send_emails
import os

app = Flask(__name__)

# Default template (your required one)
DEFAULT_TEMPLATE = """Hi {{name}},

I hope you are doing well.

I came across your profile as a {{role}} at {{company}} and found it very interesting.

I wanted to connect with you regarding an opportunity that might align with your experience.

Looking forward to your response.

Best regards,
Your Name
"""

# Home route
@app.route('/')
def home():
    return render_template('index.html', template=DEFAULT_TEMPLATE)


# Send emails route
@app.route('/send', methods=['POST'])
def send():
    file = request.files['file']
    template = request.form['template']

    # Read CSV
    data = pd.read_csv(file, sep=",", engine="python")

    # Fix column issues
    data.columns = data.columns.str.strip()

    print("Columns:", data.columns)

    # Call email sender
    send_emails(data, template)

    return "✅ Emails processed successfully!"


# Render deployment config
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))