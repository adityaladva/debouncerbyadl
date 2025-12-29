import smtplib, ssl
import streamlit as st
from email.message import EmailMessage

st.set_page_config(page_title="SMTP Delivery Demo", layout="centered")

st.markdown(
    """
    <h2>SMTP Delivery Quality Demo</h2>
    <p><b>ASTRA CONSULTANCY | INFURA TECHNOLOGIES</b></p>
    <p>Free Email SMTP Service – Product Sample</p>
    <p>contact us on LinkedIn: https://www.linkedin.com/in/aditya-ladva/ <p>
    <p> For higher volume contact us at protectbyadl@gmail.com with subject as "CONTRACT" <p>
    <hr>
    """,
    unsafe_allow_html=True
)

# SMTP CONFIG (DEMO)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "protectbyadl@gmail.com"
SMTP_PASS = "aobmritwgyugqrat"  # demo

# INPUTS
to_email = st.text_input("Recipient Email")
subject = st.text_input("Subject", "SMTP Delivery Quality Test")

# FIXED MESSAGE + SIGNATURE
EMAIL_BODY = """This email is sent to demonstrate SMTP delivery quality
using our free email SMTP service & Software Quality.

---
A FREE PRODUCT BY ADL | ASTRA CONSULTANCY | INFURATECHNOLOGIES

For higher volume email requirements, contact us on LinkedIn:
https://www.linkedin.com/in/aditya-ladva/
"""

def send_mail():
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)
        server.starttls(context=ssl.create_default_context())
        server.login(SMTP_USER, SMTP_PASS)

        msg = EmailMessage()
        msg["From"] = SMTP_USER
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(EMAIL_BODY)

        server.send_message(msg)
        server.quit()

        return "✅ Email accepted by SMTP server"

    except smtplib.SMTPRecipientsRefused:
        return "❌ Delivery failed: Email does not exist"

    except Exception as e:
        return f"⚠️ SMTP Error: {e}"

if st.button("Send Test Email"):
    if not to_email:
        st.warning("Please enter recipient email")
    else:
        st.info(send_mail())
