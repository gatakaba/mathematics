import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 40,20

t=np.linspace(0,60,1000)
x=np.sin(2*np.pi*0.05*t)*np.sin(2*np.pi*t)
t2=np.linspace(0,20,int(1000/3))
y1=np.sin(2*np.pi*t2)*np.sin(2*np.pi*0.05*t2)*.5
y2=np.sin(2*np.pi*t2*0.5)*np.sin(2*np.pi*0.05*t2)*.5
y3=np.sin(2*np.pi*t2)*np.sin(2*np.pi*0.05*t2)*.5
y=np.r_[y1,y2,y3]
z=np.sin(2*np.pi*0.05*t)*np.sin(2*np.pi*t)

plt.plot(np.r_[x,y,z])
#plt.plot(np.sin(2*np.pi*2*0.1*(t-1))*0.5+0.5)

#plt.plot(-np.sin(2*np.pi*2*0.1*(t-1))*0.5-0.5)
