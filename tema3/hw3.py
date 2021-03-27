

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


def matrix_sum(arr, a, b, c):
    for line in range(len(a)):
        for element in range(len(arr[line])):
            try:
                if arr[line][element][1] == line:
                    arr[line][element][0] += a[line]
                    # print(arr[line][element][0],line,arr[line][element][1])
            except IndexError:
                pass
                # print(arr[line][len(arr[line])-1])
                # print(arr[line][len(arr[line])-1][0], line,arr[line][len(arr[line])-1][1])
            try:
                if(arr[line][element][1] == line+1 and line < len(a)):
                    arr[line][element][0] += b[line]
                    # print(arr[line][element][0],line,arr[line][element][1])
            except IndexError:
                pass
            try:

                if (arr[line][element][1] == line - 1 and line > 0):
                    arr[line+1][element][0] += c[line]
                    # print(arr[line][element][0], line, arr[line][element][1])
            except IndexError:
                pass
                # print(arr[line][len(arr[line])-1][0],line,arr[line][len(arr[line])-1][1])

    for line in range(len(a)):
        flag_a, flag_b, flag_c = 1, 1, 1
        for element in range(len(arr[line])):
            if(line == arr[line][element][1]):
                flag_a = 0
            if(line+1 == arr[line][element][1]):
                flag_b = 0
            if(line-1 == arr[line][element][1]):
                flag_c = 0
        if(flag_a):
            arr.append([a[line], line])
        if(flag_b and line < len(b)):
            arr[line].append([b[line], line + 1])
        if(flag_c and line < len(c)):
            arr[line + 1].append([c[line], line])

            #     pass
            #
            # #print(a[line],arr[line])
            # if(line+1<len(b)):
            #     arr[line].append([b[line],line+1])
            # if (line + 1 < len(c)):
            #     arr[line+1].append([c[line], line])
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


def multiply_matrix_triangular(matrix1, matrix2):

    result_matrix = []
    empty_list = []
    for __ in range(0, len(matrix1)):
        result_matrix.append(empty_list)

    for i in range(0, len(matrix1)):
        cell_i_j = 0
        for j in range(0, len(matrix2)):
            # line_matrix[0] -valoarea a[i][j] line[matrix][1] = indecele de pe coloana
            line_matrix = get_line_matrix(matrix1, i)
            column_matrix = get_column_matrix(matrix2, j)  # coloana b[j][i]
            for element_linie in line_matrix:
                for elemenet_coloana in column_matrix:
                    if element_linie[1] == elemenet_coloana[1]:
                        cell_i_j += element_linie[0] * elemenet_coloana[0]
            if cell_i_j != 0:
                result_matrix[i].append([cell_i_j, j])
    return result_matrix



def get_line_matrix(Matrix, line_no):
    line = []
    for element in range(len(Matrix[line_no])):
        value = Matrix[line_no][element][0]
        column_found = Matrix[line_no][element][1]

        line.append((value, column_found))
    return line


def get_non_zero_column_positions(row):
    ret_list = []
    for x in range(len(row)):
        ret_list.append(row[x][1])

    ret_list = sorted(ret_list)

    return ret_list


def get_value(row, position):
    for x in range(len(row)):
        if position == row[x][1]:
            return row[x][0]
    return 0


