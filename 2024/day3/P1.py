import re

total = 0
with open("data.txt", "r") as file:
    for line in file:
        findings = re.findall(r"mul\((\d+),(\d+)\)", line)
        for num1, num2 in findings:
            total += int(num1) * int(num2)

print(total)