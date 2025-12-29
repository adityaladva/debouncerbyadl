import streamlit as st
import smtplib
from email.message import EmailMessage
import re

# ===== DUMMY CREDENTIALS =====
GMAIL_USER = "protectbyadl@gmail.com"
GMAIL_APP_PASSWORD = "aobmritwgyugqrat"  # dummy
# =============================

st.set_page_config(page_title="Gmail Deliverability Checker", page_icon="📧")

st.title("📧 Gmail Deliverability Checker")
st.write("Checks whether a Gmail address is deliverable (SMTP acceptance).")

email = st.text_input("Enter Gmail address")

def is_valid_gmail(email):
    return re.match(r"^[^@]+@gmail\.com$", email)

if st.button("Check"):
    if not email:
        st.warning("Please enter an email address.")

    elif not is_valid_gmail(email):
        st.error("❌ Invalid Gmail format")

    else:
        try:
            msg = EmailMessage()
            msg["From"] = GMAIL_USER
            msg["To"] = email
            msg["Subject"] = "Deliverability Test"
            msg.set_content("Testing deliverability")

            server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)

            # If Gmail accepts this, it is deliverable
            server.send_message(msg)
            server.quit()

            st.success("✅ DELIVERABLE (Accepted by Gmail SMTP)")

        except smtplib.SMTPRecipientsRefused:
            st.error("❌ UNDELIVERABLE (Rejected by Gmail)")

        except smtplib.SMTPAuthenticationError:
            st.error("⚠️ AUTH ERROR (Invalid App Password)")

        except smtplib.SMTPException as e:
            st.error(f"⚠️ SMTP ERROR: {e}")

        except Exception as e:
            st.error(f"⚠️ ERROR: {e}")
