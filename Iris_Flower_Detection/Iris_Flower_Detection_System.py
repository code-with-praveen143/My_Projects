from flask import Flask,jsonify,render_template,request
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv("E:\\Datasets\\iris_data.csv")
print(df.head())
x=np.array(df.iloc[:,0:4])
y=np.array(df.iloc[:,5:])
 
#print(y.shape)
from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
y=label.fit_transform(y)

X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2,random_state=2)
#print(y)
from sklearn.svm import SVC
iris=SVC(kernel="linear")
iris.fit(X_train,Y_train)
y_pred=iris.predict(X_test)
from sklearn.metrics import accuracy_score
testing_accuracy=accuracy_score(y_pred,Y_test)
print("testing accuracy score is :" , testing_accuracy)
data=np.array([[5.1,3.5,1.4, 0.2]])
result=iris.predict(data)
print("the predicted output of our model is :", result)


import pickle
pickle.dump(iris,open('iris.pkl','wb'))


model=pickle.load(open('iris.pkl','rb'))
app=Flask(__name__)
port=int(os.environ.get("PORT",5000))

 
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/predict',methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    flask_prediction = iris.predict(final_features)
    if(flask_prediction[0] == 0):
        return render_template('home.html',prediction_text="It is a Iris-Setosa")
    elif(flask_prediction[0] == 1):
        return render_template('home.html',prediction_text="It is a Iris-Versicolor")
    else:
        return render_template('home.html',prediction_text="It is a Iris-Virginica")



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=port)