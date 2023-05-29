# Importing Dependencies
 
import numpy as np 
import pandas as pd 
import warnings 
warnings.filterwarnings('ignore')
import sklearn

data = pd.read_csv("E:\\Datasets\\Bengaluru_House_Data.csv")
print(data.head())
print(data.isna().sum())
data.drop(columns=['area_type','availability','society','balcony'],inplace=True)
print(data.describe())
data['location'] = data['location'].fillna('Sarjapur Road')
data['size'] = data['size'].fillna('2 BHK')
data['bath'] = data['bath'].fillna(data['bath'].median())
print(data.info())
data['bhk'] = data['size'].str.split().str.get(0).astype(int)
