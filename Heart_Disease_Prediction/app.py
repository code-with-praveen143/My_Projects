from flask import Flask,request,jsonify,render_template
import numpy as np
import pickle
import os

model=pickle.load(open('heart.pkl','rb'))

app = Flask(__name__)

port=int(os.environ.get("PORT",5000))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    flask_prediction = model.predict(final_features)
    if(flask_prediction[0] == 1):
        return render_template("index.html",prediction_text="The Person has a Heart Disease")
    else:
        return render_template("index.html",prediction_text="The Person Doesn't has a heart disease")
if __name__ == "__main__":
    app.run(debug=True,port=port)