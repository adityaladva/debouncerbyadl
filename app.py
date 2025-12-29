import streamlit as st
import smtplib
from email.message import EmailMessage
import re

# =========================
# DUMMY CREDENTIALS
# REPLACE WITH REAL ONES
# =========================
GMAIL_USER = "protectbyadl@gmail.com"
GMAIL_APP_PASSWORD = "aobmritwgyugqrat"  # example format (no spaces)
# =========================

st.set_page_config(page_title="Email Validator", page_icon="📧")

st.title("📧 Email Validator (SMTP Debouncer)")
st.write("Checks whether an email is accepted by the mail server using Gmail SMTP (587).")

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

            # --- SMTP via 587 ---
            server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)

            server.send_message(msg)
            server.quit()

            st.success("✅ Email accepted by SMTP server")

        except smtplib.SMTPRecipientsRefused:
            st.error("❌ Email rejected by recipient server")

        except smtplib.SMTPAuthenticationError:
            st.error("❌ Gmail authentication failed (check app password)")

        except smtplib.SMTPException as e:
            st.error(f"❌ SMTP error: {e}")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
