import pickle
from flask import Flask,render_template,request,app,jsonify,url_for
import pandas
import numpy
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

model = pickle.load(open("model.pkl",'rb'))
scalar = pickle.load(open("scaling.pkl",'rb'))



@app.route("/")

def home():
    return "<h1>Hello World</h1>"

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(new_data)
    print(output[0])
    return jsonify(output[0])


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)