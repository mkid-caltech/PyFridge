from matplotlib import pyplot as plt
from matplotlib import animation
#import sys
import time
#import os
import numpy as np

from devices.Lakeshore_370 import *



LS=Lakeshore_370("LS370")

dt = 1
StartTime = time.localtime(time.time())
StartDay = StartTime.tm_mday

#PrevTimeStamp = -1

time_0 = np.arange(-3600,0,dt)
T_plot = time_0*0. #1 hr, in mK
fig = plt.figure()
plt.axes()
ax = plt.subplot(111)
line1, = ax.plot([],[])
#fig = plt.figure()
#ax = fig.add_subplot(111)
#line1, = ax.plot(T_plot)

def init():
	line1.set_data(time_0,T_plot)
	return line1

def animate(i):
	R_MC = LS.get_Rval()
	T_MC = LS.get_T()
	T_plot = T_plot[1:]+[T_MC*1000.]
	line1.set_data(time_0,T_plot)
	return line1

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=WideNum, interval=1000, blit=True)
plt.show()

#while 1:
#
#	try:
#		R_MC = LS.get_Rval()
#
#		T_MC = LS.get_T()
#
#		timer = time.time()
#		LocalTime = time.localtime(timer)
#		TimeStamp = ((LocalTime.tm_mday-StartDay)*24+LocalTime.tm_hour*60+LocalTime.tm_min)*60+LocalTime.tm_sec
#		if TimeStamp%dt == 0 and TimeStamp != PrevTimeStamp:
#			#LogFile.write("%i, %f\n"%(TimeStamp,R_still))
#			if T_MC>0.5:
#				print "\r%i sec\t%.4f Ohm\t%.4f K\tpress <ctrl+c> to stop"%(TimeStamp,R_MC,T_MC),
#			else:
#				print "\r%i sec\t%.4f Ohm\t%.4f mK\tpress <ctrl+c> to stop"%(TimeStamp,R_MC,T_MC*1000.),
#			PrevTimeStamp = TimeStamp
#
#			T_plot = T_plot[1:]+[T_MC*1000.]
#			line1.set_ydata(T_plot)
#			#ax.set_ylim(np.min(T_plot),np.max(T_plot))
#			fig.canvas.draw()
#			plt.pause(1.e-10)
#
#
#		time.sleep(dt/2.)
#
#	except KeyboardInterrupt:
#		break

	#plt.close()
