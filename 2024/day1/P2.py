def split_array(array):
    numbers_left = [row[0] for row in array]
    numbers_right = [row[1] for row in array]
    return numbers_left, numbers_right

with open("data.txt", "r") as file:
    # Remove \n and split the line to get the two numbers
    rows = [line.strip().split() for line in file]

    # Split the array into two arrays, one for each column
    left, right = split_array(rows)

    # Count the number of times each number appears in the right array
    dicto = {}

    for i in range(len(right)):
        if right[i] in dicto:
            dicto[right[i]] += 1
        else:
            dicto[right[i]] = 1

    total = 0
    for i in range(len(left)):
        # Multiply the left number by the number of times it appears in the right array
        if left[i] in dicto:
            total += int(left[i]) * int(dicto[left[i]])

    print(total)

