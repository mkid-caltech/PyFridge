import numpy as np
import matplotlib.pyplot as plt

def data_180724():
    manual_0 = np.array([[22.5,0]])
    manual_5 = np.array([[32,2],[38,5],[47,10],[72.3,20],[100,44]])
    fridge_0 = np.array([[39.5,0],[61.3,2],[78.6,5],[96.6,10],[121.9,20],[160.6,44]])
    fridge_2 = np.array([[43.1,0],[61.9,2],[78,5],[95.6,10],[118.6,20],[153.8,44]])
    fridge_5 = np.array([[45.2,0],[63.7,2],[79,5],[95.7,10],[118.2,20],[151.8,44]])
    fridge_6 = np.array([[46.7,0],[64.1,2],[79.8,5],[97.1,10],[121.0,20],[139.3,30],[159.2,44]])

    manual_5_p = np.polyfit(manual_5[:,0]**2,manual_5[:,1],1)
    fridge_0_p = np.polyfit(fridge_0[:,0]**2,fridge_0[:,1],1)
    fridge_2_p = np.polyfit(fridge_2[:,0]**2,fridge_2[:,1],1)
    fridge_5_p = np.polyfit(fridge_5[:,0]**2,fridge_5[:,1],1)
    fridge_6_p = np.polyfit(fridge_6[:,0]**2,fridge_6[:,1],1)

    plt.figure(1)

    plt.plot(manual_0[:,0]**2,manual_0[:,1],'*',label='manual 0 mW still',c='blue')
    plt.plot(manual_5[:,0]**2,manual_5[:,1],'*',label='manual 5 mW still',c='red')
    plt.plot(manual_5[:,0]**2,manual_5_p[1]+manual_5_p[0]*(manual_5[:,0]**2),c='red', label=str(manual_5_p[0]*1e3)+' $mW/K^{2}$')
    plt.plot(fridge_0[:,0]**2,fridge_0[:,1],'.',label='July fridge 0 mW still',c='blue')
    plt.plot(fridge_0[:,0]**2,fridge_0_p[1]+fridge_0_p[0]*(fridge_0[:,0]**2),c='blue', label=str(fridge_0_p[0]*1e3)+' $mW/K^{2}$')
    plt.plot(fridge_2[:,0]**2,fridge_2[:,1],'.',label='July fridge 2 mW still',c='green')
    plt.plot(fridge_2[:,0]**2,fridge_2_p[1]+fridge_2_p[0]*(fridge_2[:,0]**2),c='green', label=str(fridge_2_p[0]*1e3)+' $mW/K^{2}$')
    plt.plot(fridge_5[:,0]**2,fridge_5[:,1],'.',label='July fridge 5 mW still',c='red')
    plt.plot(fridge_5[:,0]**2,fridge_5_p[1]+fridge_5_p[0]*(fridge_5[:,0]**2),c='red', label=str(fridge_5_p[0]*1e3)+' $mW/K^{2}$')
    plt.plot(fridge_6[:,0]**2,fridge_6[:,1],'.',label='recent fridge 2 mW still (HEMT 1 on)',c='black')
    plt.plot(fridge_6[:,0]**2,fridge_6_p[1]+fridge_6_p[0]*(fridge_6[:,0]**2),c='black', label=str(fridge_6_p[0]*1e3)+' $mW/K^{2}$', linewidth=3)

    plt.legend(loc='best',fancybox=True)
    temps2 = [0,5000,10000,15000,20000,25000]
    temps = []
    for squared in temps2:
        temps = temps + ["%.2f" % np.sqrt(squared)]
    plt.xticks(temps2,temps)
    plt.yticks([0,2,5,10,20,44])
    plt.axhline(y=0, c='k', ls='--', zorder=0)
    plt.axvline(x=0, c='k', ls='--', zorder=0)
    #plt.ylim(0,50)
    plt.xlabel('MC Temperature [mK]')
    plt.ylabel('MC Heater/Cooling Power [$\mu$W]')
    plt.show()

if __name__ == "__main__":
    data_180724()
