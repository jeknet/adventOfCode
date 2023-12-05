colors = {"red": "R", "green": "G", "blue": "B"}

def parse_set(set_info: str):
    set_data = {"R": 0, "G": 0, "B": 0}

    value = set_info.strip()
    cubes_info = value.split(",") 

    for cube_info in cubes_info:
        values = cube_info.strip().split() 
        set_data[colors[values[-1]]] += int(values[0])

    return set_data

def parse_game(line):
    game_values = line.split(":")
    id = int(game_values[0].split()[-1])
    game = {"id": id, "sets": []}
    sets = game_values[-1].strip().split(";") 

    for set_info in sets:
        game['sets'].append(parse_set(set_info))

    return game


def matches(game, combination):
    for set_info in game['sets']:
        for color, number in combination.items():
            if set_info[color] > number:
                return False
    
    return True


def powerNumber(sets):
    rMax = max([set_info.get('R',1) for set_info in sets])
    gMax = max([set_info.get('G',1) for set_info in sets])
    bMax = max([set_info.get('B',1) for set_info in sets])

    return rMax * gMax * bMax

def calcPower(line):
    game = parse_game(line)

    return powerNumber(game['sets'])

def play(path, comb):
    with open(path) as file:
        lines = file.readlines()
 
        response = 0
        for line in lines:
            game = parse_game(line)
            if matches(game, comb): 
                response += game['id'] 
        return response


def play2(path):
    with open(path) as file:
        lines = file.readlines()

        response = sum([calcPower(line) for line in lines])

        return response

source = "challenge2.txt"
print(play(source, {"R": 12, "G": 13, "B": 14}))
print(play2(source))
