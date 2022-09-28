# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0, 56 -> 11

def summa(num):
    number = int(num.replace('.', ''))
    sum_num = 0
    while number > 0:
        sum_num += number % 10
        number //= 10
    return sum_num


number = input("Введите число: ")
print(summa(number))