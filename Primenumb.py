a = input("Введите 1 число: ")
a = int(a)
b = input("Введите 2 число: ")
b = int(b)
i = 0

if a <= 1:
    print("Не простое число")
elif a <= 3:
    print("Простое число")
if a%2 == 0 or a%3 == 0:
    print("Не простое число")
i = 5
while i * i <= a:
    if a % i == 0 or a % (i + 2) == 0:
        print("Не простое число")
    i += 6
print("Простое число")