import cv2
import dlib
import time
import threading
import math
import smtplib
import pandas as pd
import numpy as np
import datetime
import os
import subprocess
from yasal_hiz_siniri import yasal_hiz_siniri 
import pyautogui
from yasal_hiz_siniri import pixel1
from yasal_hiz_siniri import pixel2
from cropping import crop_image
from datetime import datetime
import shutil
from yasal_hiz_siniri import video
from yasal_hiz_siniri import crop_box
# import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

veri=pd.read_excel("ceza_hesap.xlsx")
carCascade = cv2.CascadeClassifier('myhaar.xml')
# video = cv2.VideoCapture('./testvideo.mp4')
hizsiniriasimorani=list(veri["Hız Sınırı Aşım Oranı"])
cezaorani=list(veri["Ceza Tutarı"])
mesaj=list()
WIDTH = 1280
HEIGHT = 720
now=datetime.now()

cezalar2=pd.DataFrame()
hesaplanan_asma1=list()
hesaplanan_asma2=list()
mesaj=list()
asma_miktari2=list()
ceza_tutar2=list()

ceza_tutar1=list()
ceza_liste=list()
ceza_liste2=list()
ceza_yemeyenler=list()
# *************************************************************************************

# sender_email = "birkullanicix@gmail.com"
# receiver_email = "birkullanicix@gmail.com"
# subject = ""
# body = ""
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = subject
# message.attach(MIMEText(body, "plain"))
# data=pd.read_excel("./kayitlarx.xlsx")
# data.to_excel("./yenikayit.xlsx")

# file_path = "./yenikayit.xlsx"
# with open(file_path, "rb") as attachment:
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read()) 
# encoders.encode_base64(part)
# part.add_header(
#     "Content-Disposition",
#     f"attachment; filename= {file_path}",
# )
# def send(part,sender_email,receiver_email,text):
# 	message.attach(part)
# 	text = message.as_string()
# 	server=smtplib.SMTP("smtp.gmail.com",587)
# 	server.starttls()
# 	server.login(sender_email,"wrrt pxqr pyib nzcs")
# 	server.sendmail(sender_email,receiver_email,text)

# *************************************************************************************

def estimateSpeed(location1, location2):
	d_pixels = math.sqrt(math.pow(location2[0] - location1[0], 2) + math.pow(location2[1] - location1[1], 2))
	# ppm = location2[2] / carWidht
	ppm = 8
	d_meters = d_pixels / ppm
	fps = 25
	speed = d_meters * fps * 1.6
	return speed

# def mail(carID,speed2,asma,ceza_tutar,hesaplanan_asma):
#     email="birkullanicix@gmail.com"
#     receiver_email="birkullanicix@gmail.com"
#     subject="Hiz siniri asma cezasi"
#     message=f"""        {carID} numarali arac {speed2} Km/h ile hiz sinirini %{asma} oraninda asmistir.
# 	{carID} numarali aracin hiz sinirini %{hesaplanan_asma}'den fazla astigi tespit edildiginden dolayi cezai islem uygulanmistir.
# 	Yazilan ceza tutari:{ceza_tutar} TL."""
#     text=f"Subject:{subject}\n\n{message}"
#     server=smtplib.SMTP("smtp.gmail.com",587)
#     server.starttls()
#     server.login(email,"wrrt pxqr pyib nzcs")
#     server.sendmail(email,receiver_email,text)
#     print("Ceza mail'i gönderilmiştir.")

def ceza_hesap(asma_miktari,hizsiniriasimorani,cezaorani):
	i=len(hizsiniriasimorani)-1
	while True:
		if float(asma_miktari)>=float(hizsiniriasimorani[i]):
			return cezaorani[i]
		if i==0:
			break
		i-=1

def asim_hesaplama(asma_miktari,hizsiniriasimorani):
	j=len(hizsiniriasimorani)-1
	while True:
		if float(asma_miktari)>=float(hizsiniriasimorani[j]):
			return hizsiniriasimorani[j]
		if j==0:
			break
		j-=1

