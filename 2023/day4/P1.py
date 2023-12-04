import re

pattern = re.compile(r"Card\s*(\d+):\s*([\d\s]+)\|\s*([\d\s]+)")

result = 0

with open("data.txt", "r") as file:
    for card in file:
        pattern_match = pattern.match(card)

        if pattern_match is None:
            continue

        pattern_groups = pattern_match.groups()

        winners = set(pattern_groups[1].split())
        mines = set(pattern_groups[2].split())

        result += 2 ** len(winners.intersection(mines)) // 2

print(result)


