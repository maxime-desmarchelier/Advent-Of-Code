def split_array(array):
    numbers_left = [row[0] for row in array]
    numbers_right = [row[1] for row in array]
    return numbers_left, numbers_right

with open("data.txt", "r") as file:
    # Remove \n and split the line to get the two numbers
    rows = [line.strip().split() for line in file]

    # Split the array into two arrays, one for each column
    left, right = split_array(rows)

    # Sort the arrays
    left.sort()
    right.sort()

    total = 0
    for i in range(len(left)):
        # Add the absolute difference (distance) between the two numbers
        total += abs(int(left[i]) - int(right[i]))

    print(total)

