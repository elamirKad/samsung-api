import yagmail
import os


async def send_email(receiver: str, subject: str, body: str):
    yag = yagmail.SMTP(
        user=os.getenv('EMAIL_USER'),
        password=os.getenv('EMAIL_PASSWORD'),
        host=os.getenv('EMAIL_HOST'),
        port=os.getenv('EMAIL_PORT'),
    )
    yag.send(
        to=receiver,
        subject=subject,
        contents=body,
    )


async def send_code(receiver: str, code: str):
    subject = "Your verification code"
    body = f"This is your code: {code}"
    send_email(receiver, subject, body)
