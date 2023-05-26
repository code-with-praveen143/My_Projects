import json
import pickle
import sklearn
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__,template_folder='templates')
## Load the model
model=pickle.load(open('house.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    flask_prediction = model.predict(final_features)
    output = int(flask_prediction[0])
    return render_template("home.html",prediction_text=output)

if __name__=="__main__":
    app.run(debug=True)
   