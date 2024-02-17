import smtplib, ssl

def send_email(receiver, raw_message):
    host = "smtp.gmail.com"
    port = 465

    username = "diosama99@gmail.com"
    password = "fuld itha npbv tich"

    # receiver = "diosama99@gmail.com"

    message = f"""\
Subject: New email from {receiver}

From: {receiver}
{raw_message}
"""

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
