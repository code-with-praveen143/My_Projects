# Importing the Dependencies
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import pickle
# Data Collection and Analysis
## PIMA Diabetes Dataset

# loading the diabetes dataset to a pandas DataFrame
diabetes_dataset = pd.read_csv('E:\\Datasets\\diabetes.csv') 
# printing the first 5 rows of the dataset
print(diabetes_dataset.head())
# number of rows and Columns in this dataset
print(diabetes_dataset.shape)
print(diabetes_dataset['Outcome'].value_counts())
diabetes_dataset.groupby('Outcome').mean()
# separating the data and labels
X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
Y = diabetes_dataset['Outcome']
scaler = StandardScaler()
X = scaler.fit_transform(X)
Y = diabetes_dataset['Outcome']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)
classifier = svm.SVC(kernel='linear')
#training the support vector Machine Classifier
classifier.fit(X_train, Y_train)
# accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data : ', training_data_accuracy)
# accuracy score on the test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data : ', test_data_accuracy)
input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')


from flask import Flask,request,jsonify,render_template
pickle.dump(classifier,open('model.pkl','wb+'))
with open('model.pkl','rb') as file:
  model = pickle.load(file)

new_Prediction = model.predict(std_data)
print("New Prediction with Pickle file: ",new_Prediction)
import os


app = Flask(__name__)

port=int(os.environ.get("PORT",5000))


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict',methods=["POST"])
def predict():
  features = [float(x) for x in request.form.values()]
  final_features = [np.array(features)]
  flask_prediction = model.predict(final_features)
  if(flask_prediction[0] == 1):
    return render_template('index.html',prediction_text="The Person is a Diabetic")
  else:
    return render_template('index.html',prediction_text="The Person is not a Diabetic")



if (__name__) == "__main__":
  app.run(debug=True,host='0.0.0.0',port=port)