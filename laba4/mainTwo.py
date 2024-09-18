def createAndSortMatrix():
    n = int(input("Введіть розмірність матриці n: "))
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Введіть елементи {i + 1} рядка: ").split()))
        matrix.append(row)
    diagonalS = [matrix[i][n - i - 1] for i in range(n)]
    #print(diagonalS)
    diagonalS.sort()
    return matrix, diagonalS

def findMaxOfMins(matrix):
    minElements = []
    for row in matrix:
        minElements.append(min(row))
    maxOfMins = minElements[0]
    for element in minElements:
        if element > maxOfMins:
            maxOfMins = element
    indices = []
    for i, row in enumerate(matrix):
        if min(row) == maxOfMins:
            indices.append((i, row.index(maxOfMins)))
    return maxOfMins, indices

matrix, diagonalS = createAndSortMatrix()
maxOfMins, indices = findMaxOfMins(matrix)

print(f"Елементи бічної діагоналі в порядку зростання: {diagonalS}")
print(f"Найбільший з найменших елементів: {maxOfMins}")
print(f"Індекси найбільшого з найменших елементів: {indices}")
