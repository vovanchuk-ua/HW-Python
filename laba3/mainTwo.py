def sumOfSquares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

n = int(input("Введіть натуральне число n: "))

result = sumOfSquares(n)
print("Сума квадратів перших ", n, " натуральних чисел: ", result)
