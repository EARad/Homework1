def window():
    print("     — — — → Y")
    print("     0 1 2")
    for i, row in enumerate(fild):
        arrow = "|"
        row_str = f"{arrow}  {i} {' '.join(row)}"
        print(row_str)
    print("↓")
    print("X")


def coordinates():
    while True:
        cords = input("Введите координаты X и Y:").split()

        if len(cords) == 1 and len(cords[0]) == 2:
            cords = [cords[0][0], cords[0][1]]

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if fild[x][y] != "-":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(fild[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

print("""
   Приветствую!
Давайте сыграем в
 крестики-нолики
-----------------
формат ввода Х и Y:
Х - строки
Y - столбцы
-----------------
""")
fild = [["-"] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    window()
    if count % 2 == 1:
        print(" Ходит Х")
    else:
        print(" Ходит 0")

    y, x = coordinates()

    if count % 2 == 1:
        fild[y][x] = "X"
    else:
        fild[y][x] = "0"

    if check_win():
        break

    if count == 9:
        print("Ничья!")
        break
