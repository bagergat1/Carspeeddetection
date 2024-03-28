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

veri=pd.read_excel("ceza_hesap.xlsx")
carCascade = cv2.CascadeClassifier('myhaar.xml')
video = cv2.VideoCapture('video.mp4')
hizsiniriasimorani=list(veri["Hız Sınırı Aşım Oranı"])
cezaorani=list(veri["Ceza Tutarı"])
mesaj=list()
WIDTH = 1280
HEIGHT = 720
yasal_hiz_siniri=60
cezalar2=pd.DataFrame()
# ceza_yiyenler=list()
# ceza_yiyenler2=list()
hesaplanan_asma1=list()
hesaplanan_asma2=list()
mesaj=list()
asma_miktari2=list()
ceza_tutar2=list()
# indirimli_ceza2=list()
ceza_tutar1=list()
ceza_liste=list()
ceza_liste2=list()
def estimateSpeed(location1, location2):
	d_pixels = math.sqrt(math.pow(location2[0] - location1[0], 2) + math.pow(location2[1] - location1[1], 2))
	# ppm = location2[2] / carWidht
	ppm = 8
	d_meters = d_pixels / ppm
	#print("d_pixels=" + str(d_pixels), "d_meters=" + str(d_meters))
	fps = 18
	speed = d_meters * fps * 3.6
	return speed

#***********************************************************************************************************************************************

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
# *****************************************************************************************************************************************************
def ceza_hesap(asma_miktari,hizsiniriasimorani,cezaorani):
	i=len(hizsiniriasimorani)-1
	while True:
		if float(asma_miktari)>=float(hizsiniriasimorani[i]):
			return cezaorani[i]
		if i==0:
			break
		i-=1
		
# *******************************************************************************************************************************************************
		
def asim_hesaplama(asma_miktari,hizsiniriasimorani):
	j=len(hizsiniriasimorani)-1
	while True:
		if float(asma_miktari)>=float(hizsiniriasimorani[j]):
			return hizsiniriasimorani[j]
		if j==0:
			break
		j-=1

# *************************************************************************************************************************************************	

# data = cv2.VideoCapture('/home/bagergat/Desktop/yeni/video.mp4') 
# frames = data.get(cv2.CAP_PROP_FRAME_COUNT) 
# fps = data.get(cv2.CAP_PROP_FPS) 
# seconds = round(frames / fps) 
# video_time = datetime.timedelta(seconds=seconds) 
# print(f"duration in seconds: {seconds}") 
# print(f"video time: {video_time}") 

