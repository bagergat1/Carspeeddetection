def emaildeneme(carID,speed,asma):
    # carID=self.carID
    # speed=self.speed
    # asma=self.asma
    import smtplib

    email="birkullanicix@gmail.com"
    receiver_email="birkullanicix@gmail.com"
    subject="Hiz siniri asma cezasi"
    message=f"{carID} numarali arac {speed} hizi ile hiz sinirini % {asma} oraninda asmistir."
    text=f"Subject:{subject}\n\n{message}"
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,"wrrt pxqr pyib nzcs")
    server.sendmail(email,receiver_email,text)
    print("email has been sent")