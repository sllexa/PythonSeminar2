# Задача 3. Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами, выводится на экран, затем перемешивается, опять выводится на экран.
from random import randint

def fill_list(num):
    new_list = []
    for i in range(1, num):
        new_list.append(randint(0, 100))
        i += 1
    return new_list

def shuffle_list(user_list):
    for i in range(len(user_list) - 1, 0, -1):
        j = randint(0, i + 1)
        user_list[i], user_list[j] = user_list[j], user_list[i]
    return user_list

n = int(input("Введите размерность списка: "))
source_list = fill_list(n)
print(source_list)
print()
print(shuffle_list(source_list))