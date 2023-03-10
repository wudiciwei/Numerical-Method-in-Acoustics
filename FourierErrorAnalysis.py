import math
import numpy as np
import cmath
import matplotlib.pyplot as plt

stencil = [-1,0,1]
coef = [-1,0,1]
coeff = [i/2 for i in coef]
# stencil = [0 1]; coeff = [-1 1];                        % 1st order biased
# stencil = [-2 -1 0 1 2]; coeff = [1 -8 0 8 -1]/12;      % 4th order central
# stencil = [0 1 2 3]; coeff = [-11 18 -9 2]/6;           % 3rd order biased
stencil = [0,1,2,3,4]
coef = [-25,48,-36,16,-3]
coeff = [i/12 for i in coef]

N = len(stencil)
kdx = np.linspace(0,math.pi,1000)
delta = kdx[1] - kdx[0]
T = []
Exact = []
Error = []
Integral_Error = []
for k in range(len(kdx)):
    T.append(0)
    for i in range(N):
        T[k] = T[k] - 1* complex(0,1) * cmath.exp(1 * complex(0,1) * kdx[k] * stencil[i]) * coeff[i]
    Exact.append(complex(kdx[k], 0))
    Error.append(abs(T[k] - Exact[k]))
    Integral_Error.append(sum(Error[0:k]) * delta)

fig = plt.figure(1)
ax1 = plt.subplot(1,2,1)
plt.plot(kdx,[i.real for i in T],color="red",linestyle='--')
plt.plot([0, math.pi],[0, math.pi])
# plt.axis([0, math.pi,0,math.pi])
plt.xlim((0, math.pi))
plt.ylim((0, math.pi))
plt.title('Real Part')
plt.xlabel('k\Deltax')
plt.ylabel('k\Deltax^*')
# plt.legend(loc = "best")#给图加上图例
plt.grid()


ax2 = plt.subplot(1,2,2)
plt.plot(kdx,[i.imag for i in T],color="red",linestyle='--')
plt.plot([0, math.pi],[0, 0],'-k')
plt.title('Imaginary Part')
plt.xlabel('k\Deltax')
plt.ylabel('k\Deltax^*')
plt.axis([0,math.pi,-1,1])
plt.grid()

plt.show()

fig = plt.figure(2)
plt.plot(kdx, Error, color="r",label="Local difference", linestyle = '--')
plt.plot(kdx, Integral_Error, color = "blue", label = "Integral error",linestyle = ':')
plt.title("Variation of error with k\Deltax")
plt.xlabel('k\Deltax')
plt.ylabel('Error Level')
plt.grid()
plt.show()

A = []
for i in range(len(Integral_Error)):
    if Integral_Error[i] < 0.0005:
        A.append(i-1)
print("kDx limit is {:.6f}".format(kdx[A[-1]]))