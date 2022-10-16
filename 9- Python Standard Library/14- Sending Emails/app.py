from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from pathlib import Path
import smtplib


template = Template(
    Path('9- Python Standard Library/14- Sending Emails/template.html').read_text())
body = template.substitute({"name": "Jonn"})


message = MIMEMultipart()
message["from"] = "kob87nn@hotmail.com"
message["to"] = "kob87@list.ru"
message["subject"] = "Test"
message.attach(MIMEText(body, "html"))

with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("kob87nn@hotmail.com", "Tarxun4Eva$$")
    smtp.send_message(message)
    print("ok")

# with smtplib.SMTP(host="smtp.mail.ru", port=465) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("kob87@list.ru", "GloAss1987")
#     smtp.send_message(message)
#     print("ok")
