# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiplication(n):
    multipl = [1]
    for i in range(2, n + 1):
        multipl.append(multipl[-1] * i)
    return multipl


n = int(input("Введите число N: "))
print(multiplication(n))
