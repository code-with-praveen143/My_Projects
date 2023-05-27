#**Importing Dependencies**

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore") 
import pickle
print("All Dependencies are imported")

#Loading the dataset which contain the details of heart disease patients data
data = pd.read_csv("E:\\Datasets\\heart_disease_data.csv")

#it displays the first five rows of data
print(data.head())

#this method gives the information about our data
print(data.describe())

#check whether the dataset contain any null values
print(data.isna().sum())

#the shape of the data
print(data.shape)

#splitting the data into input data and output data
X = data.iloc[:,:-1]
Y = data.iloc[:,-1]

#Now spliting the data into training data and test data
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=0)

# print("X_Trainig Data:",X_train)
# # print("X_Testing Data:",X_test)
# # print("Y_Testing Data:",Y_test)
# # print("Y_Training Data:",Y_train)
print("X_train: ",X.shape)
#Loading Our Machine Learning Model
model = LogisticRegression()

model.fit(X_train,Y_train)

#Model evaluation
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)
X_test_prediction = model.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_prediction,Y_test)
print("Training Data Accuracy: ",round(training_data_accuracy*100))
print("Testing Data Accuracy: ",round(testing_data_accuracy*100))

"""Building a Prediction System
bold text
"""

input_data = (41,0,1,130,204,0,0,172,0,1.4,2,0,2)
#changes the input data into numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting for only as instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
if(prediction[0] == 1):
  print("The Person has a Heart Disease")
else:
  print("The Person Doesn't has a heart disease")

pickle.dump(model,open('heart.pkl','wb'))