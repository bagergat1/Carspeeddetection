import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def main():
    # Ana pencere oluştur
    root = tk.Tk()
    root.withdraw()  # Ana pencereyi gizle

    # Ekranın genişliği ve yüksekliği
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Küçük pencere boyutları ve konumu (sağ tarafta)
    small_window_width = int(screen_width * 0.2)
    small_window_height = screen_height
    small_window_x = screen_width - small_window_width
    small_window_y = 0

    # Küçük pencere oluştur
    small_window = tk.Toplevel(root)
    small_window.geometry(f"{small_window_width}x{small_window_height}+{small_window_x}+{small_window_y}")
    # Küçük pencere içine grafik çiz
    fig, ax = plt.subplots()
    ax.bar([i for i in range(len(np.array(inf.iloc[1])))],np.array(inf.iloc[1]),color="red")  # Örnek veri
    ax.set_title('Grafik Başlığı')
    ax.set_xlabel('X Ekseni')
    ax.set_ylabel('Y Ekseni')

    # Matplotlib figürünü Tkinter penceresine göm
    canvas = FigureCanvasTkAgg(fig, master=small_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=tk.YES)

    # Ana pencereyi göster
    root.mainloop()

inf=pd.read_excel("kayitlarx.xlsx")
inf.pop("Unnamed: 0")
# inf.drop(0,axis=1,inplace=True)
main()
















# ************************************************************************************************


def main(inf):
    # Ana pencere oluştur
    root = tk.Tk()
    root.withdraw()  # Ana pencereyi gizle

    # Ekranın genişliği ve yüksekliği
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Küçük pencere boyutları ve konumu (sağ tarafta)
    small_window_width = int(screen_width * 0.2)
    small_window_height = screen_height
    small_window_x = screen_width - small_window_width
    small_window_y = 0

    # Küçük pencere oluştur
    small_window = tk.Toplevel(root)
    small_window.geometry(f"{small_window_width}x{small_window_height}+{small_window_x}+{small_window_y}")
    # Küçük pencere içine grafik çiz
    fig, ax = plt.subplots()
    ax.bar([i for i in range(len(np.array(inf.iloc[1])))],np.array(inf.iloc[1]),color="red")  # Örnek veri
    ax.set_title('Grafik Başlığı')
    ax.set_xlabel('X Ekseni')
    ax.set_ylabel('Y Ekseni')

    # Matplotlib figürünü Tkinter penceresine göm
    canvas = FigureCanvasTkAgg(fig, master=small_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=tk.YES)

    # Ana pencereyi göster
    root.mainloop()



# ************************************************************************************************

import time
simdi=time.time()
while True:
    simdi2=time.time()
    if simdi2-simdi==60:
        main()