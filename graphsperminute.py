import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
from datetime import datetime
import os
import shutil
move="/home/bagergat/Desktop/Bitirme/used_files/"
file="yenikayit.xlsx"


def create_graph(inf):
    root = tk.Tk()
    root.withdraw()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    small_window_width = int(screen_width * 1)
    small_window_height = screen_height
    small_window_x = screen_width - small_window_width
    small_window_y = 0

    small_window = tk.Toplevel(root)
    small_window.geometry(f"{small_window_width}x{small_window_height}+{small_window_x}+{small_window_y}")
    # fig, ax = plt.subplots()
    # ax.bar([i for i in range(len(np.array(inf.iloc[1])))], np.array(inf.iloc[1]), color="red")
    # ax.set_title('Grafik Başlığı')
    # ax.set_xlabel('X Ekseni')
    # ax.set_ylabel('Y Ekseni')

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 12))
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    plt.subplots_adjust(hspace=0.2, wspace=0.2)
    axes[0,0].bar([i for i in range(len(np.array(inf.iloc[2])))],np.array(inf.iloc[1]),color="red")
    axes[0,0].set_xlabel("Araç No")
    axes[0,0].set_ylabel("Araçların Hızı")
    axes[0,0].set_title("Araçların Hız Grafikleri")
    
    axes[0,1].bar([i for i in range(len(np.array(inf.iloc[2])))],np.array(inf.iloc[2]),color="green")
    axes[0,1].set_xlabel("Araç No")
    axes[0,1].set_ylabel("Aşma oranı")
    axes[0,1].set_title("Araçların Yasal Hız Sınırını Aşma Oranı")
    fig
    axes[1,0].bar([i for i in range(len(np.array(inf.iloc[3])))],np.array(inf.iloc[3]),color="brown")
    axes[1,0].set_xlabel("Araç No")
    axes[1,0].set_ylabel("Ceza Tutarı")
    axes[1,0].set_title("Araçlara Kesilen Ceza Tutarı")
    
    fiftyper=0
    thirtyper=0
    tenper=0
    for i in np.array(inf.loc[4]):
        if i==50:
            fiftyper+=1
        elif i==30:
            thirtyper+=1
        elif i==10:
            tenper+=1
    mylabels = ["%50 aşım sayısı","%30 aşım sayısı","%10 aşım sayısı"]
    axes[1,1].pie([fiftyper,thirtyper,tenper],labels=mylabels,colors=["red","orange","blue"])

    canvas = FigureCanvasTkAgg(fig, master=small_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=tk.YES)

    def close_window():
        small_window.destroy()
        root.destroy()  # Add this line to terminate the loop

    # Close the window after 45 seconds
    # if file:
        # os.remove(f"{move}"+"graphsperminute.xlsx")
        # shutil.move(f"{file}",f"{move}")
        
    root.after(55000, close_window)
    root.mainloop()
# simdi=datetime.now()
# x=1
# file="/home/bagergat/Desktop/graphsperminute.xlsx"
# while True:
#     # while file not in os.listdir("/home/bagergat/Desktop/"):
#     import mailattachmentdownloader
#         # break
#     # inf=pd.read_excel("./kayitlarx.xlsx")
#     create_graph(data)
    
    
    # x+=1
    # os.remove(file)
    # print("2.döngü")
# while True:
#     # import mailattachmentdownloader
#     simdi2=datetime.now()
    # if simdi2.minute-simdi.minute==x:
        # print(f"{x}. grafik olusturuldu")
        
        # inf.pop("Unnamed: 0")
        # inf.pop(0)
        # inf.to_excel("./graphsperminute.xlsx")
        # inf = pd.read_excel("./graphsperminute.xlsx")

if __name__=="__main__":
    while True:
        if file in move:
            print("evet")
            break
        else:
            import mailattachmentdownloader
            data=pd.read_excel("./used_files/yenikayit.xlsx")
            # data.drop(0,axis=1,inplace=True)
            data.drop("Unnamed: 0",axis=1,inplace=True)
            create_graph(data)
            
# file="/home/bagergat/Desktop/graphsperminute.xlsx"
# data=pd.read_excel("./used_files/yenikayit.xlsx")
# data.drop(0,axis=1,inplace=True)
# data.drop("Unnamed: 0",axis=1,inplace=True)
# data.to_excel("/home/bagergat/Desktop/graphsperminute.xlsx")
# print(type(inf))