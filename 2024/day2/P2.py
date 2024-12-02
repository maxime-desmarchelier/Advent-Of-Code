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
        safe = True

        positive = report[0] - report[1] > 0
        for i in range(len(report) - 1):
            if not is_valid_sequence(report[i], report[i + 1], positive):
                safe = False
                break

        if not safe:
            # Brut force by removing one element and check if it's safe
            for j in range(len(report)):
                temp_report = report.copy()
                temp_report.pop(j)

                if len(temp_report) > 1:
                    temp_safe = True
                    positive = temp_report[0] - temp_report[1] > 0

                    for i in range(len(temp_report) - 1):
                        if not is_valid_sequence(temp_report[i], temp_report[i + 1], positive):
                            temp_safe = False
                            break

                    if temp_safe:
                        safe = True
                        break

        if safe:
            total += 1

    print(total)

