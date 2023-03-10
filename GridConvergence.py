from func_calc_dfdx import func_calc_dfdx_2, func_calc_dfdx_4, func_calc_dfdx_6
import math
import numpy as np
import cmath
import matplotlib.pyplot as plt

# def mysin()

Nx = [201,401,501,1001]
DX = []
L2Norm_2 = []
L2Norm_4 = []
for g in range(len(Nx)):
    x = np.linspace(0,2*math.pi,Nx[g])
    dx = x[2] - x[1]
    DX.append(dx)

    k = 10
    f = np.sin(k*x)
    df_calc_2 = func_calc_dfdx_2(f, dx)
    df_calc_4 = func_calc_dfdx_4(f, dx)
    df_exact = k*np.cos(k*x)

    Error_2 = df_calc_2 - df_exact
    Error_4 = df_calc_4 - df_exact

    L2Norm_2.append(np.sqrt(np.sum(Error_2**2 )/Nx[g]))
    L2Norm_4.append(np.sqrt(np.sum(Error_4**2 )/Nx[g]))

fig = plt.figure(1)
plt.plot([math.log(i) for i in DX],[math.log(i) for i in L2Norm_2] ,label = '2nd order',color="red",linestyle='--',marker='*')
plt.plot([math.log(i) for i in DX],[math.log(i) for i in L2Norm_4],label = "4th order", color = "blue",linestyle = ":", marker = "x")
plt.title('L2 Norm Error Grid Convergence')
plt.xlabel('Log(\Delta x)')
plt.ylabel('Log(Error) L2-Norm Error')
plt.grid()
plt.legend(loc = "best")
plt.axis('equal')
plt.show()

fig = plt.figure(1)
plt.plot(DX, L2Norm_2, label = '2nd order',color="red",linestyle='--',marker='*')
plt.plot(DX, L2Norm_4 ,label = "4th order", color = "blue",linestyle = ":", marker = "x")
plt.title('L2 Norm Error Grid Convergence')
plt.xlabel('Grid Resolution dx')
plt.ylabel('L2 Norm error')
plt.grid()
plt.legend(loc = "best")
plt.show()




