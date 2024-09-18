def reflectMatrixDiagonal():
    m = int(input("Введіть порядковий номер матриці m: "))
    matrix = []

    for i in range(m):
        inputRow = input(f"Введіть елементи {i + 1} рядка: ").split()
        row = []
        for item in inputRow:
            row.append(int(item))
        matrix.append(row)

    reflectedMatrix = []
    for i in range(m):
        newRow = []
        for j in range(m):
            newRow.append(matrix[j][i])
        reflectedMatrix.append(newRow)

    print("Матриця після дзеркального відображення відносно головної діагоналі: ")
    for row in reflectedMatrix:
        rowStr = ''
        for item in row:
            rowStr += str(item) + ' '
        print(rowStr.strip())
    return reflectedMatrix

reflectMatrixDiagonal()
