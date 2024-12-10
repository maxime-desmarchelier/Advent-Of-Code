import re

def calculate_multiplication(line):
    findings = re.findall(r"mul\((\d+),(\d+)\)", line)
    total = 0
    for num1, num2 in findings:
        total += int(num1) * int(num2)
    return total

with open("data.txt", "r") as file:
    content = file.read().strip()
    result = 0

    # Split content by "don't()" sections
    sections = content.split("don't()")

    # Process first section (initially enabled)
    result += calculate_multiplication(sections[0])

    # Process remaining sections
    for section in sections[1:]:
        # On recherche un do()
        enabled_sections = section.split("do()")[1:]
        for enabled_section in enabled_sections:
            result += calculate_multiplication(enabled_section)

print(result)
