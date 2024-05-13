import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
sender_email = "birkullanicix@gmail.com"
receiver_email = "birkullanicix@gmail.com"
subject = ""
body = ""
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

file_path = "./graphsperminute.xlsx"
with open(file_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read()) 
encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {file_path}",
)
message.attach(part)
text = message.as_string()
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email,"wrrt pxqr pyib nzcs")
now=datetime.now()
x=1
server.sendmail(sender_email,receiver_email,text)
