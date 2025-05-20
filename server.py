from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__, static_url_path='', static_folder='static')
with open('data/subway_data.json', 'r') as f:
    data = json.load(f)

@app.route('/')
def about():
    
    return render_template('about.html')

@app.route('/all_boroughs')
def all_boroughs():
    boroughs=[x for x in data]
    return render_template('all_boroughs.html',boroughs=boroughs)

@app.route('/borough')
def borough():
    borough = request.args.get("borough")
    return render_template('borough.html',borough=borough)

app.run(debug=True)