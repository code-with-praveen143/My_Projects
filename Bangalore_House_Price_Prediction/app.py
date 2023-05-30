from flask import *
import numpy as np
import os
import pandas as pd

data = pd.read_csv("Cleaned_data.csv")



app = Flask(__name__)
port = int(os.environ.get("PORT",3000))
@app.route('/')
def home():
    locations = sorted(data['location'].unique())
    return render_template('index.html',locations=locations)



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=port)