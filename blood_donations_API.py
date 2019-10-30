# Run Flask and imports the model previously built on the blood_donations_model notebook.

# Imports
from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, FloatField, validators
from flask_wtf import Form
import numpy as np
import pickle as p
import json

# App config.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ML'

class LoginForm(FlaskForm):
    Recency = FloatField('recency')
    Frequency = FloatField('frequency')
    Time = FloatField('time')
    Monetary = FloatField('monetary')

@app.route('/form', methods=["GET", "POST"])
def form():
    form = LoginForm()
    return render_template('form.html', form=form)

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