def multiply_matrix_remaked(Matrix, a, b, c):
    result_matrix = []
    empty_list = []
    for __ in range(0, len(Matrix)):
        result_matrix.append(empty_list)

    for i in range(0, len(Matrix)):

        length_a = len(a)
        length_b = len(b)
        length_c = len(c)
        row = get_line_matrix(Matrix, i)
        column_positions = get_non_zero_column_positions(row)
        for j in range(0, len(Matrix)):
            final_cut = 0
            counter_a = 0
            counter_b = 0
            counter_c = 0

            for k in column_positions:  # aici in loc ce am facut eu poti itera  numai prin coloanele salvate de mine, get line iti da randul , alaturi de valoare iti spune si pe ce linie coloana a gasit , te poti folosi de asta pentru a nu itera prin o groaza de valori degeaba
                value = get_value(row, k)  # A[i][k] - in mod normal
                if k == j and counter_a < length_a:
                    value2 = a[counter_a]
                    counter_a += 1
                elif k+1 == j and counter_b < length_b:
                    # Obtinem B[k][j] in functie de vectorii salvati si relatiile dintre indexii lor
                    value2 = b[counter_b]
                    counter_b += 1              #
                elif k == j+1 and counter_c < length_c:
                    value2 = c[counter_c]
                    counter_c += 1
                else:
                    value2 = 0
                final_cut += value*value2  # result[i][j] += A[i][k] * B[k][j]

            if final_cut != 0:
                # print(f"Linia {i} coloana {j} {final_cut}")
                valoare_ls = [final_cut, j]
                result_matrix[i].append(valoare_ls)

                # iterate through rows of X
    return result_matrix


def multiply_matrix(Matrix, a, b, c):
    result_matrix = []
    empty_list = []
    for __ in range(0, len(Matrix)):
        result_matrix.append(empty_list)

    for i in range(0, len(Matrix)):
        row = get_line_matrix(Matrix, i)

        length_a = len(a)
        length_b = len(b)
        length_c = len(c)
        for j in range(0, len(Matrix)):
            # result[i][j] += A[i][k] * B[k][j]
            final_cut = 0
            counter_a = 0
            counter_b = 0
            counter_c = 0
            for k in range(0, len(Matrix)):
                value = get_value(row, k)  # A[i][k] - in mod normal
                if k == j and counter_a < length_a:
                    value2 = a[counter_a]
                    counter_a += 1
                elif k+1 == j and counter_b < length_b:
                    # Obtinem B[k][j] in functie de vectorii salvati si relatiile dintre indexii lor
                    value2 = b[counter_b]
                    counter_b += 1              #
                elif k == k+1 and counter_c < length_c:
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


def check_matrix(arr, file_name):
    f = open(file_name, "r")
    n = int(f.readline())
    i = 0  # verifica cele doua matrici
    E = 10 ** (-15)
    for line in f:
        values = [float(value)
                  for value in line.strip().split(',') if value != '']
        for elements in arr[int(values[1])]:
            if(elements[1] == int(values[2])):
                if elements[0] != values[0]:
                    if abs(float(elements[0]) - values[0]) > E:
                        print("Am gasit un element care nu corespunde epislon:\n")
                        print(
                            f"element: LINIE {int(values[1])} valoare:{elements[1]} expected :{int(values[2])}")
    return True



def check_matrix_multiplication_equality(matrix1, matrix2):
    for line in range(len(matrix2)):
        for element in range(len(matrix2[line])):
            try:
                if matrix1[line][element][1] == matrix2[line][element][1]:
                    if matrix1[line][element][0] != matrix2[line][element][0]:
                        print(
                            f"Am gasit doua elemente diferite linia { line} coloana {matrix1[line][element][1]} valoarea1 {matrix1[line][element][0]} valoare2 {matrix2[line][element][0]}  ")

            except IndexError:
                pass
    return True


if __name__ == "__main__":
    a, b, c = read_up_b_matrix("b.txt")

    matrice = matrix_read_up_a("a.txt")
    matrice_suma = matrix_sum(matrice, a, b, c)

    if check_matrix(matrice_suma, "aplusb.txt"):
        print("Suma este ok ")

    prod = multiply_matrix_remaked(matrice, a, b, c)
    prod_fis = matrix_read_up_a("aorib.txt")

    if check_matrix_multiplication_equality(prod, prod_fis):
        print("Produsul este ok")
    # print(len(a))
    # print(len(b))
    # print(len(c))
    # print(len(matrice))

    # for line in range(40, 50):
    #     print(f"Line is {line}")
    #     line_o = get_line_matrix(matrice, line)
    #     print(line_o)

    # for column in range(100, 110):
    #     print(f"Column is {column}")
    #     column_o = get_column_matrix(matrice, column)
    #     print(column_o)
