import re
import math

with open("data.txt", "r") as file:
    game_data = [line.strip() for line in file]

size = {"x": len(game_data[0]), "y": len(game_data)}

pattern = re.compile(r"([0-9]+)")

result = 0


def check_surrounding(gear_coords):
    neighbours = set()
    x, y = gear_coords

    # check left and right
    for number in re.finditer(pattern, game_data[y]):
        num_start, num_end = number.span()
        if x in (num_start - 1, num_end):
            neighbours.add(int(number.group()))

    # check up and down (including diagonals)
    for dy in [-1, 1]:
        if 0 <= y + dy < size['y']:
            for number in re.finditer(pattern, game_data[y + dy]):
                num_start, num_end = number.span()
                if x in range(num_start - 1, num_end + 1):
                    neighbours.add(int(number.group()))

    return 0 if len(neighbours) <= 1 else math.prod(neighbours)


for i in range(size["y"]):
    for gear in re.finditer(r"\*", game_data[i]):
        result += check_surrounding((gear.start(), i))

print(result)
