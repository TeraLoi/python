# 1
from sys import argv


script, working_out, hourly_rate, bonus = argv


def salary():
    print("Имя скрипта: ", script)
    print("Выработка в часах: ", working_out)
    print("Ставка в час : ", hourly_rate)
    print("Премия: ", bonus)
    result = working_out * hourly_rate + bonus
    return round(result)


print('заработная плата сотрудника', salary())

# 2
my_list = [15, 2, 3, 1, 7, 5, 4, 10]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')

# 3
print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

# 4
my_list = [5, 6, 2, 6, 8, 8, 9, 5, 1, 7]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

# 5
from functools import reduce


def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


print(my_func, [el for el in range(99, 1001) if el % 2 == 0])
print(reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0]))

# 6
from itertools import count

x_1 = int(input("Введите стартовое число "))
x_2 = int(input("Введите конечное число "))
for el in count(x_1):
    if el > x_2:
        break
    else:
        print(el)

from itertools import cycle

с = 0
for el in cycle([1, True, "ABC"]):
    if с > 10:
        break
    print(el)
    с += 1

# 7
from itertools import count
from math import factorial


n = int(input("n"))
def fact():
    for el in count(1):
        yield factorial(el)

g = fact()
x = 0
for i in g:
    if x < n:
        print(i)
        x += 1
    else:
        break
