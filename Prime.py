a = input("Введите первое число: ")
b = input("Введите второе число: ")
a = int(a)
b = int(b) 
 
print("Простые числа: ") 
for number in range(a, b + 1): 
    if number > 1: 
        for i in range(2, number): 
            if(number % i) == 0: 
                break 
        else: 
            print(number) 