import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

def send_test_email():
    sender_email = "kris.sentinel.control@gmail.com"
    receiver_email = "matthewprasa@gmail.com"
    password = "pjgbqxvmgnkzpqso"

    message = MIMEMultipart("alternative")
    message["Subject"] = "⚡ Kris: System Connection Test"
    message["From"] = f"Kris Sentinel <{sender_email}>"
    message["To"] = receiver_email

    text = """
    Matthew,

    System connection test successful. 

    The 7 AM Executive Briefing is now wired for delivery to this inbox.
    Nightly operations are commencing.

    - Kris
    """
    
    html = """
    <html>
      <body style="font-family: Arial, sans-serif; color: #f8fafc; background-color: #0f172a; padding: 20px;">
        <h2 style="color: #38bdf8;">⚡ Kris: System Connection Test</h2>
        <p>Matthew,</p>
        <p>System connection test <b>successful</b>.</p>
        <hr style="border: 0; border-top: 1px solid #334155; margin: 20px 0;">
        <p>The <b>7 AM Executive Briefing</b> is now wired for delivery to this inbox.</p>
        <p>Nightly operations are commencing.</p>
        <br>
        <p style="color: #94a3b8;">- Kris (Chief of Staff)</p>
      </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("SUCCESS: Email sent.")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    send_test_email()
