import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email information
sender_email = "birkullanicix@gmail.com"
receiver_email = "birkullanicix@gmail.com"
subject = "PDF Attachment"
body = "Ekte gerekli pdf'i bulabilirsiniz.\nİyi Günler"

# Create a multipart message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach body to the message
message.attach(MIMEText(body, "plain"))

# Path to the PDF file
file_path = "./Ceza_alanlar.pdf"

# Open the PDF file in binary mode
with open(file_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {file_path}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Send the email
# with smtplib.SMTP("smtp.example.com", 587) as server:
#     server.starttls()
#     server.login("your_email@example.com", "your_email_password")
#     server.sendmail(sender_email, receiver_email, text)

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email,"wrrt pxqr pyib nzcs")
server.sendmail(sender_email,receiver_email,text)
print("PDF gönderilmiştir.")