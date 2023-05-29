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
data['bhk'] = data['size'].str.split().str.get(0).astype(int)
def convertRange(x):
    temp = x.split('-')
    if(len(temp) == 2):
        return (float(temp[0]) + float(temp[1]))/2
    try:
        return float(x)
    except:
        return None
data['total_sqft'] = data['total_sqft'].apply(convertRange)
data['price_per_sqft'] = data['price']*100000 / data['total_sqft'] 
data['location'] = data['location'].apply(lambda x: x.strip())
location_count = data['location'].value_counts()
location_count_less_10 = location_count[location_count<11]
data['location'] = data['location'].apply(lambda x: 'other' if x in location_count_less_10 else x)
data = data[((data['total_sqft']/data['bhk'])>=300)]

def remove_outliers_sqft(df):
    df_output = pd.DataFrame()
    for key,subdf in df.groupby('location'):
        m = np.mean(subdf.price_per_sqft)
        st = np.std(subdf.price_per_sqft)

        gem_df = subdf[(subdf.price_per_sqft > (m-st)) & (subdf.price_per_sqft <= (m+st))]
        df_output = pd.concat([df_output,gem_df],ignore_index=True)

    return df_output
data = remove_outliers_sqft(data)

def bhk_outlier_remover(df):
    exclude_indicies = np.array([])
    for location,location_df in df.groupby('location'):
        bhk_stats = {}
        for bhk,bhk_df in location_df.groupby('bhk'):
            bhk_stats[bhk] = {
                'mean':np.mean(bhk_df.price_per_sqft),
                'std':np.std(bhk_df.price_per_sqft),
                'count':bhk_df.shape[0]
            }
        for bhk,bhk_df in location.groupby('bhk'):
            stats = bhk_stats .get(bhk-1)
            if stats and stats['count']>5:
                exclude_indicies = np.append(exclude_indicies,bhk[bhk_df.price_per_sqft(stats['mean'])].index.values)
        return df.drop(exclude_indices,axis='index')

data.drop(columns=['size','price_per_sqft'],inplace=True)
print(data.head())
data.to_csv("Cleaned_data.csv")