import math

N = 41
a = 0
b = math.pi
h = (b - a) / (N - 1)
y_values = []

print("Цикл For")
for x in range(N):
    y = 2 * math.sin(2 * x * h) - 1.5 * x * h
    y_values.append(y)
    print(f"x = {x*h:.3f}, y = {y:.3f}")

print("\nЦикл While:")
x = a
i = 0
while i < N:
    y = 2 * math.sin(2 * x) - 1.5 * x
    y_values.append(y)
    print(f"x = {x:.3f}, y = {y:.3f}")
    x += h
    i += 1

print("\nІмітація циклу do-while:")
x = a
i = 0
while True:
    y = 2 * math.sin(2 * x) - 1.5 * x
    y_values.append(y)
    print(f"x = {x:.3f}, y = {y:.3f}")
    x += h
    i += 1
    if i >= N:
        break
