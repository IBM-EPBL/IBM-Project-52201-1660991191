import numpy as np
import flask
from flask import Flask, render_template, request, jsonify
import pickle
import inputScript
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "MhfsR6_OrmzdUJXZv0CEQQX8jtUSvZaf7lzNXN_GqZl4"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)

@app.route('/predict')

def predict():
    return flask.render_template('final.html')

@app.route('/y_predict', methods = ['POST'])

def y_predict():

    url = request.form['URL']
    checkprediction = inputScript.main(url)
    payload_scoring = {"input_data": [{"field": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/f824b4c2-e5cc-43f2-a58c-48f70a9c5ae1/predictions?version=2022-11-18', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions = response_scoring.json())
    output = predictions['predictions'][0]['Values'][0][0]
    if(output == 1):
        pred = "You are safe !!  This is a Legitimate Website."
    else:
        pred = "You are on the wrong site. Be caustion!"
    return render_template('final.html',prediction_text='{}'.format(pred),url=url)


@app.route('/predict_api',methods=['POST','GET'])
def predict_api():
    
    data = request.get_json()
    prediction = model.y_predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)



        
if __name__ == '__main__':
    app.run(host='127.0.0.1',port='5500',debug=True)    