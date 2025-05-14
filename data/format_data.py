import json

f1 = open("subway_data_cleansed.csv", "r")
lines = f1.readlines()

dictionary = {
    'M' : [],
    'B' : [],
    'Q' : [],
    'Bx' : [],
    'SI' : []
}


for i in range(1, len(lines)):
    line = lines[i].replace("\n","").split(",")
    if line[0] == 'M':
        dictionary['M'].append(line[1])
    elif line[0] == 'B':
        dictionary['B'].append(line[1])
    elif line[0] == 'Q':
        dictionary['Q'].append(line[1])
    elif line[0] == 'Bx':
        dictionary['Bx'].append(line[1])
    else: # Staten Island
        dictionary['SI'].append(line[1])

f1.close()

# #Save the json object to a file
f2 = open("life_expectancy.json", "w")
json.dump(dictionary, f2, indent = 4)
f2.close()