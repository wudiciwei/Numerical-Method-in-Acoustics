from func_calc_dfdx import func_calc_dfdx_2, func_calc_dfdx_4, func_calc_dfdx_6
import math
import numpy as np
import cmath
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

# 1. Case Setup (Mesh)
x_0 = 0
x_max = 100
Nx = 201
x = np.linspace(0,x_max,Nx)
dx = x[1] - x[0]
print('Mesh generated \n')
print('Spatial resolution is: {:.4f} [m] \n'.format(dx))

# 2. Define Initial Condition (t0)
f = np.zeros(Nx)

# Specify a particular wave function - Gaussian Pulse
sigma = 10
x_center = 50.5

for i in range(Nx):
    f[i] = 1/sigma/np.sqrt(2)/np.pi * np.exp(-0.5 * ((x[i]-x_center)/sigma)**2)

ppw = np.array([15])
amp = np.array([1])
for i in range(Nx):
    f[i] = f[i] * np.sum(amp[0]* np.sin(x[i]*2*np.pi/((ppw[0] - 1)*dx) ))

print("Solution -f(x)- initialized \n")
p = plt.figure(1)
plt.plot(x,f,marker = 'x')
plt.title('Solution Field at Time=0')
plt.xlabel('x [m]')
plt.ylabel('f(x) at specified time')
plt.axis([0,max(x),-0.05,0.05])
plt.show()

# 3. Solution Iteration
# 3.1 Setup Iteration Settings
U = 1
tFinal = 30
CFL = 0.05
dt = CFL*dx/U
showEvery = 40

nTimeSteps = math.ceil(tFinal / dt)
print('Temporal resolution is: {:.4f} [s] \n'.format(dt))
print('Number of iterations is: {:,} \n'.format(nTimeSteps))

f_2 = f
f_4 = f
f_6 = f
x2 = np.linspace(0,x_max,10*Nx)
plt.close()
fig = plt.figure()
plt.ion()


for t in range(nTimeSteps):
    plt.cla()
    time = (t+1)*dt

    dfdx_2 = func_calc_dfdx_2(f_2, dx)
    dfdx_4 = func_calc_dfdx_4(f_4, dx)
    dfdx_6 = func_calc_dfdx_6(f_6, dx)

    dfdx_2 = np.array(dfdx_2)
    dfdx_4 = np.array(dfdx_4)
    dfdx_6 = np.array(dfdx_6)

    f_2 = f_2 - U * dfdx_2 * dt
    f_4 = f_4 - U * dfdx_4 * dt
    f_6 = f_6 - U * dfdx_6 * dt

    f_2[0] = 0
    f_4[0] = 0
    f_6[0] = 0

    f_exact = []
    f_e1 = 1/sigma/np.sqrt(2)/np.pi*np.exp(-0.5*((x2 - x_center - U*time)/sigma)**2)

    for i in range(len(x2)):
        f_exact.append(f_e1[i]*np.sum(amp[0] * np.sin((x2[i] - U*time)*2*np.pi/((ppw[0] - 1)*dx))))

    if(t%showEvery == 0):
        plt.plot(x2,f_exact,color = 'k', label = 'exact')
        plt.plot(x, f_2,color = 'r', label = '2order')
        plt.plot(x, f_4, color='g', label = '4order')
        plt.plot(x, f_6, color='b', label = '6order')

        plt.axis([0,max(x),-0.05,0.05])
        plt.title('Solution Field at Time= {:.4f}'.format(time))
        plt.xlabel('x [m]')
        plt.ylabel('f(x) at specified time')
        plt.legend(loc = 'best')
        plt.pause(0.1)

plt.show()












