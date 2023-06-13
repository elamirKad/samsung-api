import aiosmtplib
from email.message import EmailMessage
import os
import asyncio


async def send_email(receiver: str, subject: str, body: str):
    message = EmailMessage()
    message["From"] = os.getenv('EMAIL_USER')
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)
    print(f"Sending email to {receiver}")
    print(f"Email content: {body}")
    print(f"Email host: {os.getenv('EMAIL_HOST')}")
    print(f"Email port: {os.getenv('EMAIL_PORT')}")
    print(f"Email user: {os.getenv('EMAIL_USER')}")
    print(f"Email password: {os.getenv('EMAIL_PASSWORD')}")
    await aiosmtplib.send(
        message,
        hostname=os.getenv('EMAIL_HOST'),
        port=os.getenv('EMAIL_PORT'),
        username=os.getenv('EMAIL_USER'),
        password=os.getenv('EMAIL_PASSWORD'),
        use_tls=True
    )


async def send_code(receiver: str, code: str):
    subject = "Your verification code"
    body = f"This is your code: {code}"
    print(f"Sending code {code} to {receiver}")
    await send_email(receiver, subject, body)
