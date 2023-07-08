#run "pip install requests" in terminal before using. Replace the email adress with your own to send.
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data["bitcoin"]["usd"]
    return price

def send_email(sender_email, sender_password, recipient_email, subject, message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create email message
    email_message = MIMEMultipart()
    email_message["From"] = sender_email
    email_message["To"] = recipient_email
    email_message["Subject"] = subject
    email_message.attach(MIMEText(message, "plain"))

    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send email
    server.send_message(email_message)

    # Clean up
    server.quit()

# Configure email and API settings
sender_email = "your_email@gmail.com"
sender_password = "your_password"
recipient_email = "recipient_email@example.com"
subject = "Bitcoin Price Update"

# Get Bitcoin price
bitcoin_price = get_bitcoin_price()

# Create email message
message = f"The current price of Bitcoin is ${bitcoin_price}."

# Send email
send_email(sender_email, sender_password, recipient_email, subject, message)

