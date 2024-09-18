a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
c = float(input("Введіть значення c: "))
m = float(input("Введіть початок проміжку m: "))
n = float(input("Введіть кінець проміжку n: "))

def calculateY(a, b, c, x):
  numerator = a * (x**2 - b)
  denominator = b**2 * c**2 + 1
  return numerator / denominator

if m > n:
  print("Початкове значення проміжку більше за кінцеве!")
else:
    print("x\t\ty")
    for x in range(int(m), int(n) + 1):
        y = calculateY(a, b, c, x)
        print(f"{x}, \t, {y:.5f}")
