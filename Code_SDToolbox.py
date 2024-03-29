import sys
import numpy as np
from SDToolbox import *
import csv
from matplotlib.pylab import *


# Boundry parameters
Pmin = 101325
Pmax = 4 * 101325
Tmin = 293
Tmax = 900
fimin = float(0.1)
fimax = float(2)


# Amount of iteration
npoints = 20




Ti = np.zeros(npoints, 'd')
Pi = np.zeros(npoints, 'd')
fi = np.zeros(npoints, 'd')

dcj_p = np.zeros(npoints, 'd')    #C-J density
Pcj_p = np.zeros(npoints, 'd')    #C-J pressure
Tcj_p = np.zeros(npoints, 'd')    #C-J temperature
vcj_p = np.zeros(npoints, 'd')    #C-J speed
dcj_f = np.zeros(npoints, 'd')  # C-J density
Pcj_f = np.zeros(npoints, 'd')  # C-J pressure
Tcj_f = np.zeros(npoints, 'd')  # C-J temperature
vcj_f = np.zeros(npoints, 'd')  # C-J speed
dcj_t = np.zeros(npoints, 'd')    #C-J density
Pcj_t = np.zeros(npoints, 'd')    #C-J pressure
Tcj_t = np.zeros(npoints, 'd')    #C-J temperature
vcj_t = np.zeros(npoints, 'd')    #C-J speed



# Detonation parameters in function of the pressure

for j in range(npoints):
    Pi[j] = Pmin + (Pmax - Pmin) * j / (npoints - 1)
    q = 'C3H8:1.375 O2:1'  # propane - oxygen mixture (mole fractions)
    mech = 'gri30_highT.cti'

    [cj_speed, R2] = CJspeed(Pi[j], Tmin, q, mech, 0)
    gas = PostShock_eq(cj_speed, Pi[j], Tmin, q, mech)

    dcj_p[j] = gas.density
    Pcj_p[j] = gas.P
    Tcj_p[j] = gas.T
    vcj_p[j] = cj_speed

    print 'For P=' + str(Pi[j]) + 'Pa detonation parameters are:'
    print 'dcj=' + str(dcj_p[j]) + ' kg/m^3'
    print 'Pcj=' + str(Pcj_p[j]) + ' kPa'
    print 'Tcj=' + str(Tcj_p[j]) + ' K'
    print 'vcj=' + str(vcj_p[j]) + ' m/s'
    print ''

csv_file = 'Detonation parameters in fuction of pressure (T=const=293K and fi=const=1).csv'
with open(csv_file, 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Initial Pressure', 'Density', 'Final Pressure', 'Final Temperature', 'Velocity'])
    for i in range(npoints):
        writer.writerow([Pi[i], dcj_p[i], Pcj_p[i], Tcj_p[i], vcj_p[i]])




 
# Detonation parameters in function of the temperature
for j in range(npoints):
    Ti[j] = Tmin + (Tmax - Tmin) * j / (npoints - 1)
    q = 'C3H8:1.375 O2:1'  # propane - oxygen mixture (mole fractions)
    mech = 'gri30_highT.cti'

    [cj_speed, R2] = CJspeed(Pmin, Ti[j], q, mech, 0)
    gas = PostShock_eq(cj_speed, Pmin, Ti[j], q, mech)

    dcj_t[j] = gas.density
    Pcj_t[j] = gas.P / 1000
    Tcj_t[j] = gas.T
    vcj_t[j] = cj_speed

    print 'For T=' + str(Ti[j]) + 'K detonation parameters are:'
    print 'dcj=' + str(dcj_t[j]) + ' kg/m^3'
    print 'Pcj=' + str(Pcj_t[j]) + ' kPa'
    print 'Tcj=' + str(Tcj_t[j]) + ' K'
    print 'vcj=' + str(vcj_t[j]) + ' m/s'
    print ''

csv_file = 'Detonation parameters in fuction of Temperture (P=const=1atm and fi=const=1).csv'
with open(csv_file, 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Initial Temperature', 'Density', 'Final Pressure', 'Final Temperature', 'Velocity'])
    for i in range(npoints):
        writer.writerow([Ti[i], dcj_t[i], Pcj_t[i], Tcj_t[i], vcj_t[i]])



# Detonation parameters in function of the fi
for j in range(npoints):
    fi[j] = fimin + (fimax - fimin) * j / (npoints - 1)
    no2 = float(1.375 / (fi[j] * 0.2))  # Number of O2 moles
    q = 'C3H8:1.375 O2:{0}'.format(str(no2))
    mech = 'gri30_highT.cti'

    [cj_speed, R2] = CJspeed(Pmin, Tmin, q, mech, 0)
    gas = PostShock_eq(cj_speed, Pmin, Tmin, q, mech)

    dcj_f[j] = float(gas.density)
    Pcj_f[j] = float(gas.P / 1000)
    Tcj_f[j] = float(gas.T)
    vcj_f[j] = float(cj_speed)

    print 'For fi=' + str(fi[j]) + ' detonation parameters are:'
    print 'dcj=' + str(dcj_f[j]) + ' kg/m^3'
    print 'Pcj=' + str(Pcj_f[j]) + ' kPa'
    print 'Tcj=' + str(Tcj_f[j]) + ' K'
    print 'vcj=' + str(vcj_f[j]) + ' m/s'
    print ''

csv_file = 'Detonation parameters in fuction of Fi (P=const=1atm and T=const=293K).csv'
with open(csv_file, 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Initial Fi', 'Density', 'Final Pressure', 'Final Temperature', 'Velocity'])
    for i in range(npoints):
        writer.writerow([fi[i], dcj_f[i], Pcj_f[i], Tcj_f[i], vcj_f[i]])


