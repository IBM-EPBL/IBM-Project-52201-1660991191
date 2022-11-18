import numpy as np
import flask
from flask import Flask, render_template, request, jsonify
import pickle
import inputScript


app = Flask(__name__)

model = pickle.load(open('Phishing_Website.pkl','rb'))


@app.route('/predict')

def predict():
    return flask.render_template('final.html')

@app.route('/y_predict', methods = ['POST'])

def y_predict():

    url = request.form['URL']
    checkprediction = inputScript.main(url)
    prediction = model.predict(checkprediction)
    output = prediction[0]
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
    app.run('0.0.0.0',debug=True)    