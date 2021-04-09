#! /usr/bin/env python
# -*- coding: utf-8 -*-


def draw_field(play_progress):
    """Draw table with 'X' and 'O'
        0   1   2
      +---+---+---+
    0 | X |   |   |
      +---+---+---+
    1 |   | O | O |
      +---+---+---+
    2 |   |   |   |
      +---+---+---+

    Args:
        data (list of list): matrix with 'X' and 'O' positions
    """
    print(" " * 4 + "   ".join([str(indx) for indx in range(size)]))
    print(" ", "+---" * size + "+")
    for indx, line in enumerate(play_progress):
        print(str(indx) + " | " + " | ".join(line) + " |")
        print("  " + "+---" * size + "+")


def draw_welcome():
    """Draw Welcome info."""
    welcome_string = """
    \tДобро пожаловать.
    \tКоординаты вводятся через пробел в формате "X Y"
    """
    print(welcome_string)


def coordinates():
    """Getting desired cell from player.

    Returns:
        x, y (int, int): X and Y coordinates
    """
    while True:
        try:
            x, y = input("\tВведите координаты X Y: ").split()
        except ValueError:
            print("\t\tОшибка, нужно два числа.")
            continue

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


def check_for_winner(signs):
    """Who is th winner.

    Args:
        signs (list): List with plaeyr's signs, ['X','O'] usualy

    Returns:
        element of signs list or None: None if no winner yet, or player's sign
    """

    # rows
    for_check = field.copy()

    # cols
    field_flat = []
    for col in field:
        field_flat.extend(col)
    for col_number in range(size):
        col = [x for indx, x in enumerate(field_flat) if indx % size == col_number]
        for_check.append(col)

    # diags
    diag1 = []
    diag2 = []
    for row_number, line in enumerate(field):
        diag1.append(line[row_number])
        diag2.append(line[-1 - row_number])
    for_check.append(diag1)
    for_check.append(diag2)

    # check for winner
    for line in for_check:
        if len(list(set(line))) == 1 and line[0] in signs:
            return line[0]
    else:
        return None


def field_initialize():
    """Geetting field size from customer

    Returns:
        size (int): field size
    """
    while True:
        try:
            size = input("Введите размер стороны поля (от 3 до 9):")
        except ValueError:
            print("\t\tОшибка, нужно одно число")
            continue

        if not size.isdigit():
            print("\t\tОшибка, введено не числа.")
            continue

        size = int(size)

        if not 3 <= size <= 9:
            print("\t\tОшибка, размеры должны быть от 3 до 9")
            continue

        return size


if __name__ == "__main__":
    size = field_initialize()
    draw_welcome()
    field = [[" " for _ in range(size)] for _ in range(size)]
    signs = ["X", "O"]
    turn = 0
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
        winner = check_for_winner(signs)
        if winner is not None:
            draw_field(field)
            print(f"\n\tПобедил '{winner}'")
            break
