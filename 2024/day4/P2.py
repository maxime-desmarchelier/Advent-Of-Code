def find_xmas(grid, x, y):
    # Check not at the edge
    if x == 0 or x == len(grid)-1 or y == 0 or y == len(grid[0])-1:
        return 0

    count = 0

    # Check top-left(M) to bottom-right(S)
    if grid[x-1][y-1] == "M" and grid[x+1][y+1] == "S":
        count += 1

    # Check top-right(M) to bottom-left(S)
    if grid[x-1][y+1] == "M" and grid[x+1][y-1] == "S":
        count += 1

    # Check bottom-right(M) to top-left(S)
    if grid[x+1][y+1] == "M" and grid[x-1][y-1] == "S":
        count += 1

    # Check bottom-left(M) to top-right(S)
    if grid[x+1][y-1] == "M" and grid[x-1][y+1] == "S":
        count += 1

    return 1 if count == 2 else 0

result = 0

with open("data.txt", "r") as file:
    matrix = [line.strip() for line in file]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "A":
            result += find_xmas(matrix, i, j)

print(result)