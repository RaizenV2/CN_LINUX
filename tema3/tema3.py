
def read_sparse_matrix(input_data):
    with open(input_data, 'r') as f:
        matrix = dict()
        n = int(f.readline().strip())

        for line in f:
            if line.strip() != "":
                field = line.split(",")
                value = float(field[0])
                key = (int(field[1]), int(field[2]))
                if matrix.get(key) is None:
                    matrix[key] = value
                else:
                    matrix[key] += value

        return matrix, n


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
                a.append(float(value))

        while(len(b) < n-p):
            value = f.readline().strip()
            if value != "":
                b.append(float(value))

        while(len(c) < n-q):
            value = f.readline().strip()
            if value != "":
                c.append(float(value))

    return a, b, c, n, p, q


def print_matrix(matrix_in):
    for key, value in matrix_in.items():
        print(key, "->", value)


def print_matrix_v2(matrix_in, n):
    for i in range(0, n):
        for j in range(0, n):
            key = (i, j)
            if matrix_in.get(key) is not None:
                print(key, "->", matrix_in[key])


def make_sum(sparse_matrix, a, b, c, n, p, q):
    for i in range(0, n):
        for j in range(0, n):
            key = (i, j)
            if i == j:

                if sparse_matrix.get(key) is not None:
                    # print(key, "->", sparse_matrix[key], "AFTER")
                    sparse_matrix[key] += float(a[i])
                    # print(key, "->", sparse_matrix[key], "BEFORE")
                    # print("*" *10)
                else:
                    sparse_matrix[key] = a[i]
            elif i + p == j and i < n-1:
                if sparse_matrix.get(key) is not None:
                    sparse_matrix[key] += b[i]
                else:
                    sparse_matrix[key] = b[i]
            elif i == j+q and j < n-1:
                if sparse_matrix.get(key) is not None:
                    sparse_matrix[key] += c[j]
                else:
                    sparse_matrix[key] = c[j]
    return sparse_matrix


def verify_matrix(sparse_matrix1, sparse_matrix2, n):
    for i in range(0, n):
        for j in range(0, n):
            key = (i, j)
            if sparse_matrix1.get(key) is not None and sparse_matrix2.get(key) is not None:
                if sparse_matrix1[key] != sparse_matrix2[key]:
                    print(key, "->", sparse_matrix1[key], "M1")
                    print(key, "->", sparse_matrix2[key], "M2")
                    return False

    return True


def multiply_matrix(sparse_matrix, a, b, c, n, p, q):
    sparse_matrix_2 = dict()
    for i in range(0, n):
        for j in range(0, n): 
            key = (i, j)
            res = 0
            if sparse_matrix.get(key) is not None:
                res += sparse_matrix.get(key) * a[j]  # a[i][j] * b[j][j]

            if j > p:
                key = (i, j-p)
                if sparse_matrix.get(key) is not None:
                    # a[i][j-p] * b[j-p][j]
                    res += sparse_matrix.get(key) * b[j-p]

            if j < n-q:
                key = (i, j+q)
                if sparse_matrix.get(key) is not None:
                    # a[i][j+p] * b[j+p][j]
                    res += sparse_matrix.get(key) * c[j]

            if res != 0:
                key_s = (i, j)
                sparse_matrix_2[key_s] = res
                # print(key_s, "-->", sparse_matrix_2[key_s])

    return sparse_matrix_2


def multipy_tridiagonal_matrix(a1, b1, c1, a, b, c, p, q, p1, q1, n):
    sparse_matrix_2 = dict()
    for i in range(0, n):
        for j in range(0, n):
            res_first = 0 #aici incepe valoare  care se calculeaza pentru elementul de pe poz i j
                          # res_first += a[i][k] * b[j][k]
            for k in range(0, n):
                value1 = 0 # elementul selectat din prima matrice
                value2 = 0 #a [i][k] # elementul selectat din a doua matrice 
                if k > i and k - i == p and i <= n-p:  # k = i+p
                    value1 = b[i]  # a[i][i+p] * b[i+p][j]

                if k == i:         # k == i
                    value1 = a[k]  # a[i][k] b[j][j]
                if i > k and i - k == q and k <= n-1:
                    value1 = c[k]
                
            #a [k][k+p] a[k][j]
                if j >=  k and j-k == p1:
                    value2 = b1[k]
            
                if k == j:
                    value2 = a1[k]

                if k - j == q1 and j <= n-1:
                    value2 = c1[j]

                res_first += value1 * value2
            key = (i, j)
            if res_first != 0:
                sparse_matrix_2[key] = res_first
                print(key, "->", sparse_matrix_2[key])


def print_tridiagonal_input(a, b, c, n, p, q):
    print("Dimension of matrix", n)
    print("Main diagonal", end=" ")

    for i in range(0, n):
        print(a[i], " ", end=" ")

    print("\n")

    print("2nd diagonal", end=" ")
    for i in range(0, n-p):
        print(b[i], " ", end=" ")

    print("\n")

    print("3nd diagonal", end=" ")
    for i in range(0, n-q):
        print(c[i], " ", end=" ")

    print("\n")


def main():
    # print("Run directly !")
    # SP_M1, n = read_sparse_matrix("a.txt")
    # SP_SUM, n = read_sparse_matrix("aplusb.txt")
    # print_matrix_v2(SP_M1, n)
    # a, b, c, n, p, q = read_tridiagonal_data("b.txt")
    # SP_M2 = make_sum(SP_M1, a, b, c, n, p, q)
    # # print_matrix_v2(SP_M2, n)
    # # print_matrix_v2(SP_SUM, n)

    # if verify_matrix(SP_M2, SP_SUM, n):
    #     print("It works now !\n")

    # SP_M1, n = read_sparse_matrix("a.txt")
    # SP_PROD = multiply_matrix(SP_M1, a, b, c, n, p, q)

    # SP_PRODF, n = read_sparse_matrix("aorib.txt")
    # # print_matrix(SD_PRODF)
    # if verify_matrix(SP_PROD, SP_PRODF, n):
    #     print("It works once again!\n")

    a, b, c, n, p, q = read_tridiagonal_data("test_tridiagonal.txt")

    a1, b1, c1, n1, p1, q1 = read_tridiagonal_data("test_tridiagonal.txt")

    print_tridiagonal_input(a, b, c, n, p, q)

    multipy_tridiagonal_matrix(a1, b1, c1, a, b, c, p, q, p1, q1, n)


if __name__ == "__main__":
    print("Some syntax available here !\n")
    main()
