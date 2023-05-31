import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings 
warnings.filterwarnings('ignore')
df = pd.read_csv('E:\\Datasets\\Admission_Predict_Ver1.1.csv')
print(df.head())
# **The above Data Looks likes this**
# 1.GRE Scores ( out of 340 )
# 2.TOEFL Scores ( out of 120 )
# 3.University Rating ( out of 5 )
# 4.Statement of Purpose and Letter of Recommendation Strength ( out of 5 )
# 5.Undergraduate GPA ( out of 10 )
# 6.Research Experience ( either 0 or 1 )
# 7.Chance of Admit ( ranging from 0 to 1 )
# Check whether the data contian any missing values
print(df.isna().sum())
# Check for duplicates if there try to remove
print(df.duplicated().count())
# Remove Serial No. column
print(df.drop(columns='Serial No.',inplace=True))
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print(X_train[0])
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X_train,Y_train)
y_pred = regressor.predict(X_test)
input_data = [337.  , 118.  ,   4.  ,   4.5 ,   4.5 ,   9.65,   1.  ]
input_data_as_array = np.asarray(input_data)
input_data_reshaped = input_data_as_array.reshape(1, -1)
scaled_data = scaler.transform(input_data_reshaped)
prediction = regressor.predict(scaled_data)
output = str(int(prediction[0]*100))+"%"
print("Your are getting Chance of :",output)


import pickle
pickle.dump(regressor,open('model.pkl','wb+'))