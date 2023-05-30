from flask import *
import numpy as np
import os
import pandas as pd
import pickle
import sklearn
from sklearn.preprocessing import OneHotEncoder
data = pd.read_csv("Cleaned_data.csv")

model = pickle.load(open('bangalore.pkl','rb'))

app = Flask(__name__)
port = int(os.environ.get("PORT",5001))
@app.route('/')
def home():
    locations = sorted(data['location'].unique())
    return render_template('index.html',locations=locations)

@app.route('/predict', methods=["POST"])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('BHK')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')
    input_data = pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    prediction = model.predict(input_data)[0]
    return str(np.round(prediction))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=port)