import random

b = random.randrange(10)
while True:
    a = input("Введите число от 1 до 10 ")
    a = int(a)
    if a == b:
        print("Вы угадали!") 
        break
    elif a > b: 
            print("Ваше число больше загадонного")  
    elif a < b: 
            print("Ваше число меньше загадонного") 
    else:
        print("Попробуйте ещё раз: ")