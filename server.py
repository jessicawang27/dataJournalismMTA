from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__, static_url_path='', static_folder='static')
with open('data/life_expectancy.json', 'r') as f:
    data = json.load(f)

@app.route('/')
def index():
    return render_template('about.html')


@app.route('/borough')
def year():
    borough = request.args.get("borough")
    # print(data['years'])
    year_index = data['years'].index(year + '.00')

    year_data = {
        'United States': data['countries']['United States'][year_index],
        'Canada': data['countries']['Canada'][year_index],
        'Mexico': data['countries']['Mexico'][year_index]
    }
    sorted_year_data = [
        {'country': 'Canada', 'value': year_data['Canada']},
        {'country': 'United States', 'value': year_data['United States']},
        {'country': 'Mexico', 'value': year_data['Mexico']}
    ]
    if sorted_year_data[0]['value'] < sorted_year_data[1]['value']:
        temp = sorted_year_data[0]
        sorted_year_data[0] = sorted_year_data[1]
        sorted_year_data[1] = temp

    if sorted_year_data[0]['value'] < sorted_year_data[2]['value']:
        temp = sorted_year_data[0]
        sorted_year_data[0] = sorted_year_data[2]
        sorted_year_data[2] = temp

    if sorted_year_data[1]['value'] < sorted_year_data[2]['value']:
        temp = sorted_year_data[2]
        sorted_year_data[2] = sorted_year_data[1]
        sorted_year_data[1] = temp

    mean_value, max_value, min_value = important_values()
    return render_template('year.html', year_data=year_data, max=max_value, min=min_value, year=year,sorted_year_data=sorted_year_data)


app.run(debug=True)