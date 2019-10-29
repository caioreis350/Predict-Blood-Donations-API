# Run Flask and imports the model previously built on the blood_donations_model notebook.

# Imports
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)

# POST Method to predict data from the data input.
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

