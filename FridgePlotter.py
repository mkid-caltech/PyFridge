import sys
import numpy as np
import matplotlib.pyplot as plt
from RX202A_Convert import Thermiator

def whole(fname1, fname2=False):
    """
    "whole" plots IGH and SRS bridge data for the whole run
    Input parameters:
        fname1: string name of the IGH file
        fname2: string name of the SRS file (may have to delete the last line in fname2 if it is a string)

    Returns:
        plot of all uncommented data
    """
    data1 = np.loadtxt(fname1, skiprows=6)
    if fname2:
        data2 = np.loadtxt(fname2, delimiter=',')
        for i in range(len(data2[:,0])):
            if data2[i,0] < data2[0,0]:
                data2[i,0] = data2[i,0] + 86400 # added to help deal with the day changing

    plt.figure(1)

    plt.plot(data1[:,0],data1[:,1], label="G1 [mBar]")
    plt.plot(data1[np.argmin(data1[:,12]),0],data1[np.argmin(data1[:,12]),1],"*")
    plt.plot(data1[:,0],data1[:,2], label="G2 [mBar]")
    plt.plot(data1[np.argmin(data1[:,12]),0],data1[np.argmin(data1[:,12]),2],"*", label="3He [mbar]")
    plt.plot(data1[:,0],data1[:,3], label="G3 [mBar]")
    plt.plot(data1[:,0],data1[:,4], label="P1 [mBar]")
    plt.plot(data1[np.argmin(data1[:,12]),0],data1[np.argmin(data1[:,12]),4],"*")
    plt.plot(data1[:,0],data1[:,5], label="P2 [mBar]")
    plt.plot(data1[:,0],data1[:,6],"--", label="MC Heater [uW]")
    plt.plot(data1[:,0],data1[:,7],"--", label="Still Heater [mW]")
    plt.plot(data1[:,0],data1[:,8],"--", label="Sorb Heater [mW]")
    plt.plot(data1[:,0],data1[:,9],"-", label="V12a [%]")
    plt.plot(data1[:,0],data1[:,10],"-", label="V6 [%]")
    plt.plot(data1[:,0],data1[:,11],"-", label="V1K [%]")
    plt.plot(data1[:,0],data1[:,12], label="MC Temp [K]")
    plt.plot(data1[np.argmin(data1[:,12]),0],data1[np.argmin(data1[:,12]),12],"*")
    plt.plot(data1[:,0],data1[:,13], label="1K Pot Temp [K]")
    plt.plot(data1[:,0],data1[:,14], label="Sorb Temp [K]")
    if fname2:
        plt.plot(data2[:,0],Thermiator(data2[:,1]), label="Still Temp [K]")


    plt.grid(True)
    plt.legend()
    plt.show()

    #plt.axvline(data1[np.argmin(data1[:,12]),0])
    #ax1 = plt.subplot(4,1,1)
    #plt.subplot(4,1,2,sharex=ax1)
    #plt.legend()
    #plt.subplot(4,1,3,sharex=ax1)
    #plt.grid(True)
    #plt.legend()
    #plt.subplot(4,1,4,sharex=ax1)
    #plt.grid(True)
    #plt.legend()
    #plt.plot(data1[np.argmin(data1[:,12]),0],min(data1[:,12]),"*", label="Lowest MC Temp [K]")

if __name__ == "__main__":
    if len(sys.argv)>2:
        whole(sys.argv[1],sys.argv[2])
    else:
        whole(sys.argv[1])
