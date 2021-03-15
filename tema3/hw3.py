def matrix_read_up_a(input_data):
    f = open(input_data, "r")
    n = int(f.readline())

    matrix = ["" for x in range(n)]

    for line in f:
        elements = [int(value)
                    for value in line.strip().split(',') if value != '']
        value = elements[0]
        row = elements[1]
        column = elements[2]
        flag = 0
        print("Checking ")
        print("Matrix ", matrix)
        print("matrixay  ", elements)
        if(matrix[row] == ""):
            matrix[row] = [[value, column]]
        else:
            for el in range(0, len(matrix[row])):
                if(matrix[row][el][1] == column):
                    matrix[row][el][0] += value
                    flag = 1
                    break
            if(flag == 0):
                matrix[row].append([value, column])
    f.close()
    print(matrix)


def read_up_b_matrix(input_data):
    with open(input_data, 'r') as f:
        n = int(f.readline())
        p = int(f.readline())
        q = int(f.readline())
        a = [float(f.readline().strip()) for __ in range(n)]
        b = [float(f.readline().strip()) for __ in range(n-p)]
        c = [float(f.readline().strip()) for __ in range(n-q)]
    return a, b, c


def sum_matrix(M, a, b, c, q, p):
    matrix = []
    counter_a = 0
    counter_b = 0
    counter_c = 0
    for i in range(len(M)):
        row = []
        for j in range(len(M)):
            value = 0
            if i == j:
                value += a[counter_a]
                counter_a += 1
            elif i == j+p:
                value += b[counter_b]
                counter_b += 1
            elif i == j+q:
                value += c[counter_c]
                counter_c += 1
            for element in (len(M[i])):
                if M[i][element][1] == j:
                    value += M[i][element][0]
                row.append(value)
        matrix.append(row)

    return matrix


def multiply_matrix(M, a, b, c, q, p):
    print("This is where we will implement the matrix!\n")


def read_full_matrix_from_file(input_data):
    with open(input_data, 'r') as f:
        return [[float(num) for num in line.split(',')] for line in f if line.strip() != ""]


if __name__ == "__main__":
    print("it will run from main program\n   ")
    read_up_b_matrix("b.txt")
    diagonala, deasupra, dedesubt = read_up_b_matrix("b.txt")
    print(len(diagonala))
    print(len(deasupra))
    print(len(dedesubt))
