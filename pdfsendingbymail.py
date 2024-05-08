import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
sender_email = "birkullanicix@gmail.com"
receiver_email = "birkullanicix@gmail.com"
subject = "Ceza Alan Araçların Verileri"
body = "Ekte cezalandırılan araçların verilerini içeren grafiğini pdf formatında bulabilirsiniz."
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

file_path = "./Ceza_alanlar.pdf"
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
server.sendmail(sender_email,receiver_email,text)
print("PDF gönderilmiştir.")