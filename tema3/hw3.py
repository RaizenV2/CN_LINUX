

from copy import deepcopy


def matrix_read_up_a(input_data):
    f = open(input_data, "r")
    n = int(f.readline())

    matrix = ["" for x in range(n)]

    for line in f:
        elements = [float(value)
                    for value in line.strip().split(',') if value != '']
        value = elements[0]
        row = int(elements[1])
        column = int(elements[2])
        flag = 0
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
    return matrix


def read_up_b_matrix(input_data):
    with open(input_data, 'r') as f:
        n = int(f.readline())
        p = int(f.readline())
        q = int(f.readline())
        a = [float(f.readline().strip()) for __ in range(n)]
        b = [float(f.readline().strip()) for __ in range(n-p)]
        c = [float(f.readline().strip()) for __ in range(n-q)]
    return a, b, c


def matrix_sum(arr, a, b, c):  # de adaugat p si q aici pentru variabile
    for line in range(len(a)):
        for element in range(len(arr)):
            try:
                if arr[line][element][1] == line:
                    arr[line][element][0] += a[line]

            except IndexError:
                pass

            try:

                # + p in loc de +1 , line < len(a)
                if(arr[line][element][1] == line+1 and line < len(a)):
                    arr[line][element][0] += b[line]

            except IndexError:
                pass
            try:
                if (arr[line][element][1] == line - 1 and line > 0):  # de inlocuit cu q
                    # fiindca este cu un nivel mai jos , de asta decrementam indexul
                    arr[line][element][0] += c[line-1]

            except IndexError:
                pass
        # resturile care nu au fost gasite si adaugate pentru program
        arr[line].append([a[line], line])

        if(line+1 < len(b)):
            arr[line].append([b[line], line+1])
        if (line + 1 < len(c)):
            arr[line+1].append([c[line], line])
            print(line+1, c[line], arr[line+1])

    return arr


def get_matrix_element_multiplication(row, column):
    element = 0.0
    for element in range(len(row)):
        element += row[element]*column[element]
    return element


def get_column_matrix(Matrix, column_no):
    column = []
    for line in range(len(Matrix)):
        # nu am mai folosit functia asta , dar este buna pentru urmatoarea tema
        for element in range(len(Matrix[line])):
            if Matrix[line][element][1] == column_no:
                column.append((Matrix[line][element][0], line))
    return column


def get_line_matrix(Matrix, line_no):
    line = []
    for element in range(len(Matrix[line_no])):
        value = Matrix[line_no][element][0]
        column_found = Matrix[line_no][element][1]

        line.append((value, column_found))
    return line


def get_value(row, position):
    for x in range(len(row)):
        if position == row[x][1]:
            return row[x][0]
    return 0


def multiply_matrix(Matrix, a, b, c):
    result_matrix = []
    empty_list = []
    for __ in range(0, len(Matrix)):
        result_matrix.append(empty_list)

    for i in range(0, len(Matrix)):
        row = get_line_matrix(Matrix, i)
        counter_a = 0
        counter_b = 0
        counter_c = 0
        for j in range(0, len(Matrix)):
            # result[i][j] += A[i][k] * B[k][j]
            final_cut = 0

            for k in range(0, len(Matrix)):
                value = get_value(row, k)  # A[i][k] - in mod normal
                if k == j:
                    value2 = a[counter_a]
                    counter_a += 1
                elif k+1 == j:
                    # Obtinem B[k][j] in functie de vectorii salvati si relatiile dintre indexii lor
                    value2 = b[counter_b]
                    counter_b += 1              #
                elif k == k+1:
                    value2 = c[counter_c]
                    counter_c += 1
                else:
                    value2 = 0
                final_cut += value*value2  # result[i][j] += A[i][k] * B[k][j]

            if final_cut != 0:
                print(f"Linia {i} coloana {j} {final_cut}")
                valoare_ls = [final_cut, j]
                result_matrix[i].append(valoare_ls)

                # iterate through rows of X
    return result_matrix


def check_matrix(a, file_name):
    f = open(file_name, "r")
    n = int(f.readline())
    i = 0                               #verifica cele doua matrici 
    E = 10 ** (-15)
    for line in f:
        values = [float(value)
                  for value in line.strip().split(',') if value != '']
        for elements in arr[int(values[1])]:
            if(elements[1] == int(values[2])):
                if elements[0] != values[0]:
                    if abs(float(elements[0]) - values[0]) > E:
                        print("Error")


if __name__ == "__main__":

    matrice = matrix_read_up_a("a.txt")
    # for line in range(40, 50):
    #     print(f"Line is {line}")
    #     line_o = get_line_matrix(matrice, line)
    #     print(line_o)

    # for column in range(100, 110):
    #     print(f"Column is {column}")
    #     column_o = get_column_matrix(matrice, column)
    #     print(column_o)

    a, b, c = read_up_b_matrix("b.txt")
    print(len(a))
    print(len(b))
    print(len(c))
    print(len(matrice))
    multiply_matrix(matrice, a, b, c)
