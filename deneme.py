import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
from datetime import datetime
simdi=datetime.now()
def create_graph(inf,simdi):
    root = tk.Tk()
    root.withdraw()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    small_window_width = int(screen_width * 0.2)
    small_window_height = screen_height
    small_window_x = screen_width - small_window_width
    small_window_y = 0

    small_window = tk.Toplevel(root)
    small_window.geometry(f"{small_window_width}x{small_window_height}+{small_window_x}+{small_window_y}")
    fig, ax = plt.subplots()
    ax.bar([i for i in range(len(np.array(inf.iloc[1])))], np.array(inf.iloc[1]), color="red")
    ax.set_title('Grafik Başlığı')
    ax.set_xlabel('X Ekseni')
    ax.set_ylabel('Y Ekseni')

    canvas = FigureCanvasTkAgg(fig, master=small_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=tk.YES)

    def close_window():
        small_window.destroy()
        root.destroy() 
    simdi2=datetime.now()
    if simdi2.minute-simdi.minute==1:
        close_window()
    # root.after(55000, close_window)
    root.mainloop()
# simdi=datetime.now()
x=1
print(f"{x}. grafik olusturuldu")
inf=pd.read_excel("kayitlarx.xlsx")
inf.pop("Unnamed: 0")
inf.pop(0)
inf.to_excel("graphsperminute.xlsx")
inf = pd.read_excel("graphsperminute.xlsx")
create_graph(inf,simdi)
x+=1