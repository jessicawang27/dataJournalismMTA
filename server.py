from flask import Flask
from flask import render_template
from flask import request
import json
from jinja2 import FileSystemLoader

app = Flask(__name__, static_url_path='', static_folder='static')
app.jinja_loader = FileSystemLoader(['templates', 'data'])
with open('data/subway_data.json', 'r') as f:
    data = json.load(f)

@app.route('/')
def about():
    
    return render_template('about.html')

@app.route('/all_boroughs')
def all_boroughs():
    boroughs = [{'name': key, 'value': len(data['boroughs'][key])} for key in data['boroughs'].keys()]

    for i in range(len(boroughs) - 1):
        for j in range(len(boroughs) - i - 1):
            if boroughs[j]['value'] < boroughs[j + 1]['value']:
                boroughs[j], boroughs[j + 1] = boroughs[j + 1], boroughs[j]

    pure_data = {key:len(data['boroughs'][key]) for key in data['boroughs'].keys()}
    avg = sum(pure_data.values())/len(pure_data.values())
    # print(avg)
    return render_template('all_boroughs.html',
                           shorthand=data['shorthand'],
                           boroughs=boroughs,pure_data=pure_data,avg=avg,
                           max=boroughs[0]['value'], min=boroughs[-1]['value'])

@app.route('/borough')
def borough():
    borough = request.args.get("borough")
    if borough not in data['shorthand'].keys():
        borough = 'M'
    stops = data['boroughs'][borough]
    subways = data['subways']
    # the stops of each line
    amount_info = {key: 0 for key in subways}
    colors = [{'line': '1', 'bg': '1'}, {'line': '2', 'bg': '1'}, {'line': '3', 'bg': '1'},
              {'line': 'B', 'bg': '2'}, {'line': 'D', 'bg': '2'}, {'line': 'F', 'bg': '2'},{'line': 'M', 'bg': '2'},
              {'line': 'N', 'bg': '3'}, {'line': 'Q', 'bg': '3'}, {'line': 'R', 'bg': '3'},{'line': 'W', 'bg': '3'},
              {'line': '4', 'bg': '4'}, {'line': '5', 'bg': '4'}, {'line': '6', 'bg': '4'},
              {'line': 'G', 'bg': '5'},
              {'line': 'A', 'bg': '6'}, {'line': 'C', 'bg': '6'}, {'line': 'E', 'bg': '6'},
              {'line': '7', 'bg': '7'},
              {'line': 'L', 'bg': '8'},
              {'line': 'S', 'bg': '9'},
              {'line': 'J', 'bg': '10'}, {'line': 'Z', 'bg': '10'},
              {'line':'SIR','bg':'11'}]

    for st in stops:
        for key in subways:
            if st in subways[key]:
                amount_info[key] += 1

    pure_data = {key: len(data['boroughs'][key]) for key in data['boroughs'].keys()}
    avg = sum(pure_data.values()) / len(pure_data.values())
    stops = pure_data[borough]
    print(stops)
    return render_template('borough.html',
                           borough=data['shorthand'][borough],avg=avg,stops=stops,
                           amount_info=amount_info, colors=colors,   #extra_lines=extra_lines,
                           max=max(amount_info.values()), min=min(amount_info.values()))


app.run(debug=True)
