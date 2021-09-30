#1 задание

def my_function():
    a = int(input("Введите первое число "))
    b = int(input("Введите второе число "))
    if b == 0:
        print("Ошибка! Целочисленное деление на 0 невозможно")
    else:
        return a / b


print("Результат ", my_function())

#2 задание

def second_func():
    name = input('Введите имя ')
    surname = input('Введите фамилию ')
    year = input('Введите год рождения ')
    city = input('Введите город ')
    email = input('Введите email ')
    phone = input('Введите номер телефона ')
    return f"имя {name} фамилия {surname} год рождения {year} город {city}  почта {email} телефон {phone}"


print(second_func())


#3 задание

a, b, c = map(int, input('Введите 3 числа через пробел ').split())


def my_func():
    if (a >= b > c) or (b > a >= c):
        return a + b
    elif (a < c <= b) or (a < b <= c):
        return b + c
    elif a == b == c:
        print("Все равны")
    elif (a > b == c) or (c == a < b) or (a == b < c):
        print("е соответствует условию задачи для дальнейшей операции")
    else:
        return a + c


print(my_func())

#4 задание

def x_pow():
    x = int(input("Введите первое число "))
    y = int(input("Введите второе число "))
    return x**y
print(x_pow())

def x_pow():
    number = int(input("Введите число "))
    n = int(input("Введите степень "))
    i = 1
    result = 1
    while i <= n:
        result *= number
        i += 1
    return result


print(x_pow())


#5 задание

def summa():
    sum_result = 0
    running = False
    while running == False:
        number = input('Выход - q. Введите последовательность: ').split()
        result = 0
        for el in range(len(number)):
            if number[el] == 'q':
                running = True
                break
            else:
                result = result + int(number[el])
        sum_result = sum_result + result
        print(f'Current sum is {sum_result}')
    print(f'Your final sum is {sum_result}')


summa()


#6-7 задание
def my_func():
    my_str = input("Введите слово или предложение ")
    print(my_str.title())
    return


my_func()

