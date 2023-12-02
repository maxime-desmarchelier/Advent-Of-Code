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
    return {"red": max([int(x) for x in red]) if red else 0, "blue": max([int(x) for x in blue]) if blue else 0,
            "green": max([int(x) for x in green]) if green else 0}


def getCubeSetPower(cube_set):
    return cube_set["red"] * cube_set["blue"] * cube_set["green"]


with open("data.txt", "r") as file:
    for game in file:
        gameId = getGameId(game)
        gameColors = getColorsCount(game)
        result += getCubeSetPower(gameColors)

print(result)
