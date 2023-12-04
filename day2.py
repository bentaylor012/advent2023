games = []
with open("day2input.txt") as file:
    for line in file:
        games.append(line)
gameDict = {}
rules = {'red': 12, 'green': 13, 'blue': 14}

#12 red cubes, 13 green cubes, and 14 blue cubes
total = 0
for game in games:
    gameNum = game.split(':')[0].split(' ')[1]
    gameStats = game.split(':')[1]
    cubes = gameStats.replace(';', ',').split(',')
    curGame = {}
    valid = True
    for cube in cubes:
        color = cube.split()[1]
        count = cube.split()[0]
        if (color not in rules.keys() or rules[color] < int(count)):
            print(color + ' not in rules')
            valid = False
            
    if valid:
        total = total + int(gameNum)

print(total)
