dicto = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def getFirst(line):
    for idc, c in enumerate(line):
        if c.isdigit():
            return c, line[idc + 1:]
        for key in dicto.keys():
            if c == key[0]:
                if line[idc:idc + len(key)] == key:
                    return str(dicto[key]), line[idc + len(key):]

    return -1, ""


def getLast(line):
    for idc in range(len(line) - 1, -1, -1):
        c = line[idc]
        if c.isdigit():
            return c
        for key in dicto.keys():
            if idc >= len(key) - 1 and c == key[-1]:
                if line[idc - len(key) + 1:idc + 1] == key:
                    return str(dicto[key])

    return -1


with open("data.txt", "r") as file:
    result = 0
    for currentLine in file:
        first, remains = getFirst(currentLine)

        if first == -1:
            continue

        last = getLast(remains)

        if last == -1:
            last = first

        result += int(str(first) + str(last))
    print(result)
