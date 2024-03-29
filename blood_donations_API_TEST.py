# Simple Post Request to test the API
"""
    On prompt run: python blood_donations_API_TEST.py

    list(list) -> list

    data = [[2, 15, 30, 90.134544]]
    [1]
    data = [[2	5	16	7.130899]]
    [0]
"""

import requests
import json

# Post Request on an API hosted on my local machine.
url = 'http://10.1.3.214:5000/api/'

# Individual that will be predicted upon. And the columns of the list are: Recency, Frequency, Monetary Value.
data = [[2, 5, 16, 7.130899]]

# Converting to json.
j_data = json.dumps(data)

# Sending the post Request.
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
# Showing the Request Response.
print(r, r.text)

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