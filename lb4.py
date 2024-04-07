num = int(input("Введите целое число больше 1: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Число не является простым")
            break
    else:
        print("Число является простым")
else:
    print("Введите число больше 1")