def trackMultipleObjects():
	rectangleColor = (0, 255, 0)
	frameCounter = 0
	currentCarID = 0
	fps = 0
	
	carTracker = {}
	carNumbers = {}
	carLocation1 = {}
	carLocation2 = {}
	speed = [None] * 1000
	speed2 = [None] * 1000
	out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (WIDTH,HEIGHT))

	constant=1
	while True:
		start_time = time.time()
		rc, image = video.read()
		if type(image) == type(None):
			break
		
		image = cv2.resize(image, (WIDTH, HEIGHT))
		resultImage = image.copy()
		
		frameCounter = frameCounter + 1
		
		carIDtoDelete = []

		for carID in carTracker.keys():
			trackingQuality = carTracker[carID].update(image)
			
			if trackingQuality < 7:
				carIDtoDelete.append(carID)
				
		for carID in carIDtoDelete:
			carTracker.pop(carID, None)
			carLocation1.pop(carID, None)
			carLocation2.pop(carID, None)
			
		if not (frameCounter % 10):
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			cars = carCascade.detectMultiScale(gray, 1.1, 13, 18, (24, 24))
			
			for (_x, _y, _w, _h) in cars:
				x = int(_x)
				y = int(_y)
				w = int(_w)
				h = int(_h)
			
				x_bar = x + 0.5 * w
				y_bar = y + 0.5 * h
				
				matchCarID = None
			
				for carID in carTracker.keys():
					trackedPosition = carTracker[carID].get_position()
					
					t_x = int(trackedPosition.left())
					t_y = int(trackedPosition.top())
					t_w = int(trackedPosition.width())
					t_h = int(trackedPosition.height())
					
					t_x_bar = t_x + 0.5 * t_w
					t_y_bar = t_y + 0.5 * t_h
				
					if ((t_x <= x_bar <= (t_x + t_w)) and (t_y <= y_bar <= (t_y + t_h)) and (x <= t_x_bar <= (x + w)) and (y <= t_y_bar <= (y + h))):
						matchCarID = carID
				
				if matchCarID is None:
					
					tracker = dlib.correlation_tracker()
					tracker.start_track(image, dlib.rectangle(x, y, x + w, y + h))
					
					carTracker[currentCarID] = tracker
					carLocation1[currentCarID] = [x, y, w, h]

					currentCarID = currentCarID + 1
		


		for carID in carTracker.keys():
			trackedPosition = carTracker[carID].get_position()
					
			t_x = int(trackedPosition.left())
			t_y = int(trackedPosition.top())
			t_w = int(trackedPosition.width())
			t_h = int(trackedPosition.height())
			
			cv2.rectangle(resultImage, (t_x, t_y), (t_x + t_w, t_y + t_h), rectangleColor, 4)
			carLocation2[carID] = [t_x, t_y, t_w, t_h]
			sender_email = "birkullanicix@gmail.com"
			receiver_email = "birkullanicix@gmail.com"
			subject = ""
			body = ""
			message = MIMEMultipart()
			message["From"] = sender_email
			message["To"] = receiver_email
			message["Subject"] = subject
			message.attach(MIMEText(body, "plain"))
			file_path = "yenikayit.xlsx"
			with open(file_path, "rb") as attachment:
				part = MIMEBase("application", "octet-stream")
				part.set_payload(attachment.read()) 
			encoders.encode_base64(part)
			part.add_header(
			    "Content-Disposition",
			    f"attachment; filename= {file_path}",
			)
			# print(file_path)
			def send(part,sender_email,receiver_email,text):
				message.attach(part)
				text = message.as_string()
				server=smtplib.SMTP("smtp.gmail.com",587)
				server.starttls()
				server.login(sender_email,"wrrt pxqr pyib nzcs")
				server.sendmail(sender_email,receiver_email,text)

			now2=datetime.now()
			if now2.minute-now.minute==1*constant:
				print(now2.minute-now.minute)
				send(part,sender_email,receiver_email,body)
				constant+=1
				print("Excel dosyası sanal sisteme gönderilmiştir.")
				
		
		end_time = time.time()
		
		if not (end_time == start_time):
			fps = 1.0/(end_time - start_time)

		for i in carLocation1.keys():	
			
			if frameCounter % 1 == 0:
				[x1, y1, w1, h1] = carLocation1[i]
				[x2, y2, w2, h2] = carLocation2[i]
				carLocation1[i] = [x2, y2, w2, h2]
				# print(list(carLocation1.values())[0][1])

				if [x1, y1, w1, h1] != [x2, y2, w2, h2]:
					if (speed[i] == None or speed[i] == 0) and y1 >= 275 and y1 <= 285:
						speed[i] = estimateSpeed([x1, y1, w1, h1], [x2, y2, w2, h2])

					
					if speed[i] != None and y1 >= 180:
						cv2.putText(resultImage, str(int(speed[i])) + " kmh", (int(x1 + w1/2), int(y1-5)),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
					
						asma_miktari=format(((speed[i]*100)/yasal_hiz_siniri)-100,".2f")
						
						if speed[i]>=yasal_hiz_siniri:
							speed2[i]=format(speed[i],".2f")
							speed2[i]=float(speed2[i])
							ceza_tutar=ceza_hesap(asma_miktari,hizsiniriasimorani,cezaorani)
							hesaplanan_asma=asim_hesaplama(asma_miktari,hizsiniriasimorani)

							for j in list(carLocation1.values()):
								if j[1]<pixel2 and j[1]>pixel1:
									image = pyautogui.screenshot()
									image1 = pyautogui.screenshot(f"./Screenshots/{carID}.png")
									
									input_image_path = f"/home/bagergat/Desktop/Bitirme/Screenshots/{carID}.png" 
									output_image_path = f"/home/bagergat/Desktop/Bitirme/Screenshots/{carID}.png" 
									# crop_box = (300, 100, 1100, 800) 
									crop_image(input_image_path, output_image_path, crop_box)

									# crop_image(input_image_pat
									# print(video.__qualname__)h, output_image_path, crop_box)
									
									
							
							if carID and speed2 and asma_miktari and ceza_tutar and hesaplanan_asma!=None:
								my_dict=dict(carID=carID,speed2=speed2[i],asma=asma_miktari,ceza_tutar=ceza_tutar,hesaplanan_asma=hesaplanan_asma)
								cezalar=pd.Series(my_dict)
								cezalar2[i]=cezalar
								
								cezalar2.to_excel("./kayitlarx.xlsx")
								os.remove("./yenikayit.xlsx")
								shutil.copy("./kayitlarx.xlsx","./yenikayit.xlsx")
								# cezalar2.to_excel("graphsperminute.xlsx")
								
						elif speed[i]<yasal_hiz_siniri and speed[i]!=0:
							ceza_yemeyenler.append(speed[i])
							ceza_yemeyenler2=pd.Series(ceza_yemeyenler).unique()
							pd.DataFrame(ceza_yemeyenler2).to_excel("ceza_almayan_araclar.xlsx")
		cv2.imshow('result', resultImage)

		if cv2.waitKey(33) == 27:
			break
	
	cv2.destroyAllWindows()
if __name__ == '__main__':
	trackMultipleObjects()
df=pd.read_excel("kayitlarx.xlsx")
df.columns=[i for i in range(len(df.columns))]
df.to_excel("kayitlarx.xlsx")
subprocess.run(["python3","/home/bagergat/Desktop/Bitirme/mail_sending.py"])
import Graphs
import Graphsforcarsnotfired
import pdfsendingbymail
