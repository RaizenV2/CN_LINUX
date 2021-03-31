import numpy as np
import math


def read_free_terms(input_data):
    free_t = []
    with open(input_data, 'r') as f:
        length_terms = int(f.readline())
        while(len(free_t) < length_terms):
            value = f.readline().strip()
            if value != "":
                free_t.append(float(value))
    return free_t


def read_tridiagonal_data(input_data):
    with open(input_data, 'r') as f:
        a = []
        b = []
        c = []
        n = int(f.readline())
        p = int(f.readline())
        q = int(f.readline())

        while(len(a) < n):
            value = f.readline().strip()
            if value != "":
                a.append(float(value))  # citesc diagonala principala a
        while(len(c) < n-p):
            value = f.readline().strip()
            if value != "":
                # citesc diagonala secundara de sub cea principala c
                c.append(float(value))
        while(len(b) < n-q):
            value = f.readline().strip()
            if value != "":
                # citesc diagonala de deasupra diagonalei principale  b
                b.append(float(value))

    return a, b, c, n, p, q


def check_non_null_values(main_diagonal, epsilon):
    if epsilon in main_diagonal:
        return False
    return True


def norma(z):
    return math.sqrt(np.sum(np.power(z, 2.0)))


def sum_current_iteration(index, a, b, c, x):
    ret_sum = 0
    tri_flag = 0
    if index < 0:
        return ret_sum

    for j in range(0, index):
        if j == index:
            ret_sum += a[index] * x[j]
            tri_flag += 1
        elif index + 1 == j:
            ret_sum += b[index] * x[j]
            tri_flag += 1
        elif index == j+1:
            ret_sum += c[index] * x[j]
            tri_flag += 1
        elif tri_flag == 3:
            break
    return ret_sum


def sum_current_iteration_v2(index, a, b, c, x, p, q):
    ret_sum = 0
    if index <= 0:
        return ret_sum
        ret_sum += a[index] * x[index]
        ret_sum += b[index] * x[index-p]
        if index < len(a)-1:
            ret_sum += c[index] * x[index+q]
    return ret_sum


def sum_last_iteration(index, a, b, c, x):
    ret_sum = 0
    n = len(a)
    b_l = len(b)
    c_l = len(c)
    tri_flag = 0
    for j in range(index, n):
        if j == index:
            ret_sum += a[index] * x[j]
            tri_flag += 1
        elif index + 1 == j and index <= b_l:
            ret_sum += b[index] * x[j]
            tri_flag += 1
        elif index == j+1 and index <= c_l:
            ret_sum += c[index] * x[j]
            tri_flag += 1
        elif tri_flag == 3:
            break
    return ret_sum


def Gauss_Seidel(a, b, c, f, p, q):
    n = len(a)
    xc = [0 for __ in range(n)]
    xp = xc[:]
    k = 0
    kmax = 10000
    dx = 0
    eps = 10 ** -16
    while 1:
        xp = xc[:]
        for index in range(len(a)):
            xc[index] = (f[index] - sum_current_iteration_v2(index, a, b,
                                                             c, xc, p, q) - sum_current_iteration_v2(index+1, a, b, c, xp, p, q))/a[index]

        dx = norma([xc[i]-xp[i] for i in range(len(xc))])
        k += 1
        if not(dx >= eps and k <= kmax and dx <= pow(10, 8)):
            break
    if dx < eps:
        return (xc, k)
    else:
        return "Divergenta!!"


if __name__ == "__main__":
    epsilon = 10**-15
    a, b, c, n, p, q = read_tridiagonal_data("a1.txt")
    f = read_free_terms("f1.txt")
    if check_non_null_values(a, epsilon):
        print("The main diagonal has no null values")
    final, iteratie = Gauss_Seidel(a, b, c, f, p, q)
    print(f"FInal vector {final}")
    print(f"ITERIATIE{iteratie}")
    print("\n"*3)

    a, b, c, n, p, q = read_tridiagonal_data("a2.txt")
    f = read_free_terms("f2.txt")
    if check_non_null_values(a, epsilon):
        print("The main diagonal has no null values")
    final, iteratie = Gauss_Seidel(a, b, c, f, p, q)
    print(f"FInal vector {final}")
    print(f"ITERIATIE{iteratie}")
    print(f"LEn")
