def func_calc_dfdx_2(f,dx):
    coef_1 = [-1,1]
    coeff_1 = [i * 1 for i in coef_1]

    coef_c = [-1,0,1]
    coeff_c = [i*1/2 for i in coef_c]

    coeff_N = [i* (-1) for i in coeff_1]
    coeff_N.reverse()

    Nx = len(f)
    dfdx = []
    dfdx.append(sum(list(map(lambda e,f:e*f, f[0:2],coeff_1[0:2]))))

    for i in range(1,Nx-1):
        dfdx.append(sum(list(map(lambda e,f:e*f, f[i-1:i+2],coeff_c[0:3]))))

    i = Nx - 1
    dfdx.append(sum(list(map(lambda e,f:e*f, f[Nx-2:Nx],coeff_N))))

    dfdx_dx = [i/dx for i in dfdx]

    return dfdx_dx

def func_calc_dfdx_4(f,dx):
    coef_1 = [-3,4,-1]
    coeff_1 = [i/2 for i in coef_1]

    coef_2 = [-2,-3,6,-1]
    coeff_2 = [i/6 for i in coef_2]

    coef_c = [1,-8,0,8,-1]
    coeff_c = [i/12 for i in coef_c]

    coeff_Nm1 = [i*(-1) for i in coeff_2]
    coeff_Nm1.reverse()

    coeff_N = [i*(-1) for i in coeff_1]
    coeff_N.reverse()

    Nx = len(f)
    dfdx= []

    dfdx.append(sum(list(map(lambda e,f:e*f, f[0:3],coeff_1[0:3]))))
    dfdx.append(sum(list(map(lambda e, f: e * f, f[0:4], coeff_2[0:4]))))

    for i in range(2,Nx-2):
        dfdx.append(sum(list(map(lambda e, f: e * f, f[i-2:i+3], coeff_c[0:5]))))

    i = Nx-2
    dfdx.append(sum(list(map(lambda e, f: e * f, f[Nx-4:Nx], coeff_Nm1))))
    dfdx.append(sum(list(map(lambda e, f: e * f, f[Nx-3:Nx], coeff_N))))

    dfdx_dx = [i/dx for i in dfdx]

    return dfdx_dx

def func_calc_dfdx_6(f,dx):
    coef_1 = [-22,36,-18,4]
    coeff_1= [i/12 for i in coef_1]

    coef_2 = [-3,-10,18,-6,1]
    coeff_2 = [i/12 for i in coef_2]

    coef_3 = [3,-30,-20,60,-15,2]
    coeff_3 = [i/60 for i in coef_3]

    coef_c = [-1,9,-45,0,45,-9,1]
    coeff_c = [i/60 for i in coef_c]

    coeff_Nm2 = [i*(-1) for i in coeff_3]
    coeff_Nm2.reverse()

    coeff_Nm1 = [i*(-1) for i in coeff_2]
    coeff_Nm1.reverse()

    coeff_N = [i*(-1) for i in coeff_1]
    coeff_N.reverse()

    Nx = len(f)
    dfdx = []

    dfdx.append(sum(list(map(lambda e,f:e*f, f[0:4],coeff_1[0:4]))))
    dfdx.append(sum(list(map(lambda e,f:e*f, f[0:5],coeff_1[0:5]))))
    dfdx.append(sum(list(map(lambda e,f:e*f, f[0:6],coeff_1[0:6]))))

    for i in range(3,Nx-3):
        dfdx.append(sum(list(map(lambda e,f:e*f, f[i-3:i+4],coeff_c[0:7]))))

    dfdx.append(sum(list(map(lambda e,f:e*f, f[Nx-6:Nx],coeff_Nm2))))
    dfdx.append(sum(list(map(lambda e, f: e * f, f[Nx - 5:Nx], coeff_Nm1))))
    dfdx.append(sum(list(map(lambda e, f: e * f, f[Nx - 4:Nx], coeff_N))))

    dfdx_dx = [i/dx for i in dfdx]
    return dfdx_dx























