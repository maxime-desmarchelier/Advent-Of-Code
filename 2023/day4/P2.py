import re
from collections import defaultdict

pattern = re.compile(r"Card\s*(\d+):\s*([\d\s]+)\|\s*([\d\s]+)")

result = 0
copy = defaultdict(lambda: 0)

with open("data.txt", "r") as file:
    for card in file:
        pattern_match = pattern.match(card)

        if pattern_match is None:
            continue

        card_number, winners, mines = pattern_match.groups()
        card_number = int(card_number)
        winners_set = set(winners.split())
        mines_set = set(mines.split())

        matches = len(winners_set.intersection(mines_set))

        copy[card_number] += 1
        if matches > 0:
            for i in range(1, matches + 1):
                copy[card_number + i] += copy[card_number]

result = sum(copy.values())
print("Total:", result)
