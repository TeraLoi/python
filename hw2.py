# 1 задание
my_list = [1, 'god', 1.25, 1 + 25j, -2, [6, -5], ("god", 6), None, False, {1: 2}]


def type_list(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


type_list(my_list)

# 2 задание
el_count = int(input("Введите количество чисел "))
my_list = []
i = 0
el = 0
while i < el_count:
    el = input("Введите элемент списка ")
    my_list.append(el)
    i += 1

for i in range(0, len(my_list) - 1, 2):
    str(my_list)
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

# 3 задание
seasons = {
    1: "зима",
    2: "весна",
    3: "лето",
    4: "осень",
}
season_list = ["winter", "spring", "summer", "autumn"]
month = int(input('ведите цифру от 1 до 12 '))
if month == 12 or month == 1 or month == 2:
    print(seasons.get(1))
    print(season_list[0])
if month == 3 or month == 4 or month == 5:
    print(seasons.get(2))
    print(season_list[1])
if month == 6 or month == 7 or month == 2:
    print(seasons.get(3))
    print(season_list[2])
if month == 9 or month == 10 or month == 11:
    print(seasons.get(4))
    print(season_list[3])

# 4 задание
my_str = input("введите предлложение ")
my_list = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_list = my_str.split()
    if len(str(my_list)) > 10:
        print(f" {num} {my_list[el] [0:10]}")
        num += 1

    else:
        print(f" {num} {my_list[el]}")
        num += 1

# 5 задание
digit = [7, 5, 3, 3, 2]
n = int(input("Введите количество вводимых чисел для добавления в рейтинг "))
i = 0
while n != i:
    number = int(input(f"Введите число {i+1} "))
    digit.append(number)
    i += 1

print(sorted(digit, reverse=True))

# 6 задание
HELP = """
    help = справка
    exit = выход
    add = добавить товар
    analytics = запрос аналитики товаров
    goods = запрос списка товаров
"""
goods = []
analytics = {
            "название": [],
            "цена": [],
            "количество": [],
            "ед": []
        }
run = True
while run:
    command = input('Введите команду или help ')
    if command == "exit":
        print("До скорого!")
        break
    elif command == "help":
        print(HELP)
    elif command == "add":
        code = input("Введите код товара ")
        title = input("Введите название товара ")
        price = input("Введите цену товара ")
        number = input("Введите количество товара в единице ")
        units = input("Введите количество единиц товара ")
        goods.append(
            (code,
             {
                 "название": title,
                 "цена": price,
                 "количество": number,
                 "ед": units
             })
        )
        analytics["название"].append(title)
        analytics["цена"].append(price)
        analytics["количество"].append(number)
        analytics["ед"].append(units)
    elif command == "analytics":
        print(analytics)
    elif command == "goods":
        print(goods)
else:
    print("Неизвестная команда")

