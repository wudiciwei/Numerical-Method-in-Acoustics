from func_calc_dfdx import func_calc_dfdx_2, func_calc_dfdx_4, func_calc_dfdx_6
import math
import numpy as np
import cmath
import matplotlib.pyplot as plt

Nx = 101
x = np.linspace(0,2*np.pi,Nx)
dx = x[1] - x[0]

k = 20
f = np.sin(k*x)
df2_calc = func_calc_dfdx_2(f,dx)
df4_calc = func_calc_dfdx_4(f,dx)
df6_calc = func_calc_dfdx_6(f,dx)
ppw = 2*np.pi/k/dx

# Exact solution
x2 = np.linspace(0,2*np.pi,10000)            # HD mesh for exact solution
df_exact = k*np.cos(k*x2)

fig = plt.figure()
plt.plot(x2,df_exact,'-k',label = 'exact solution')
plt.plot(x,df2_calc,'xr',label = '2nd order')
plt.plot(x,df4_calc,'xg',label = '4th order')
plt.plot(x,df6_calc,'xb',label = '6th order')
plt.title('Resolution - {:.4f}'.format(ppw))
plt.xlabel('x')
plt.ylabel("$f'(x)$")
plt.legend(loc = "best")
plt.xlim([0,2*np.pi])
plt.show()