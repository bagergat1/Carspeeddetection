import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

inf=pd.read_excel("kayitlarx.xlsx")
inf.pop("Unnamed: 0")
inf.drop(0,axis=1,inplace=True)



fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 12))
fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
plt.subplots_adjust(hspace=0.2, wspace=0.2)
axes[0,0].bar([i for i in range(len(np.array(inf.iloc[1])))],np.array(inf.iloc[1]),color="red")
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

plt.show(block=True)

fig.savefig("SavedGraph.pdf")