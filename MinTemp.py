import numpy as np
import matplotlib.pyplot as plt

def data_180724():
    stillpower = np.array([0,0,0.5,1,1,2,2,3.5,5])
    basetemp = np.array([40.6,37.2,40.2,41.2,40.9,42.0,42.7,44.1,45.4])
    singleshottemp = np.array([39.6,37.5,34.6,35.9,35.5,36.9,38.3,39.8,41.3])

    plt.figure(1)

    plt.plot(stillpower,basetemp,'o',label='base temp',c='blue')
    plt.plot(stillpower,singleshottemp,'o',label='single-shot temp',c='red')

    plt.legend(loc='best',fancybox=True)
    plt.xlabel('Still Power [mW]')
    plt.ylabel('MC Temperature [mK]')
    plt.show()

if __name__ == "__main__":
    data_180724()
