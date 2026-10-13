def task_2():
    print(" Завдання 2 ")
    n = int(input("Введіть натуральне число n: "))
    
    if n <= 0:
        print("Число n має бути натуральним (n >= 1).")
        return

    product = 1
    
    for i in range(1, 2 * n, 2):
        product *= i
        
    print(f"Добуток перших {n} непарних чисел = {product}\n")

