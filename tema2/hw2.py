import numpy as np
import random
from scipy import linalg
import math


def check_symmetric(a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)


def verify_matrix(M):  # de implementat epsilon

    if not check_symmetric(M):
        print("The matrix is not simmetric")
        return False

    for dimension in range(1, len(M)+1):
        minor = [row[:dimension] for row in (M[:dimension])]
        if linalg.det(minor) < 0:
            print("The matrix is not positive :( ")
            return False
    return True

# function when numbers are not ordered into the file , but separated by a comma


def get_matrix_unordered(data_input, dimension):
    my_matrix = []
    with open(data_input, 'r') as f:
        lines_list = f.readlines()
        for line in lines_list:
            for val in line.strip().split(','):
                if len(my_matrix) == dimension * dimension:
                    break
                if val.isdigit and val != "":
                    my_matrix.append(val)

    my_matrix = np.array(my_matrix)
    my_matrix = np.reshape(my_matrix, (dimension, dimension))

    return my_matrix


# function when numbers are ordered in a file ,
# need to have a preconfigured input textfile


def get_matrix_ordered(data_input):
    with open(data_input, 'r') as f:
        my_matrix = [[float(num) for num in line.split(',')]
                     for line in f if line.strip() != ""]
        return np.array(my_matrix)

# generatinf


def generate_b_for_matrix(n, min, max):
    c = [round(random.uniform(min, max), 2)for __ in range(n)]
    return c


def get_matrix_input():
    n = input("How big do u want the matrix to be ? (nxn)")
    n = int(n)
    matrix = [[float(input()) for __ in range(n)] for __ in range(n)]
    return np.array(matrix)


def generate_matrix(n, min, max):

    matrix = [[round(random.uniform(min, max), 2)
               for __ in range(n)] for __ in range(n)]
    return np.array(matrix)


def generate_simmetric_matrix(n, min, max):
    while True:
        simmetric_matrix = np.random.randint(min, max, size=(n, n))
        simmetric_matrix = (simmetric_matrix + simmetric_matrix.T)/2
        if verify_matrix(simmetric_matrix):
            break

    return np.array(simmetric_matrix)


def lppFormula2(p, d, A, eps):
    s = 0
    for j in range(0, p):
        s = s + (A[p][j] * A[p][j])

    if (math.sqrt(d[p] - s)) <= eps:
        return eps
    else:
        return math.sqrt(d[p] - s)


def lipFormula2(i, p, A, eps):
    if i > p:  # partea inferioara a lui A
        Ai = p
        Ap = i
    else:  # partea superioara a lui A
        Ai = i
        Ap = p

    s = 0
    for j in range(0, p):
        s = s + (A[i][j] * A[p][j])

    if ((A[Ai][Ap] - s) / A[p][p]) <= eps:
        return eps
    else:
        return (A[Ai][Ap] - s) / A[p][p]


def cholesky3(A, d, eps):
    n = len(A)
    ret = A

    for j in range(n):  # n pasi (coloanele lui L)
        # print("j=",j)
        for i in range(j, n):  # calculam elementele de sub diagonala principala
            # print("  i= ", i)
            if i == j:
                ret[i][j] = lppFormula2(i, d, ret, eps)
            else:
                ret[i][j] = lipFormula2(i, j, ret, eps)
        # print("\n")

    return np.array(ret)


def determinant(A):
    detA = 1
    for i in range(len(A)):
        detA = detA * A[i][i]
    return (detA)


