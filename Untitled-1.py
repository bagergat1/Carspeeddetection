# %%
import pandas as pd 
import numpy as np
import smtplib

# %%
veri=pd.read_excel("kayitlar.xlsx")
veri.pop("Unnamed: 0")
veri.columns=["Degerler"]
veri=pd.Series(veri["Degerler"]).unique()

# %%
def mail(carID,speed2,asma,ceza_tutar,hesaplanan_asma):
    email="birkullanicix@gmail.com"
    receiver_email="birkullanicix@gmail.com"
    subject="Hiz siniri asma cezasi"
    message=f"""        {carID} numarali arac {speed2} Km/h ile hiz sinirini %{asma} oraninda asmistir.
	{carID} numarali aracin hiz sinirini %{hesaplanan_asma}'den fazla astigi tespit edildiginden dolayi cezai islem uygulanmistir.
	Yazilan ceza tutari:{ceza_tutar} TL."""
    text=f"Subject:{subject}\n\n{message}"
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,"wrrt pxqr pyib nzcs")
    server.sendmail(email,receiver_email,text)
    print("Ceza mail'i gönderilmiştir.")

# %%
j=list()
for i in veri:
    vi=i.split()
    j.append(vi)
for i in j:
    i[0]=i[0].replace("[","")
    i[-1]=i[-1].replace("]","")
    mail(i[0],i[1],i[2],i[3],i[4])


