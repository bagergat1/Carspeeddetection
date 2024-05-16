import cv2



yasal_hiz_siniri=35
pixel1=200
pixel2=205
video_dosyasi="./ofis.mp4"
video = cv2.VideoCapture(video_dosyasi)
name=video_dosyasi.split("/")
name=name[-1]
if name =="ofis.mp4":
    crop_box = (0, 100, 800, 600) 
else:
    crop_box = (300, 100, 1100, 800) 