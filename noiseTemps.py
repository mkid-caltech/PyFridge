from __future__ import division
import numpy as np

def gain(dB):
    return 10**(dB/10)

def atten_Teff(T,dB):
    G = gain(dB)
    return T*((1/G)-1)

def T_out_MC2(attens):
    attens = np.array(attens)

    noises = np.array([300])

    for val,temp in attens:
        noises = np.append(noises,atten_Teff(temp,val))
        noises *= gain(val)

    print noises
    for val in noises:
        print str(round(100*val/noises.sum()))+' % ',
    print ''
    print noises.sum()

    return noises

print 'Channel #1'
T_out_MC2([[-20,4]])
print ''

print 'Channel #2'
T_out_MC2([[-20,4],[-10,1],[-10,0.05],[-1,0.05]])
print ''

print 'Channel #2'
T_out_MC2([[-20,4],[-10,1],[-10,1],[-1,1]])
print ''

print 'Channel #2'
T_out_MC2([[-20,4],[-10,4],[-10,4],[-1,4]])
print ''
