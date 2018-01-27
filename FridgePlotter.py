import sys
import numpy as np
import matplotlib.pyplot as plt
from RX202A_Convert import Thermiator
import seaborn as sns

sns.set_palette(sns.hls_palette(13, h=.5))

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
        for i in range(len(data2[1:,0])):
            if data2[i+1,0] < data2[i,0]:
                data2[i+1,0] = data2[i+1,0] + 86400 # added to help deal with the day changing

    data1_reverse = data1[::-1,12]
    min_temp = len(data1_reverse) - np.argmin(data1_reverse) - 1

    plt.figure(1)
    plt.title(fname1)

    plt.plot(data1[:,0],data1[:,1], label="G1 [mBar]")
    plt.plot(data1[min_temp,0],data1[min_temp,1],"r*")
    plt.plot(data1[:,0],data1[:,2], label="G2 [mBar]")
    plt.plot(data1[min_temp,0],data1[min_temp,2],"r*", label="Lowest MC")
    #plt.plot(data1[:,0],data1[:,3], label="G3 [mBar]")
    plt.plot(data1[:,0],data1[:,4], label="P1 [mBar]")
    plt.plot(data1[min_temp,0],data1[min_temp,4],"r*")
    plt.plot(data1[:,0],data1[:,5], label="P2 [mBar]")
    #plt.plot(data1[:,0],data1[:,6],"--", label="MC Heater [uW]")
    plt.plot(data1[:,0],100*data1[:,7],"--", label="Still Heater [mW]")
    #plt.plot(data1[:,0],data1[:,8],"--", label="Sorb Heater [mW]")
    plt.plot(data1[:,0],data1[:,9], label="V12a [%]")
    plt.plot(data1[:,0],data1[:,10], label="V6 [%]")
    #plt.plot(data1[:,0],data1[:,11], label="V1K [%]")
    plt.plot(data1[:,0],data1[:,12], label="MC Temp [K]")
    plt.plot(data1[min_temp,0],data1[min_temp,12],"r*")
    plt.plot(data1[:,0],data1[:,13], label="1K Pot Temp [K]")
    #plt.plot(data1[:,0],data1[:,14], label="Sorb Temp [K]")
    if fname2:
        plt.plot(data2[:,0],Thermiator(data2[:,1]), label="Still Temp [K]")


    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv)>2:
        whole(sys.argv[1],sys.argv[2])
    else:
        whole(sys.argv[1])
