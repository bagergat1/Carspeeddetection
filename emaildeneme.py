import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd 

veri=pd.read_excel("kayitlarx.xlsx")
veri.pop("Unnamed: 0")
veri.set_index(veri[0], inplace=True)
veri.pop(0)

def mail(carID, speed2, asma, ceza_tutar, hesaplanan_asma):
    msg = MIMEMultipart()
    email = "birkullanicix@gmail.com"
    receiver_email = "birkullanicix@gmail.com"
    subject = "Hiz siniri asma cezasi"
    
    message = f"""{carID} numarali arac {speed2} Km/h ile hiz sinirini %{asma} oraninda asmistir.
    {carID} numarali aracin hiz sinirini %{hesaplanan_asma}'den fazla astigi tespit edildiginden dolayi cezai islem uygulanmistir.
    Yazilan ceza tutari:{ceza_tutar} TL."""
    
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    path = f"./Screenshots/{carID}.png"
    with open(path, 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename=f"{carID}.png")
        msg.attach(img)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, "wrrt pxqr pyib nzcs")
    server.sendmail(email, receiver_email, msg.as_string())
    print("Ceza mail'i gönderilmiştir.")

for i in range(1, len(veri.columns)):
    carID = int(veri[i][0])
    speed2 = veri[i][1]
    asma = veri[i][2]
    ceza_tutar = veri[i][3]
    hesaplanan_asma = veri[i][4]
    mail(carID, speed2, asma, ceza_tutar, hesaplanan_asma)