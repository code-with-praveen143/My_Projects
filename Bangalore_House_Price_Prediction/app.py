from flask import *
import numpy as np
import os


app = Flask(__name__)
port = int(os.environ.get("PORT",3000))
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=port)