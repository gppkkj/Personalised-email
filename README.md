# 📧 Personalized Email Sender

## 📌 Project Overview
This project is a Flask-based web application that sends personalized emails to multiple recipients using a CSV file.

Each email is dynamically customized using placeholders such as `{{name}}`, `{{company}}`, and `{{role}}`, making every email appear as a one-to-one message instead of bulk mail.

---

## 🚀 Features
- Send emails to 100+ recipients
- Personalized content using placeholders
- CSV file upload support
- Individual email sending (no CC/BCC)
- Gmail SMTP integration
- Delay between emails (avoids spam detection)
- Logging of success and failures
- Simple web interface

---

## 🛠️ Tech Stack
- Python
- Flask
- Pandas
- SMTP (Gmail)

---

## 📂 Project Structure
personalized-email-sender/
│
├── app.py
├── email_sender.py
├── sample_data.csv
├── README.md
├── templates/
│ └── index.html


---

 How to Run the Project

# 1️. Install Python
Download and install Python from:
https://www.python.org/downloads/

Make sure to check:
✔ "Add Python to PATH"

# 2. Install Required Libraries

Open terminal and run:
pip install flask pandas


---

# 3️. Set Up Gmail App Password (VERY IMPORTANT)

Gmail does NOT allow normal passwords for sending emails via code.  
You must use an **App Password**.

#### Step 1: Enable 2-Step Verification
Go to:
https://myaccount.google.com/security

Turn ON:
   "2-Step Verification"
you will get a mail to accept the 2 step security 
---

#### Step 2: Generate App Password
Go to:
https://myaccount.google.com/apppasswords

- Select App → Mail
- Select Device → Windows Computer
- Click Generate

You will get a password like:  abcd efgh ijkl mnop  
## Remove spaces from password :abcdefghijklmnop

---

#### Step 3: Use in Code

Open `email_sender.py` and update:
sender_email = "your_email@gmail.com"   # Your account email address which you have created password with 
password = "abcdefghijklmnop"


⚠ IMPORTANT:
- Remove spaces from the password
- Use the SAME Gmail account that generated the password

---

### 4️⃣ Prepare CSV File

Use the format below:
email,name,company,role
test1@gmail.com,Rahul,Google,Engineer
test2@gmail.com,Priya,Amazon,Analyst


## 5. Run application 

python app.py

## 6. Open in Browser 

http://127.0.0.1:5000 
  



### 7️⃣ Use the Application

1. Upload your CSV file  
2. Edit the email template (optional)  
3. Click **Send Emails**


## 📧 Example Template


Hi {{name}},

I hope you are doing well.

I saw your work at {{company}} as a {{role}}.

I would like to connect with you regarding an opportunity.

Best regards,
Your Name ## 🙋 Author



---

## 📊 Logging

The application logs:
- Successful emails
- Failed emails

Check:  logs.txt  


