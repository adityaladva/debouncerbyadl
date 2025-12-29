import streamlit as st
import smtplib
from email.message import EmailMessage
import re

# =========================
# DUMMY GMAIL CREDENTIALS
# (REPLACE WITH REAL ONES)
# =========================
GMAIL_USER = "protectbyadl@gmail.com"
GMAIL_APP_PASSWORD = "aobmritwgyugqrat"   # DUMMY APP PASSWORD
# =========================

st.set_page_config(page_title="Email Validator", page_icon="📧")

st.title("📧 Email Validator (SMTP Debouncer)")
st.write("Checks whether an email is accepted by the mail server using Gmail SMTP.")

email = st.text_input("Enter email address")

def valid_email_format(email):
    return re.match(r"^[^@]+@[^@]+\.[^@]+$", email)

if st.button("Check Email"):
    if not email:
        st.warning("Please enter an email address.")

    elif not valid_email_format(email):
        st.error("❌ Invalid email format.")

    else:
        try:
            msg = EmailMessage()
            msg["From"] = GMAIL_USER
            msg["To"] = email
            msg["Subject"] = "SMTP Validation Test"
            msg.set_content("Email validation test")

            server = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=6)
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.send_message(msg)
            server.quit()

            st.success("✅ Email accepted by SMTP server")

        except smtplib.SMTPRecipientsRefused:
            st.error("❌ Email rejected by recipient server")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
