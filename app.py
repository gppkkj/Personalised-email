from flask import Flask, render_template, request
import pandas as pd
from email_sender import send_emails
import os

app = Flask(__name__)

# Default template (shown when page loads)
DEFAULT_TEMPLATE = """Hi {{name}},

I hope you are doing well.

I saw your work at {{company}} as a {{role}}.

I would like to connect with you regarding an opportunity.

Best regards,
Your Name
"""

# Home page
@app.route('/')
def home():
    return render_template('index.html', template=DEFAULT_TEMPLATE)

# When button is clicked
@app.route('/send', methods=['POST'])
def send():
    file = request.files['file']
    template = request.form['template']

    # Debug: check template
    print("TEMPLATE RECEIVED:\n", template)

    # Read CSV properly
    data = pd.read_csv(file, sep=",", engine="python")

    # Fix column issues
    data.columns = data.columns.str.strip()

    # Debug: check columns
    print("Columns:", data.columns)

    # Send emails
    send_emails(data, template)

    return "✅ Emails processed! Check terminal and logs.txt"

# Run app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))