def matrixConfig(x, d):
    n = len(x)
    matrixResulted = [[0.0] * n for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            matrixResulted[i][j] = x[i][j]
    return np.array(matrixResulted)


def calul_epsilon():
    u = 1
    while 1+u > 1:
        u /= 10
    return u * 10


def calcul_xChol(A, b, eps):
    n = len(A)
    solutie = [eps for i in range(n)]

    # notam y = L_trans * x
    # rezolvam L * y = b
    y = [eps]*n
    y[0] = b[0]/A[0][0]
    for i in range(1, n):
        sum = 0
        for j in range(i):
            sum = sum + A[i][j] * y[j]
        y[i] = (b[i] - sum) / A[i][i]

    # rezolvam L_trans * x = y
    x = [eps]*n
    x[n-1] = y[n-1] / A[n-1][n-1]

    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum = sum + A[j][i] * x[j]
            if sum == eps:
                sum = sum * (-1)
        x[i] = (y[i] - sum) / A[i][i]

    return np.array(x)


def get_init_matrix(A, eps, d):
    n = len(A)
    rez = [[eps] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                rez[i][j] = d[i]
            else:
                if i > j:
                    rez[i][j] = A[j][i]
                else:
                    rez[i][j] = A[i][j]

    return np.array(rez)


def calcul_inversa(A, eps):
    n = len(A)
    rezultat = [[0.0] * n for i in range(n)]

    for k in range(n):
        # rezolv A * x = l_k
        # adica L * L_trans * x = l_k
        # adica L * y = l_k
        l = [eps for t in range(n)]  # generez l_k
        l[k] = 1

        # rezolv L * y = l_k
        y = [eps]*n
        y[0] = l[0]/A[0][0]
        for i in range(1, n):
            sum = 0
            for j in range(i):
                sum = sum + A[i][j] * y[j]
            y[i] = (l[i] - sum) / A[i][i]

        # rezolv L_trans * x = y
        x = [eps]*n
        x[n-1] = y[n-1] / A[n-1][n-1]
        for i in range(n-2, -1, -1):
            sum = 0
            for j in range(i+1, n):
                sum = sum + A[j][i] * x[j]
                if sum == eps:
                    sum = sum * (-1)
            x[i] = (y[i] - sum) / A[i][i]

        # actualizez coloana k
        for i in range(n):
            rezultat[i][k] = x[i]

    return np.array(rezultat)


if __name__ == "__main__":

    eps = calul_epsilon()
    ok = True
    while ok:
        option = int(
            input("\n\n\n\n1. Tastatura \n2. Fisier \n3. Random\nType your option:"))
        if option == 1:
            x = get_matrix_input()
            d = [0.0 for i in range(len(x))]
            for i in range(0, len(x)):
                d[i] = x[i][i]
            ok = False
        else:
            if option == 2:
                x = get_matrix_ordered("matricea_ideala.txt")
                d = [0.0 for i in range(len(x))]
                for i in range(0, len(x)):
                    d[i] = x[i][i]
                ok = False
            else:
                if option == 3:
                    x = generate_simmetric_matrix(4, 1, 50)
                    d = [0.0 for i in range(len(x))]
                    for i in range(0, len(x)):
                        d[i] = x[i][i]
                    ok = False
                else:
                    print("Not a valid option!\n\n\n")
                    ok = True

    if verify_matrix(x):
        print("The matrix is positive definite and simmetric\n")
        A = matrixConfig(x, d)
    else:
        print("The matrix is NOT positive definite and simmetric")
        exit()

    A = cholesky3(A, d, eps)

    print(f"The chosen one is: \n {x}\n")

    print(f"\nA:\n {A}\n")

    print(f"Determinantul matricii A:\n{determinant(A)}\n")

    b = generate_b_for_matrix(len(x), 10, 100)
    # b = [12, 6, 13, 20]
    print(f"B generated {b}\n")

    xChol = calcul_xChol(A, b, eps)
    print(f"\nxChol :", xChol)

    euclidianNorm = np.linalg.norm(
        np.dot(get_init_matrix(A, eps, d), xChol) - b, 2)
    print(f"Norma euclidiana este: {euclidianNorm}\n")

    p, L, U = linalg.lu(get_init_matrix(A, eps, d))
    solutiee = np.linalg.solve(get_init_matrix(A, eps, d), b)

    print(f"L: {L}\n")
    print(f"U :{U}\n")
    print(solutiee)

    aproxInversa = calcul_inversa(A, eps)
    print(f"\nAproxiarea inversei matricei A este:\n {aproxInversa}\n")
    Abibl = linalg.inv(get_init_matrix(A, eps, d))
    print(f"\nA_bibl este:\n {Abibl}\n")
    normaMatrice = np.linalg.norm(aproxInversa - Abibl)
    print(f"\nNorma este:\n {normaMatrice}\n")
