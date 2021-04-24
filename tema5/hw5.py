
import numpy as np
import random
import math
# Verificari pe matrice , de la tema 2 + generari de matrice , random, simetrice , si pozitiv definite


def get_matrix_unordered(data_input, dimension1, dimension2):
    my_matrix = []
    with open(data_input, 'r') as f:
        lines_list = f.readlines()
        for line in lines_list:
            for val in line.strip().split(','):
                if len(my_matrix) == dimension1 * dimension2:
                    break
                if val.isdigit and val != "":
                    my_matrix.append(float(val))

    my_matrix = np.array(my_matrix)
    my_matrix = np.reshape(my_matrix, (dimension1, dimension2))

    return my_matrix


def check_symmetric(a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)


def is_diagonal_matrix(M1):
    return np.array_equal(M1, np.diag(np.diag(M1)))


def determinant(A):
    detA = 1
    for i in range(len(A)):
        detA = detA * A[i][i]
    return (detA)


def get_matrix_ordered(data_input):
    with open(data_input, 'r') as f:
        my_matrix = [[float(num) for num in line.split(',')]
                     for line in f if line.strip() != ""]
        return np.array(my_matrix)


def generate_simmetric_matrix(n, min, max):
    while True:
        simmetric_matrix = np.random.randint(min, max, size=(n, n))
        simmetric_matrix = (simmetric_matrix + simmetric_matrix.T)/2
        if verify_matrix(simmetric_matrix):
            break
    return np.array(simmetric_matrix)


def verify_matrix(M):  # de implementat epsilon

    if not check_symmetric(M):
        print("The matrix is not simmetric")
        return False

    for dimension in range(1, len(M)+1):
        minor = [row[:dimension] for row in (M[:dimension])]
        if np.linalg.det(minor) < 0:
            print("The matrix is not positive :( ")
            return False
    return True


def generate_matrix(n, min, max):

    matrix = [[round(random.uniform(min, max), 2)
               for __ in range(n)] for __ in range(n)]
    return np.array(matrix)


def compute_p_q(M):
    sample = ()
    if M is None:
        print("Matrix cannot be empty\n")
        return
    n = len(M)
    max = M[0][1]
    for i in range(0, n):
        for j in range(0, n):
            if max < M[i][j] and i != j:
                max = M[i][j]
                sample = (i, j)
    return sample


def compute_c_s_t(M, p, q):
    alfa = (M[p][p] - M[q][q]) / 2 * M[p][q]

    value = math.sqrt(alfa ** 2 + 1)

    if alfa >= 0:
        final_value = - alfa + value
    else:
        final_value = -alfa - value

    final = math.sqrt(1 + final_value ** 2)
    c = 1 / final
    s = final_value / final

    return c, s


def Compute_R_Matrix(c, s, n, p, q):
    matrix = np.zeros(shape=(n, n))
    for i in range(0, n):
        for j in range(0, n):

            if i == j and i != p and i != q:
                matrix[i][j] = 1

            elif i == j and i == p:
                matrix[i][j] = c

            elif i == j and i == q:
                matrix[i][j] = c

            elif i == p and j == q:
                matrix[i][j] = s

            elif i == q and j == p:
                matrix[i][j] = -s

    return matrix, matrix.T


def compute_rotation_matrix(M):
    pass


def Jacobi_Method(m):
    m1 = np.copy(m)
    n = len(m)
    kmax = 10000
    k = 0
    while not is_diagonal_matrix(m1) and k < kmax:

        U = np.identity(n)

        p, q = compute_p_q(m1)

        c, s = compute_c_s_t(m1, p, q)

        R, R_T = Compute_R_Matrix(c, s, n, p, q)

        m1 = R @  m1 @ R_T

        U = U @ R_T

        k += 1

    print(m1)
    c = m @ U
    d = U @ m1
    ceva = np.linalg.norm(c-d, ord=np.inf)
    print(ceva)


def compute_another_method(m):
    m_k = np.copy(m)
    eps = 10 ** -15
    k = 0
    kmax = 10000
    while True and k < kmax:
        L = np.linalg.cholesky(m_k)
        temp = L.T @ L
        if np.linalg.norm(temp-m_k) < eps:
            break
        k += 1
        m_k = temp
        # print("something")
    return temp


if __name__ == "__main__":
    m = get_matrix_unordered("input.txt", 3, 3)

    print(m)
    line = len(m)
    column = len(m[0])
    if line == column:

        # Jacobi_Method(m)
         c = compute_another_method(m)
         print(c)

        # try:
        #     result = "sa nu dea eroare"
        #     print(result)
        # except np.linalg.LinAlgError:
        #     print("The matrix is not positive defined")
    else:

        U, S, V = np.linalg.svd(m)
        print("U--->")
        print(U)
        print("*" * 100)
        print("S-->")
        print(S)
        S = np.diag(S)
        print(S)

        if line > column:
            column1 = np.zeros(len(S[0]))
            print("Add column")
            S = np.column_stack((S, column1))
        else:
            line1 = np.zeros(len(S))
            print("Aadd line")
            print("column")

            S = np.vstack([S, line1])

        print("*" * 100)
        print("V--->",end=" ")
        print(V)
        print("*" * 100)
        print("CONDITTION NUMBER -->",end= " ")
        condition_number = np.linalg.cond(m)

        print(condition_number)
        # print(valoarea_singulara)

        rank_matrix = np.linalg.matrix_rank(m)

        print("RANK")

        print(rank_matrix)

        Moose_Penrose = np.linalg.pinv(m)
        print("MOOSE_PENROSE")
        print(Moose_Penrose)

        print("PSEUDO INVERSE IN A PARTICULAR CASE\n")
        m_i = V.T @ S @ U.T
        aux2 = m.T @ m
        print(">"*100)
        print(aux2)
        try:
            aux = np.linalg.inv(aux2)
            m_j = aux @ m.t
        except np.linalg.LinAlgError:
            print("The determinat of inverse is zero so we  cannot proceed")
        
        norma = np.linalg.norm(m_i - m_j, ord=np.inf)
        print(norma)
