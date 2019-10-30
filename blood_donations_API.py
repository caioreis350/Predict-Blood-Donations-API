# Run Flask and imports the model previously built on the blood_donations_model notebook.

# Imports
from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import numpy as np
import pickle as p
import json

import requests


app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')
    
"""
@app.route('/')
def root():
    url = 'http://10.1.3.214:5000/api/'
    data = [[2, 5, 16, 7.130899]]
    j_data = json.dumps(data)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=j_data, headers=headers)

    return r.text
"""

# POST Method Calculation predict data from the data input.
@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

# Running the API no my Machine.
if __name__ == '__main__':
    modelfile = 'model_logreg.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(host='10.1.3.214')

