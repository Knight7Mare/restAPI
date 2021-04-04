import matplotlib
matplotlib.use('WebAgg')
matplotlib.rcParams["webagg.address"]="0.0.0.0"
import matplotlib.pyplot as plt,mpld3
import matplotlib.dates as md
import matplotlib.animation as animation
import time
import numpy as np
from datetime import datetime
import pandas as pd
import psycopg2
xfmt = md.DateFormatter('%H:%M:%S')

def get_arr(mycol,method):
    now = time.time()
    #print("now:",now)
    #print(datetime.fromtimestamp(now).strftime('%H:%M:%S'))
    mycol.execute("SELECT * FROM cekilenler where method=  %s AND timestamp > %s" ,(method,str(int(now-3600))))
    logs = mycol.fetchall()
    arr1=[]
    arr2=[]
    date_time=[]
    for i in logs:
        
        tmstp=int(i[1])-(now-3600)
        date_time.append(pd.to_datetime(datetime.fromtimestamp(i[1])))
        arr1.append(tmstp)
        arr2.append(float(i[2]))
    #print(date_time)
    date_time = pd.to_datetime(date_time)
    #print(date_time)
    #exit()
    DF = pd.DataFrame()
    DF['delay'] = arr2
    DF = DF.set_index(date_time)
    
    #print(DF)
    return DF
conn = psycopg2.connect(dbname='restfulapiDB',user='postgres', password='omer', host='postgredb')
mycol = conn.cursor()

getDF=get_arr(mycol,"GET")
postDF=get_arr(mycol,"POST")
putDF=get_arr(mycol,"PUT")
delDF=get_arr(mycol,"DELETE")
fig1 = plt.figure(figsize=[12, 4.8])
ax1 = fig1.add_subplot(1,1,1)
ax1.xaxis.set_major_formatter(xfmt)
plt.xlabel('adet')
plt.ylabel('saat')
plt.title('Metodlar')
plt.axis([0, 60, 0, 3000])
ax1.plot(getDF,drawstyle="steps",linewidth=1,label="get method")   
ax1.plot(postDF,drawstyle="steps",linewidth=1,label="post method") 
ax1.plot(putDF,drawstyle="steps",linewidth=1,label="put method") 
ax1.plot(delDF,drawstyle="steps",linewidth=1,label="delete method")  
ax1.legend()
#plt.plot(arr2)
def animate(i):
    getDF=get_arr(mycol,"GET")
    postDF=get_arr(mycol,"POST")
    putDF=get_arr(mycol,"PUT")
    delDF=get_arr(mycol,"DELETE")
    
   
    ax1.clear()
    ax1.plot(getDF,drawstyle="steps",linewidth=1,label="get method")   
    ax1.plot(postDF,drawstyle="steps",linewidth=1,label="post method") 
    ax1.plot(putDF,drawstyle="steps",linewidth=1,label="put method") 
    ax1.plot(delDF,drawstyle="steps",linewidth=1,label="delete method")   
    ax1.legend()
    
ani = animation.FuncAnimation(fig1,animate,interval=2000 )
plt.show()
