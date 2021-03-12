import numpy as np
import random
from scipy import linalg
import math
import copy


def check_symmetric(a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)


def verify_matrix(M):

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
    simmetric_matrix = np.random.randint(min, max, size=(n, n))
    simmetric_matrix = (simmetric_matrix + simmetric_matrix.T)/2
    return np.array(simmetric_matrix)


def cholesky(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    for i in range(n):
        for k in range(i + 1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            if i == k:
                L[i][k] = round(math.sqrt(A[i][i] - tmp_sum), 2)
            else:
                L[i][k] = round(1.0 / L[k][k] * (A[i][k] - tmp_sum), 2)
    return np.array(L)


def DS(M, b):
    n = len(M)
    x = [0]*n
    x[0] = b[0]/M[0][0]

    for i in range(1, n):
        sum = 0
        for j in range(i):
            sum += M[i][j]*x[j]
        x[i] = sum/M[i][i]
    
    print(f"DS x: {x}\n ")

    return x


def IS(M, b):
    n = len(M)
    x = [0]*n
    x[n-1] = b[n-1] / M[n-1][n-1]

    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(i, n):
            sum += M[i][j]*x[j]
        x[i] = sum/M[i][i]

    print(f"IS x: {x}\n ")

    return x


def determinant_cholesky(A, n):
    detA = 1
    for i in range(n):
        detA *= A[i][i]*A[i][i]
    return (detA)


if __name__ == "__main__":

    x = get_matrix_ordered("matricea_ideala.txt")
    if verify_matrix(x):
        print("The matrix is positive definite and simmetric\n")
    else:
        print("The matrix is NOT positive definite and simmetric")
        exit()

    x_copy = copy.deepcopy(x)
    cholesky_matrix = cholesky(x)

    b = generate_b_for_matrix(len(x), 10, 100)

    print(f"B generated {b}\n")

    print(f"The chosen one is: \n {x}\n")

    print(f"Cholesky Matrix: {cholesky_matrix}\n")

    print(
        f"Determinant calculand Cholesky:\n{determinant_cholesky(x, len(x))}\n")

    initial_matrix = np.dot(cholesky_matrix, cholesky_matrix.T)

    print(f"The initial matrix should be:\n {initial_matrix}\n")

    initial_matrix = np.round(initial_matrix)

    print(f"The initial matrix should be:\n {initial_matrix}\n")

    Chol_v1 = DS(initial_matrix, b)

    Chol_v2 = IS(initial_matrix, b)

    rez1 = np.linalg.norm(np.dot(initial_matrix, Chol_v1) - b, 2)

    rez2 = np.linalg.norm(np.dot(initial_matrix, Chol_v2) - b, 2)

    print(f"rez1: {rez1} \n rez2: {rez2} \n")

    p, L, U = linalg.lu(initial_matrix)
    solutiee = np.linalg.solve(initial_matrix, b)

    print(f"L: {L}\n")
    print(f"U :{U}\n")
    print(solutiee)
    # print(generate_matrix(10, 10, 100))
