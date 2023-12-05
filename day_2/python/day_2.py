"""
Module to hold the code for day 2.
"""

from collections import defaultdict
from math import prod

import re

MAX_VALUES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def _get_game_id(game_line: str) -> int:
    """
    Extract the game ID from the game line.
    """
    return int(game_line[4:9].split(":")[0].strip())

def _extract_colour(colour: str, game_line) -> list[int]:
    """
    Extract all the values for a given colour in a game line.
    """
    rtn = []
    # We need to add both , and ; to the end of the colour because the colour
    # could be at the end of the game.
    for match in re.finditer(fr"\d+ {colour}(,|;|)", game_line):
        rtn.append(int(match.group(0).split()[0]))
    return rtn

def _is_valid_game(game_line: str) -> bool:
    """
    Return True if the max number for each colour is under that the MAX_VALUES.
    """
    for colour, max_number in MAX_VALUES.items():
        colour_list = _extract_colour(colour=colour, game_line=game_line)
        if not colour_list:
            continue
        if max(colour_list) > max_number:
            return False
    return True

def _find_min_cubes(game_line: str) -> dict[str, int]:
    """
    Return the min value for each red, blue, green
    """
    rtn = defaultdict(int)
    rtn.update({'red': 0, 'green': 0, 'blue': 0})
    for colour in MAX_VALUES.keys():
        colour_list = _extract_colour(colour=colour, game_line=game_line)
        if not colour_list:
            continue
        rtn[colour] = max(colour_list)

    return rtn

def _get_power(game_line: str) -> int:
    """
    Times together all the minimum values for a valid game.
    """
    return prod(_find_min_cubes(game_line=game_line).values())

def _read_input(input_file_path: str) -> list[str]:
    input_data = []
    with open(input_file_path, 'r') as in_file:
        for line in in_file.readlines():
            input_data.append(str(line))
    return input_data

test_input = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green ',
]

real_input = _read_input(input_file_path='./ch_1_input.txt')

# valid_games = [_get_game_id(game_line=test) for test in real_input if _is_valid_game(game_line=test)]
# print(sum(valid_games))

power_games = [_get_power(game_line=test) for test in test_input]
print(sum(power_games))

power_games = [_get_power(game_line=test) for test in real_input]
print(sum(power_games))
