def task_3():
    print(" Завдання 3 ")
    
   
    raw_input = input("Введіть цілі числа через пробіл (наприклад: 5 -3 4 -12 8 -1 0): ")
    array = [int(x) for x in raw_input.split()]
    
    print(f"Початковий масив: {array}")

   
    positive_elements = [x for x in array if x > 0]
    if positive_elements:
        max_positive = max(positive_elements)
        print(f"Максимальний додатний елемент: {max_positive}")
    else:
        print("Додатних елементів у масиві немає.")


    positive_even_sum = sum(x for x in array if x > 0 and x % 2 == 0)
    print(f"Сума додатних парних елементів: {positive_even_sum}")

 
    negative_elements = [x for x in array if x < 0]
    reversed_negatives = negative_elements[::-1]
    
    print(f"Від'ємні елементи у зворотному порядку: {reversed_negatives}\n")

