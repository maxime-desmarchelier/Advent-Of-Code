import re

with open("data.txt", "r") as file:
    game_data = [line.strip() for line in file]

size = {"x": len(game_data[0]), "y": len(game_data)}

pattern = re.compile(r"([0-9]+)")


def is_symbol(c):
    return not c.isdigit() and c != '.'


def check_surrounding(x, y):
    # Check left
    if x[0] > 0:
        if is_symbol(game_data[y][x[0] - 1]):
            return game_data[y][x[0]:x[1]]

    # Check right
    if x[1] < size["x"]:
        if is_symbol(game_data[y][x[1]]):
            return game_data[y][x[0]:x[1]]

    # Check up
    if y > 0:
        if any(is_symbol(c) for c in game_data[y - 1][x[0]:x[1]]):
            return game_data[y][x[0]:x[1]]
    # Check down
    if y < size["y"] - 1:
        if any(is_symbol(c) for c in game_data[y + 1][x[0]:x[1]]):
            return game_data[y][x[0]:x[1]]

    # Check up left
    if x[0] > 0 and y > 0:
        if any(is_symbol(c) for c in game_data[y - 1][x[0] - 1]):
            return game_data[y][x[0]:x[1]]
    # Check up right
    if x[1] < size["x"] and y > 0:
        if any(is_symbol(c) for c in game_data[y - 1][x[1]]):
            return game_data[y][x[0]:x[1]]

    # Check down left
    if x[0] > 0 and y < size["y"] - 1:
        if any(is_symbol(c) for c in game_data[y + 1][x[0] - 1]):
            return game_data[y][x[0]:x[1]]
    # Check down right
    if x[1] < size["x"] and y < size["y"] - 1:
        if any(is_symbol(c) for c in game_data[y + 1][x[1]]):
            return game_data[y][x[0]:x[1]]
    return 0


result = 0

for i in range(size["y"]):
    numbers = [[m.start(), m.end()] for m in pattern.finditer(game_data[i])]
    for number in numbers:
        result += int(check_surrounding(number, i))

print(result)
