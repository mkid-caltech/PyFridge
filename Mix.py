from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
dumpx = np.array(range(588,588+349))
storedx = np.array(range(349,588+349))
purex = np.array(range(349,666))
plt.plot(dumpx,((588*6.23)+((dumpx-588)*26))/(dumpx),label='dump')
plt.plot(storedx,((349*26)+((storedx-349)*6.23))/(storedx),label='stored')
plt.plot(purex,((666*20)+((purex-666)*100))/(purex),label='add pure')
plt.plot(dumpx,((588*6.23)+((dumpx-588)*100))/(dumpx),label='dump')
plt.plot([300,1050],[20,20],'--',color='black')
plt.plot([666,666],[0,100],'--',color='black')
plt.plot(666,20,'.',color='black')

plt.legend()
plt.xlim(350,1000)
plt.ylim(0,30)
plt.xlabel('total mix [mbar in 15L]')
plt.ylabel('mix ratio [%]')

plt.show()
