from flask import Flask,request,jsonify,render_template
import numpy as np
import pickle
import os

app = Flask(__name__,template_folder=templates)

port=int(os.environ.get("PORT",5000))

@app.rout('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True,port=port)