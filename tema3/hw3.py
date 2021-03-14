
#read up for a.txt matrix 
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


if __name__ == "__main__":
    print("it will run from main program\n   ")
    matrix_read_up("a.txt")
