from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

#plt.figure(1) # For the case before any tuning
#dumpx = np.array(range(588,588+349))
#storedx = np.array(range(349,588+349))
#purex = np.array(range(349,666))
#plt.plot(dumpx,((588*6.23)+((dumpx-588)*26))/(dumpx),label='dump')
#plt.plot(storedx,((349*26)+((storedx-349)*6.23))/(storedx),label='stored')
#plt.plot(purex,((666*20)+((purex-666)*100))/(purex),label='add pure')
#plt.plot(dumpx,((588*6.23)+((dumpx-588)*100))/(dumpx),label='dump')
#plt.plot([300,1050],[20,20],'--',color='black')
#plt.plot([666,666],[0,100],'--',color='black')
#plt.plot(666,20,'.',color='black')

#plt.figure(1) # After removing as much dilute mix and adding as much concentrated mix as possible 180423
#dumpx = np.array(range(330,666))
#purex = np.array(range(349,666))
#plt.plot(dumpx,(((232.7*26)+((dumpx-232.7)*6.23))/dumpx),label='dump')
#plt.plot(purex,(((666*20)+((purex-666)*100))/purex),label='add pure')
#plt.plot([300,1050],[20,20],'--',color='black')
#plt.plot([666,666],[0,100],'--',color='black')
#plt.plot(666,20,'.',color='black')

#plt.figure(1) # After removing as much dilute mix and adding as much concentrated mix as possible, then adding back some dilute mix 180425
#dumpx = np.array(range(614,667))
#purex = np.array(range(617,667))
#purex2 = np.array(range(614,667))
#plt.plot(dumpx,(((232.7*26)+((dumpx-232.7)*6.23))/dumpx),label='add 6.23%')
#plt.plot(purex,(((666*20)+((purex-666)*100))/purex),label='add 100%')
#plt.plot(purex2,(((232.7*26)+((614.3-232.7)*6.23)+((purex2-614.3)*100))/purex2),label='add 100%')
#plt.plot([300,1050],[20,20],'--',color='black')
#plt.plot([666,666],[0,100],'--',color='black')
#plt.plot(614.3,(((232.7*26)+((614.3-232.7)*6.23))/614.3),'.',color='black')
#plt.plot(666,20,'.',color='black')

#plt.figure(1) # After removing as much dilute mix and adding as much concentrated mix as possible, then adding back some dilute mix twice 180427
#dumpx = np.array(range(617,667))
#purex = np.array(range(617,667))
#purex2 = np.array(range(617,667))
#plt.plot(617.5,(((232.7*26)+((617.5-232.7)*6.23))/617.5),'s',color='black',label="current")
#plt.plot(dumpx,(((232.7*26)+((dumpx-232.7)*6.23))/dumpx),label='current add 6.23%')
#plt.plot(purex2,(((232.7*26)+((617.5-232.7)*6.23)+((purex2-617.5)*100))/purex2),label='current add 100%')
#plt.plot(purex,(((666*20)+((purex-666)*100))/purex),label='target subtract 100%')
#plt.plot([300,1050],[20,20],'--',color='black')
#plt.plot([666,666],[0,100],'--',color='black')
#plt.plot(666,20,'*',color='black',label="target")
#plt.plot(617.5,(((232.7*26)+((617.5-232.7)*6.23))/617.5),'s',color='black')

plt.figure(1) # After removing as much dilute mix and adding as much concentrated mix as possible, then adding back some dilute mix twice, then adding pure mix 180509
dumpx = np.array(range(665,668))
purex = np.array(range(665,668))
purex2 = np.array(range(665,668))
plt.plot(665.8,(((232.7*26)+((617.5-232.7)*6.23)+((665.8-617.5)*100))/665.8),'s',color='black',label="current")
plt.plot(dumpx,(((232.7*26)+(((617.5-232.7)+(dumpx-665.8))*6.23)+((665.8-617.5)*100))/dumpx),label='current add 6.23%')
plt.plot(purex2,(((232.7*26)+((617.5-232.7)*6.23)+((purex2-617.5)*100))/purex2),label='current add 100%')
plt.plot(purex,(((666*20)+((purex-666)*100))/purex),label='target subtract 100%')
plt.plot([300,1050],[20,20],'--',color='black')
plt.plot([666,666],[0,100],'--',color='black')
plt.plot(666,20,'*',color='black',label="target")
plt.plot(665.8,(((232.7*26)+((617.5-232.7)*6.23)+((665.8-617.5)*100))/665.8),'s',color='black')

plt.xlim(664,668)
plt.ylim(19.5,20.5)
plt.xlabel('total mix [mbar in 15L]')
plt.ylabel('mix ratio [%]')
plt.legend(loc='best')

plt.show()
