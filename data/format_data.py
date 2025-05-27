import json

f1 = open("subway_data_cleansed.csv", "r")
lines = f1.readlines()[1:]

boroughs = {
    'M' : [],
    'B' : [],
    'Q' : [],
    'Bx' : [],
    'SI' : []
}

shorthand = {
    'M' : 'Manhattan',
    'B' : 'Brooklyn',
    'Q' : 'Queens',
    'Bx' : 'The Bronx',
    'SI' : 'Staten Island'
}

for i in range(1, len(lines)):
    line = lines[i].replace("\n","").split(",")
    boroughs[line[0]].append(line[1])

f1.close()

subways = {}
for line in lines:
    infos = line.split(",")
    share_lines = infos[2].replace("\n","").split(" ")
    for line in share_lines:
        if line not in subways.keys():
            subways[line] = [infos[1]]
        elif infos[1] not in subways[line]:
            subways[line].append(infos[1])

data = {
    'boroughs':boroughs,
    'shorthand':shorthand,
    'subways':subways
}
