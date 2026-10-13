import math

def task_1():
    print(" Завдання 1 ")
    a = float(input("Введіть число a (в радіанах): "))

    z = math.cos(a) + math.cos(2 * a) + math.cos(6 * a) + math.cos(7 * a)

    print(f"Результат z({a}) = {z:.4f}\n")


task_1()