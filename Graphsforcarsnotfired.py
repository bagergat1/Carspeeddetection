import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from yasal_hiz_siniri import yasal_hiz_siniri
inf=pd.read_excel("ceza_almayan_araclar.xlsx")
inf.pop("Unnamed: 0")

betw=dict()
liste=list()
def countme(veri,x,y):
    for i in veri:
        if i-x<10 and i-x>=0:
            y+=1
            key="{x}-{u}".format(x=x,u=x+10)
            betw[key]=y
    liste.append(betw)

betw=dict()
y=0
x=30
while True:
    countme(inf[0],x,y)
    x+=10
    if yasal_hiz_siniri>=y:
        break
# print(liste)
liste2=list()
liste3=list()
for i in liste:
    a=i.keys()
    a=str(a)
    a=a.split("'")
    liste2.append(a[1])
    b=i.values()
    b=str(b)
    b=b.split("[")[1]
    b=int(b.split("]")[0])
    liste3.append(b)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 3))
fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
plt.subplots_adjust(hspace=0.2, wspace=0.2)

plt.subplot(1,2,2)
plt.pie(liste3,labels=liste2)
plt.subplot(1,2,1)
plt.bar([i for i in range(len(np.array(inf[0])))],np.array(inf[0]),color="red")
plt.show()
plt.savefig("Ceza_almayanlar.pdf")