import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime
simdi=datetime.now() 
file="./graphsperminute.xlsx"
x=1
while True:
    import mailattachmentdownloader
    while file in os.listdir():
        # verison=veri.columns[-1]
        # eskiveri=veri[veri.columns[0:verison]]
        # veri.drop(eskiveri,axis=1,inplace=True)
        simdi2=datetime.now()
        if simdi2.minute-simdi.minute==1*x:
            import graphsperminute
            x+=1
            os.remove(file)





        