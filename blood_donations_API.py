# Run Flask and imports the model previously built on the blood_donations_model notebook.

# Imports
from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, FloatField, validators
from wtforms.validators import InputRequired, NumberRange
from flask_wtf import Form
import numpy as np
import pickle as p
import json

# App config.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ML'

class LoginForm(FlaskForm):
    Recency = FloatField('recency', 
                            validators=[InputRequired(), 
                            NumberRange(min=0, max=100)],
                            message="Recency must be between 0 and 500")

    Frequency = FloatField('frequency', 
                                validators=[InputRequired(), 
                                NumberRange(min=0, max=500)],
                                message="Frequency must be between 0 and 500")

    Time = FloatField('time', 
                        validators=[InputRequired(), 
                        NumberRange(min=0, max=500)],
                        message="Time since last donation must be between 0 and 500")

    Monetary = FloatField('monetary', 
                            validators=[InputRequired(), 
                            NumberRange(min=0, max=1000)],
                            message="Monetary must be between 0 and 500")

@app.route('/form', methods=["GET", "POST"])
def form():
    form = LoginForm()
    
    if form.validate_on_submit():
        return f"<h1>The data provided is {form.Recency.data}, {form.Frequency.data}, {form.Time.data}, {form.Monetary.data}<h1>"
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

