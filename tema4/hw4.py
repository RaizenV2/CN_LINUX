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


def Gauss_Seidel(a, b, c, f, p, q):
    n = len(a)
    xc = [0 for __ in range(n)]
    k = 0
    kmax = 10000
    dx = 0
    eps = 10 ** -16
    x_precedent = 0
    while 1:

        for i in range(len(a)):
            # xc[index]  = (f[index] - a[i][i-q]*v[i-q] - a[i][i+p]*vp_precedent) x[i+p]

            if i >= q:
                value1 = c[i-q]*xc[i-q]  # a[i][i-q] elementul de sub diagonala
            else:
                value1 = 0

            if i < n-p:
                # a[i][i+p] elementul deasupra diagonalei principale
                value2 = b[i] * x_precedent
            else:
                value2 = 0

            if i < n:
                xc[i] = (f[i]-value1 - value2) / a[i]
            else:
                xc[i] = (f[i]-c[i-q]*xc[i-q]) / a[i]
                if i >= q and i+p <= n:
                    print(
                        f"x[{i}] = f{i} -c{i-q} * xc[{i-q}] - b[{i}] * x[{i+p}]")
                    print("\n")

            # print("X ACTUAL", xc[i])
            # print("X PRECEDENT ", x_precedent)

            norma = math.sqrt(abs(xc[i]-x_precedent))
            if i < n-p:
                x_precedent = xc[i+p]

            # print("NORMA", norma, "\n")

        if not (norma >= eps and k < kmax and norma < 10 ** 8):
            break

        k += 1

    if dx < eps:
        return (xc, k)
    else:
        return("Divergenta")


def multipy_tridiagonal_matrix(a, b, c, p, q, n, v):
    ret_list = []

    for i in range(0, n):
        res_first = 0
        for j in range(0, n):

            value1 = 0
            value2 = 0  # a [i][k]

            if j == i:         # k == i
                value1 = a[j]  # a[i][k] b[j][j]

            if j > i and j - i == p and i < n-p:  # k = i+p
                value1 = b[i]  # a[i][i+p] * b[i+p][j]   a

            if i > j and i - j == q and j <= n-1:
                value1 = c[j]

            value2 = v[j]

            res_first += value1 * value2
        # print("Pe linia ", i, "-->", res_first)
        ret_list.append(res_first)

    return ret_list


def multipy_tridiagonal_matrix_v2(a, b, c, p, q, n, v):
    ret_list = []
    for i in range(0, n):
        res_val = 0
        res_val += a[i] * v[i]
        if i < n-p :
            res_val += b[i] * v[i+p]  # a[i][i+p]
        else:
            res_val += 0

        if i > q-1:
            res_val += c[i-q] * v[i-q]  # a[i+q]
        else:
            res_val += 0

        ret_list.append(res_val)

    return ret_list


def main():
    epsilon = 10**-14
    for i in range(1, 2):
        a, b, c, n, p, q = read_tridiagonal_data("a"+str(i)+".txt")
        f = read_free_terms("f"+str(i)+".txt")
        if check_non_null_values(a, epsilon):
            print("The main diagonal has no null values")
        final, iteratie = Gauss_Seidel(a, b, c, f, p, q)
        print(f"FInal vector {final}")
        # print(f"ITERIATIE{iteratie}")
        x_Gs = multipy_tridiagonal_matrix_v2(a, b, c, p, q, n, final)
        # print("\n"*3)
        ceva = np.linalg.norm(np.array(x_Gs) - np.array(f), ord=np.inf)
        print(ceva)


if __name__ == "__main__":
    # a, b, c, n, p, q = read_tridiagonal_data("test_tridiagonal.txt")
    # f = read_free_terms("freeterm.txt")
    # x_Gs = multipy_tridiagonal_matrix_v2(a, b, c, p, q, n, f)
    # print(f)
    # print("a= ",a)
    # print("b= ",b)
    # print("c= ",c)
    # print(x_Gs)
    main()
    # print(len(Axgs))
    # print(diferenta_norma)
