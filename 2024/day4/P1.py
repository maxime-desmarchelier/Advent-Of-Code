matrix = []

word = ["X", "M", "A", "S"]

DIRECTIONS = [
    (-1, 0),  # top
    (0, 1),   # right
    (1, 0),   # bot
    (0, -1),  # left
    (-1, 1),  # top_right
    (-1, -1),  # top_left
    (1, 1),   # bot_right
    (1, -1)  # bot_left
]

def search_direction(grid, x, y, dx, dy, index):
    if index == 4:
        return 1

    new_x, new_y = x + dx, y + dy
    if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]):
        return 0

    if grid[new_x][new_y] == word[index]:
        return search_direction(grid, new_x, new_y, dx, dy, index + 1)

    return 0

def find_xmas(grid, x, y):
    if grid[x][y] != "X":
        return 0

    count = 0
    for dx, dy in DIRECTIONS:
        count += search_direction(grid, x, y, dx, dy, 1)
    return count


result = 0

with open("data.txt", "r") as file:
    for line in file:
        matrix = [line.strip() for line in file]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "X":
            result += find_xmas(matrix, i, j)

print(result)