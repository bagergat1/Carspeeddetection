import pandas as pd
import numpy as np
def ceza_hesap(asma_miktari):
    
    veri=pd.read_excel("Hiz_ceza_son.xlsx")
    veri.drop(columns=["Unnamed: 0"],axis=1,inplace=True)
    i=0
    j=len(veri["Hız Sınırı Aşım Oranı"])
    while True:
        veri["Ceza Tutarı"][i]=veri["Ceza Tutarı"][i].replace(".","")
        veri["Ceza Tutarı"][i]=veri["Ceza Tutarı"][i].replace(",",".")
        veri["Hız Sınırı Aşım Oranı"][i]=float(veri["Hız Sınırı Aşım Oranı"][i].replace("%",""))
        veri["Ceza Tutarı"][i]=float(veri["Ceza Tutarı"][i])
        i+=1
        if i==len(veri):
            break
    while True:
        if veri["Hız Sınırı Aşım Oranı"][j]>=asma_miktari:
            return veri["Hız Sınırı Aşım Oranı"][j]

