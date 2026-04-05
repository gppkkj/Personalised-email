from flask import Flask, render_template, request
import pandas as pd
from email_sender import send_emails

app = Flask(__name__)

# Default template (always shown on UI)
DEFAULT_TEMPLATE = """Hi {{name}},

I hope you are doing well.

I saw your work at {{company}} as a {{role}}.

I would like to connect with you regarding an opportunity.

Best regards,
Your Name
"""

@app.route('/')
def home():
    return render_template('index.html', template=DEFAULT_TEMPLATE)


@app.route('/send', methods=['POST'])
def send():
    try:
        file = request.files.get('file')
        template = request.form.get('template')

        if not file:
            return "❌ Please upload a CSV file"

        if not template:
            return "❌ Template is missing"

        # Read CSV
        data = pd.read_csv(file)

        # Clean column names
        data.columns = data.columns.str.strip().str.lower()

        # Required columns check
        required_cols = ['email', 'name', 'company', 'role']
        for col in required_cols:
            if col not in data.columns:
                return f"❌ Missing column: {col}"

        # Send emails
        send_emails(data, template)

        return "✅ Emails processed successfully!"

    except Exception as e:
        return f"❌ Error: {str(e)}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)