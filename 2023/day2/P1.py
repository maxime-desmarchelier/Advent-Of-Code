import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

game_id_pattern = re.compile(r"Game ([0-9]+)")
red_pattern = re.compile(r"([0-9]+) red")
blue_pattern = re.compile(r"([0-9]+) blue")
green_pattern = re.compile(r"([0-9]+) green")

result = 0


def getGameId(game_data):
    return int(game_id_pattern.findall(game_data)[0])


def getColorsCount(game_data):
    red = red_pattern.findall(game_data)
    blue = blue_pattern.findall(game_data)
    green = green_pattern.findall(game_data)
    return {
        "red": int(red[0]) if red else 0,
        "blue": int(blue[0]) if blue else 0,
        "green": int(green[0]) if green else 0
    }


def isSubsetValid(game_data):
    colors = getColorsCount(game_data)
    return colors["red"] <= MAX_RED and colors["blue"] <= MAX_BLUE and colors["green"] <= MAX_GREEN


with open("data.txt", "r") as file:
    for game in file:
        gameId = getGameId(game)
        gameValid = True
        for subset in game.split(";"):
            if not isSubsetValid(subset):
                gameValid = False
                break

        if gameValid:
            result += gameId

print(result)
