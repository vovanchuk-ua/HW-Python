x = float(input("Введіть x: "))

def findY(x):
    if x <= -1:
        y = (1 + abs(x)) / (1 + x + x**2)**1/3
    else:
        y = (1 + math.cos(x)**4) / (3 + x)
    return y

result = findY(x)
print("Для x = ", x, "значення функції y = ", result)
