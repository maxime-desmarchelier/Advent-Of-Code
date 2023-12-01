result = 0
with open("data.txt", "r") as file:
    for line in file:
        digits = [s for s in line if s.isdigit()]

        if not digits:
            continue

        first_digit = last_digit = digits[0]
        if len(digits) > 1:
            last_digit = digits[-1]

        result += int(first_digit + last_digit)

print(result)
