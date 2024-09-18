def isValidNumber(n):
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5
    return n == 1

N = int(input("Введіть натуральне число N: "))

validNumbers = []

for i in range(1, N + 1):
    if isValidNumber(i):
        validNumbers.append(i)

print("Числа, дільниками яких є тільки 2, 3 або 5:")
print(validNumbers)
print(len(validNumbers))
