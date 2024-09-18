A = int(input("Введіть число A: "))
B = int(input("Введіть число B: "))
C = int(input("Введіть число C: "))
D = int(input("Введіть число D: "))
numbers = [A, B, C, D]

def checkNum(nums):
    divisible = False
    evenNum = False
    for num in nums:
        if num % 5 == 0:
            divisible = True
        if num % 2 == 0:
            evenNumber = True
        if divisible and evenNumber:
            return True
    return False

if checkNum(numbers):
    print("Одне з чисел ділиться на 5, а інше є парним")
else:
    print("Умова не виконана!")
