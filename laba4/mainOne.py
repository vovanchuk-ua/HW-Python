n = int(input("Введіть розмірність матриці n: "))
matrix = []

for i in range(n):
    row = list(map(int, input(f"Введіть елементи {i+1} рядка: ").split()))
    matrix.append(row)

diagonalS = [matrix[i][n - i - 1] for i in range(n)]
diagonalS.sort()

print("Елементи бічної діагоналі в порядку зростання:")
print(diagonalS)
