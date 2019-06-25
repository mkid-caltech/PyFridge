import numpy as np
import matplotlib.pyplot as plt

R_LakeShore0 = np.array([2244.,2300.,2390.,2579.,2757.,2918.,3112.,3420.,3797.,4366.,6069.,8364.,11420.,23340.,110000.])
T_LakeShore0 = np.array([40.,30.,20.,10.,6.,4.2,3.,2.,1.4,1.,0.5,0.3,0.2,0.1,0.05])
dRdT_LakeShore0 = np.array([-4.58,-6.88,-11.9,-31.6,-66.6,-121.,-218.,-440.,-935.,-2000.,-6791.,-19400.,-49000.,-274000.,-12300000.])

R_LakeShore1 = np.log(R_LakeShore0)
T_LakeShore1 = np.log(T_LakeShore0)
params = np.polyfit((1/R_LakeShore1),T_LakeShore1,6)

'''
plt.figure(1)
plt.xlabel("Resistance")
plt.ylabel("Temperature")
plt.loglog(R_LakeShore0,T_LakeShore0,".",color='black')
R_lin = np.linspace(R_LakeShore0[0],R_LakeShore0[-1],10000)
x = np.log10(R_lin)-2.533
fitM = np.power(10,-3.622+9.067/x-10.516/x/x+5.383/x/x/x)
plt.loglog(R_lin, np.exp(np.polyval(params,(1/np.log(R_lin)))), label="Thermiator")
plt.loglog(R_lin, np.exp(np.polyval([8.81271505E9,-5.37484763E9,1.36122784E9,-1.83220949E8,1.38243782E7,-5.54423089E5,9.23019417E3],(1/np.log(R_lin)))), label="Thermiator2")
plt.loglog(R_lin, fitM, label="Monitor")
plt.legend()
plt.show()
'''

def Thermiator(R):
    T = np.exp(np.polyval(params,(1/np.log(R))))
    return T
