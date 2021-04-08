def draw_field(data):
    print(" " * 4 + "   ".join([str(i) for i in range(size)]))
    print(" ", "+---" * size + "+")
    for i, line in enumerate(data):
        print(str(i) + " | " + " | ".join(line) + " |")
        print("  " + "+---" * size + "+")


def draw_welcome():
    s = """
    \tДобро пожаловать.
    \tКоординаты вводятся через пробел в формате "X Y"
    """
    print(s)


def coordinates():
    while True:
        x, y = input("\tВведите координаты X Y: ").split()

        if not (x.isdigit()) or not (y.isdigit()):
            print("\t\tОшибка, введены не числа.")
            continue

        x, y = int(x), int(y)

        if not (0 <= x < size) or not (0 <= y < size):
            print("\t\tОшибка, координаты за пределами поля.")
            continue

        if field[x][y] in signs:
            print("\t\tОшибка, ячейка уже занята.")
            continue

        return x, y


def check_for_win():
    # rows
    for_check = field.copy()

    # cols
    field_flat = []
    for col in field:
        field_flat.extend(col)
    for i in range(size):
        col = [x for indx, x in enumerate(field_flat) if indx % size == i]
        for_check.append(col)

    # diags
    diag1 = []
    diag2 = []
    for i, line in enumerate(field):
        diag1.append(line[i])
        diag2.append(line[-1 - i])
    for_check.append(diag1)
    for_check.append(diag2)

    # check for winners
    for line in for_check:
        if len(list(set(line))) == 1 and line[0] in signs:
            return line[0]
    else:
        return None


size = int(input("Введите размер стороны поля:"))
field = [[" " for _ in range(size)] for _ in range(size)]
signs = ["X", "O"]
turn = 0

draw_welcome()
while True:
    turn += 1
    draw_field(field)
    sign = signs[turn % 2]
    print(f"\tХодит '{sign}'")

    if turn > size ** 2:
        draw_field(field)
        print("\tНичья")
        break

    x, y = coordinates()

    field[x][y] = sign
    win = check_for_win()
    if win is not None:
        draw_field(field)
        print(f"\n\tПобедил '{win}'")
        break
