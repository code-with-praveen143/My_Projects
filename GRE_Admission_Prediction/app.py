from flask import Flask,request,jsonify,render_template
import os
import pickle
import numpy as np
with open('model.pkl','rb') as file:
  model = pickle.load(file)
app = Flask(__name__)

port=int(os.environ.get("PORT",3000))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    output = str(int(prediction[0]*100))+"%"
    print("prediction is: ",prediction[0])
    return render_template('index.html',prediction_text=output)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=port)