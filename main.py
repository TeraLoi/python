HELP = """
    help = справка
    exit = выход
    1 = задача 1
    2 = задача 2
    3 = задача 3
    4 = задача 4
    5 = задача 5
    6 = задача 6
"""
run = True
while run:
    command = input('Введите команду или help ')
    if command == "exit":
        print("До скорого!")
        break
    elif command == "help":
        print(HELP)
    elif command == "1":
        a = int(input("Введите число a "))
        b = int(input("Введите число b "))
        print((a + b), (a * b), (a - b), (a // b), (a ** b))
        task = []
        tasks = []
        c = str(input("Введите слово  "))
        d = str(input("Введите слово "))
        e = int(input("Введите число  "))
        task.append(c)
        task.append(d)
        tasks.append(e)
        tasks.append(c)
        tasks.append(d)
        print(' '.join(task))
        print(tasks)

    elif command == "2":
        n = int(input("Введите время в секундах "))
        xx = n // 3600
        yy = (n - 3600 * xx) // 60
        cc = (n - 3600 * xx) - (60 * yy)
        print(f'{xx}:{yy}:{cc}')

    elif command == "3":
        n = int(input("Введите цифру  "))
        nn = int(str(n) + str(n))
        nnn = int(str(nn) + str(n))
        summa = n + nn + nnn
        print(f'{n} + {nn} + {nnn} = {summa}')

    elif command == "4":
        n = int(input("Введите число "))
        i = 0
        while n >= 9:
            N = n % 10
            n //= 10
            if N > i:
                i = N
        print(i)
    elif command == "5":
        proceeds = int(input("выручка "))
        costs = int(input("издержки "))
        result = proceeds - costs
        if result > 0:
            print(f'Прибыль {result}')
            rent = result / proceeds
            print('рентабельность выручки', round(rent, 2))
            amount = int(input("Введите число сотрудников "))
            RESULT = result // amount
            print('Прибыль в расчете на одного сотрудника', round(RESULT))

        elif result < 0:
            print('Убыток', abs(result))
        else:
            print('Выручка и издержки равны')
    elif command == "6":
        a = int(input("Введите число a "))
        b = int(input("Введите число b "))
        day = 1
        while a < b:
            a = a + (0.1 * a)
            day += 1
        print(f'на {day}-й день спортсмен достиг результата — не менее', round(a), 'км')

else:
    print("Неизвестная команда")
