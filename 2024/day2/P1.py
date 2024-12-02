def is_valid_sequence(a, b, is_positive):
    diff = a - b
    if abs(diff) > 3 or abs(diff) < 1 or diff == 0:
        return False

    new_positive = diff > 0
    return is_positive == new_positive

with open("data.txt", "r") as file:
    reports = [[int(num) for num in line.strip().split()] for line in file]

    total = 0
    for report in reports:
        is_positive = report[0] - report[1] > 0
        is_valid = True

        for i in range(len(report) - 1):
            if not is_valid_sequence(report[i], report[i + 1], is_positive):
                is_valid = False
                break

        if is_valid:
            total += 1

    print(total)

