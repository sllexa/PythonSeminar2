# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.
def enter_coordinates(n, num):
    coord = []
    for i in range(n):
        coord.append(int(input(f"Введите координату {i + 1} для {num} точки: ")))
    return coord

def distance(n, a, b):
    dist = 0
    for i in range(n):
        dist += (b[i] - a[i]) ** 2
    dist **= 0.5
    return dist

n = int(input("Введите размерность пространства: "))
a = enter_coordinates(n, 1)
b = enter_coordinates(n, 2)
dist = distance(n, a, b)
print(round(dist, 2))