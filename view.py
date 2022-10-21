import os


def clear(): return os.system('cls')


def GetInt(msg):
    try:
        return int(input(msg))
    except:
        return GetInt(msg)


def item_sel():
    clear()
    items = ["Ввести выражение для вычисления",
             "Посмотреть логи", "Очистить логи", "Выйти"]
    input = ""
    for i in range(len(items)):
        print(f"{i}: {items[i]}")
    print()
    while input not in range(len(items)) and input != -1:
        input = GetInt("Выбирите необходимую операцию: ")
    return input


def get_expr():
    clear()
    expr = input("Введите выражение: ")
    return expr


def show(string):
    print()
    print(string)
    print()