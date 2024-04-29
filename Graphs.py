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
axes[0,0].set_xlabel("Araç ID")
axes[0,0].set_ylabel("Araçların Hızı")
axes[0,0].set_title("Araçların Hız Grafikleri")

axes[0,1].bar([i for i in range(len(np.array(inf.iloc[2])))],np.array(inf.iloc[2]),color="green")
axes[0,1].set_xlabel("Araç ID")
axes[0,1].set_ylabel("Araçların Hızı")
axes[0,1].set_title("Araçların Hız Grafikleri")

axes[1,0].bar([i for i in range(len(np.array(inf.iloc[3])))],np.array(inf.iloc[3]),color="blue")
axes[1,0].set_xlabel("Araç ID")
axes[1,0].set_ylabel("Araçların Hızı")
axes[1,0].set_title("Araçların Hız Grafikleri")

axes[1,1].bar([i for i in range(len(np.array(inf.iloc[4])))],np.array(inf.iloc[4]),color="yellow")
axes[1,1].set_xlabel("Araç ID")
axes[1,1].set_ylabel("Araçların Hızı")
axes[1,1].set_title("Araçların Hız Grafikleri")
plt.show(block=True)

fig.savefig("SavedGraph.pdf")