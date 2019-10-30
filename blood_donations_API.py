# Run Flask and imports the model previously built on the blood_donations_model notebook.

# Imports
from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import numpy as np
import pickle as p
import json

import requests


app = Flask(__name__)

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def root():
    print form.errors
    if request.method == 'POST':
        name=request.form['name']
        print name

    if form.validate():
        # Save the comment here.
        flash('Hello ' + name)
    else:
        flash('All the form fields are required. ')

    return render_template('hello.html', form=form)


""" How to show the result of the predictions.
@app.route('/')
def root():
    url = 'http://10.1.3.214:5000/api/'
    data = [[2, 5, 16, 7.130899]]
    j_data = json.dumps(data)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=j_data, headers=headers)

    return r.text # The prediction.
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

