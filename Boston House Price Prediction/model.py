#Importing Dependencies 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import sklearn
#load the dataset
from sklearn.datasets import load_boston
boston = load_boston()
print(boston.keys())
dataset = pd.DataFrame(boston.data,columns = boston.feature_names)
print(dataset.head())
dataset['Price'] = boston.target
# Independent And Dependent Features 
X = dataset.iloc[:,:-1]
Y = dataset.iloc[:,-1]
# Splitting the data into training and testing data
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.3,random_state=0)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
#Load the Machine Learning Model
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(X_train,Y_train)
# Prediction on train data
train_pred = model.predict(X_train)
# Prediction on test data
test_pred = model.predict(X_test)
from sklearn.metrics import mean_squared_error,mean_absolute_error
print('mean_absolute_error: ',mean_absolute_error(Y_test,test_pred))
print('mean_squared_error: ',mean_squared_error(Y_test,test_pred))
print('root_mean_squared_error: ',np.sqrt(mean_squared_error(Y_test,test_pred)))
from sklearn.metrics import r2_score
r2score = r2_score(Y_test,test_pred)
print("R^2 Score: ",r2score)
adjusted_r2_score = 1-(1-r2score)*(len(Y_test)-1)/(len(Y_test)-X_test.shape[1]-1)
print("Adjusted R^2 Score: ",adjusted_r2_score)
input_data = (0,18,2,0,0,6,65,4,1,296,15,396,4.98)

# converting the input data into a numpy array
input_data_as_array = np.asarray(input_data)

# reshaping the input data into 2-D array
input_data_reshaped = input_data_as_array.reshape(1,-1)

# transforming the data by using StandardScaler
scaled_data = scaler.fit_transform(input_data_reshaped)

# predciting the outcome on new scaled input data
prediction = model.predict(scaled_data)
print(prediction)

import pickle
pickle.dump(model,open('house.pkl','wb'))
