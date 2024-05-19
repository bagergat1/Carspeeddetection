# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from yasal_hiz_siniri import yasal_hiz_siniri
# inf=pd.read_excel("ceza_almayan_araclar.xlsx")
# inf.pop("Unnamed: 0")

# betw=dict()
# liste=list()
# def countme(veri,x,y):
#     for i in veri:
#         if i-x<10 and i-x>=0:
#             y+=1
#             key="{x}-{u}".format(x=x,u=x+10)
#             betw[key]=y
#     liste.append(betw)

# betw=dict()
# y=0
# x=30
# while True:
#     countme(inf[0],x,y)
#     x+=10
#     if yasal_hiz_siniri>=y:
#         break
# # print(liste)
# liste2=list()
# liste3=list()
# for i in liste:
#     a=i.keys()
#     a=str(a)
#     a=a.split("'")
#     # *****************************************out of renge
#     liste2.append(a[1])
#     b=i.values()
#     b=str(b)
#     b=b.split("[")[1]
#     b=int(b.split("]")[0])
#     liste3.append(b)

# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 3))
# fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
# plt.subplots_adjust(hspace=0.2, wspace=0.2)

# plt.subplot(1,2,2)
# plt.pie(liste3,labels=liste2)
# plt.subplot(1,2,1)
# plt.bar([i for i in range(len(np.array(inf[0])))],np.array(inf[0]),color="red")
# plt.show()
# plt.savefig("Ceza_almayanlar.pdf")

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel("./ceza_almayan_araclar.xlsx")
data.drop("Unnamed: 0",inplace=True,axis=1)

data['Group'] = (data[0] + 1) // 10

grouped_df = data.groupby('Group')[0].apply(list).reset_index(name='Grouped_Values')
grouped_df

liste=list()
for i in grouped_df["Grouped_Values"]:
    liste.append(i)
liste3=list();liste2=list()
for i in liste:
    liste3.append(len(i))
    liste2.append(i[0]//10*10)
liste2=[f"{i}-{i+9}" for i in liste2]
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 7))
 # Or equivalently,  "plt.tight_layout()"
plt.subplots_adjust(hspace=0.2, wspace=0.2)
plt.subplot(1,2,2)
plt.pie(liste3,labels=liste2)
plt.title("Hız Aralıklarındaki Araç Sayısı Dairesel Grafiği")
plt.subplot(1,2,1)
plt.barh(liste2,liste3)
# plt.xlim()
plt.xlabel("Bu Hız Aralığındaki Araç Sayısı")
plt.ylabel("Hız Aralıkları")
plt.title("Hız Aralıklarındaki Araç Sayısı Sutun Grafiği")

plt.tight_layout()
plt.savefig("./Ceza_almayanlar.pdf")
plt.show()