# *************************************************************************************************************************************************	


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
	# Write output to video file
	out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (WIDTH,HEIGHT))


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
			# print ('Removing carID ' + str(carID) + ' from list of trackers.')
			# print ('Removing carID ' + str(carID) + ' previous location.')
			# print ('Removing carID ' + str(carID) + ' current location.')
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
					# print ('Creating new tracker ' + str(currentCarID))
					
					tracker = dlib.correlation_tracker()
					tracker.start_track(image, dlib.rectangle(x, y, x + w, y + h))
					
					carTracker[currentCarID] = tracker
					carLocation1[currentCarID] = [x, y, w, h]

					currentCarID = currentCarID + 1
		
		#cv2.line(resultImage,(0,480),(1280,480),(255,0,0),5)


		for carID in carTracker.keys():
			trackedPosition = carTracker[carID].get_position()
					
			t_x = int(trackedPosition.left())
			t_y = int(trackedPosition.top())
			t_w = int(trackedPosition.width())
			t_h = int(trackedPosition.height())
			
			cv2.rectangle(resultImage, (t_x, t_y), (t_x + t_w, t_y + t_h), rectangleColor, 4)
			
			# speed estimation
			carLocation2[carID] = [t_x, t_y, t_w, t_h]
		
		end_time = time.time()
		
		if not (end_time == start_time):
			fps = 1.0/(end_time - start_time)
		
		#cv2.putText(resultImage, 'FPS: ' + str(int(fps)), (620, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)


		for i in carLocation1.keys():	
			if frameCounter % 1 == 0:
				[x1, y1, w1, h1] = carLocation1[i]
				[x2, y2, w2, h2] = carLocation2[i]
		
				# print 'previous location: ' + str(carLocation1[i]) + ', current location: ' + str(carLocation2[i])
				carLocation1[i] = [x2, y2, w2, h2]
		
				# print 'new previous location: ' + str(carLocation1[i])
				if [x1, y1, w1, h1] != [x2, y2, w2, h2]:
					if (speed[i] == None or speed[i] == 0) and y1 >= 275 and y1 <= 285:
						speed[i] = estimateSpeed([x1, y1, w1, h1], [x2, y2, w2, h2])

					#if y1 > 275 and y1 < 285:
					if speed[i] != None and y1 >= 180:
						cv2.putText(resultImage, str(int(speed[i])) + " km/hr", (int(x1 + w1/2), int(y1-5)),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
					
						#print ('CarID ' + str(i) + ': speed is ' + str("%.2f" % round(speed[i], 0)) + ' km/h.\n')

					#else:
						#cv2.putText(resultImage, "Far Object", (int(x1 + w1/2), int(y1)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

						#print ('CarID ' + str(i) + ' Location1: ' + str(carLocation1[i]) + ' Location2: ' + str(carLocation2[i]) + ' speed is ' + str("%.2f" % round(speed[i], 0)) + ' km/h.\n')
						asma_miktari=format(((speed[i]*100)/yasal_hiz_siniri)-100,".2f")
						
						if speed[i]>=yasal_hiz_siniri:
							# print(speed[i])
							speed2[i]=format(speed[i],".2f")
							speed2[i]=float(speed2[i])
							# print(f"{carID} numarali aracin hizi {speed2[i]} \n % {asma_miktari} hiz sinirini asma tespit edildi")
							# ceza_yiyenler.append(carID)
							# print("*****************",ceza_hesap(asma_miktari),"***********************")
							# ceza_yiyenler2=pd.Series(ceza_yiyenler)
							# ceza_yiyenler2=ceza_yiyenler2.unique()
							# print(ceza_yiyenler2)
							ceza_tutar=ceza_hesap(asma_miktari,hizsiniriasimorani,cezaorani)
							
# ********************************************************************************************************************************************
							# print(type(ceza_tutar))
							# if isinstance(ceza_tutar,float):
							# 	indirimli_ceza=float(ceza_tutar)*.75
							
# ********************************************************************************************************************************************
							
							hesaplanan_asma=asim_hesaplama(asma_miktari,hizsiniriasimorani)
							# asma_miktari2.append(asma_miktari)
							# print(pd.Series(asma_miktari2).unique())
							# ceza_tutar1.append(ceza_tutar)
							# ceza_tutar2=pd.Series(ceza_tutar1).unique()
							# print(ceza_tutar2)
							# indirimli_ceza2.append(indirimli_ceza)
							# print(pd.Series(indirimli_ceza2).unique())
							# hesaplanan_asma1.append(hesaplanan_asma)
							# hesaplanan_asma2=pd.Series(hesaplanan_asma1).unique()
							# hesaplanan_asma2.append(hesaplanan_asma)
							# print(pd.Series(hesaplanan_asma2).unique())
							# print(hesaplanan_asma2)
							# mail(carID,speed2[i],asma_miktari,ceza_tutar,hesaplanan_asma)
			# continue		
							
						# break
							if carID and speed2 and asma_miktari and ceza_tutar and hesaplanan_asma!=None:
								my_dict=dict(carID=carID,speed2=speed2[i],asma=asma_miktari,ceza_tutar=ceza_tutar,hesaplanan_asma=hesaplanan_asma)
								cezalar=pd.Series(my_dict)
								# print(cezalar)
								cezalar2[i]=cezalar
								print(cezalar2)
								cezalar2.to_excel("kayitlarx.xlsx")
								# cezalar.to_excel("kayitlar.xlsx")
								# print(len())
							# print(my_dict)
							# print(carIDtoDelete)
							# for i in range(len(carIDtoDelete)):
							# 	for j in range(len(ceza_yiyenler)):
							# 		if carIDtoDelete[i]==ceza_yiyenler[j]:
							# 			print("******************",i,"Ceza yedi")
							# 			continue
		cv2.imshow('result', resultImage)
		#Write the frame into the file 'output.avi'
		#out.write(resultImage)


		if cv2.waitKey(33) == 27:
			break

		
	
	cv2.destroyAllWindows()
# print(ceza_yiyenler)
# print(cezalar2)
if __name__ == '__main__':
	trackMultipleObjects()
# print(pd.Series(cezalar2).unique())
# verikayit=pd.read_excel("kayitlar.xlsx")
# verikayit.pop("Unnamed: 0")
# verikayit.columns=["Degerler"]
# verikayit=pd.Series(verikayit["Degerler"]).unique()
# j=list()
# for i in veri:
#     vi=i.split()
#     j.append(vi)
# for i in j:
#     i[0]=i[0].replace("[","")
#     i[-1]=i[-1].replace("]","")
#     print(i)
#     mail(i[0],i[1],i[2],i[3],i[4])
df=pd.read_excel("kayitlarx.xlsx")
df.columns=[i for i in range(len(df.columns))]
df.to_excel("kayitlarx.xlsx")
subprocess.run(["python", "/home/bagergat/Desktop/yeni/mail_sending.py"])