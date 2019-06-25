import numpy as np
import matplotlib.pyplot as plt

still1 = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5])
LS1 = np.array([58.62, 53.67, 52.14, 49.97, 50.29, 48.74, 47.88, 47.89, 48.23, 48.54])
IGH1 = np.array([61.5, 55.8, 54.1, 51.8, 51.9, 50.3, 49.1, 49.3, 49.8, 50.1])
LS_or_IGH_err1 = np.array([0, 0, 0, 0, 1, 0.05, 0, 0, 0, 0])

still2 = np.array([0, 0.5, 1, 1.5, 2, 2.5])
LS2 = np.array([49.00, 48.30, 43.32, 44.40, 45.06, 45.87])
IGH2 = np.array([50.6, 50.2, 44.4, 45.5, 46.3, 47.0])
LS_or_IGH_err2 = np.array([1.8, 2, 0, 0, 0, 0])

plt.figure()
plt.errorbar(still1,LS1, yerr=LS_or_IGH_err1*0.5)
#plt.errorbar(still1,IGH1)
plt.errorbar(still2,LS2, yerr=LS_or_IGH_err2*0.5)
#plt.errorbar(still2,IGH2)
plt.show()
