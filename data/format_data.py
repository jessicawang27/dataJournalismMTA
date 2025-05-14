import json

f1 = open("subway_data_cleansed.csv", "r")
lines = f1.readlines()

dictionary = {
    'borough' : [],
    'stop' : []
}


for i in range(1, len(lines)):
    line = lines[i].replace("\n","").split(",")
    dictionary['borough'].append(line[0])
    dictionary['stop'].append(line[1])

f1.close()

# #Save the json object to a file
f2 = open("life_expectancy.json", "w")
json.dump(dictionary, f2, indent = 4)
f2.close()