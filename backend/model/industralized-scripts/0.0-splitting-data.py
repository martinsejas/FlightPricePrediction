'''

IMPORTANT: Please download the 'Clean_Dataset.csv' file and place it in the same folder as this script.
The file can be found at https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction.

This script should be run only once to split the raw data into data for training and data for future ingestion.
Feel free to change the paths of each destination folder on lines 41 and 42.

This script was authored by Martin Sejas.

'''


import pandas as pd
from sklearn.model_selection import train_test_split


#import here raw data set, names as 'Clean_dataset.csv' from the Kaggle Repository
df = pd.read_csv("./data/Clean_Dataset.csv")

#saving the column names
column_names = df.columns

#create a copy
master_copy = (df.copy())


# Separate into X and Y for the split and stratify, but we will add them back later
Y = master_copy.pop('price')
X = master_copy

#dropping index column
X = X.drop(columns=X.columns[0])

#We are getting 20% of our entire set 300k rows so 60k rows, to serve as prediction jobs in the future
Xraw, Xprediction, yraw, yprediction = train_test_split(X, Y, random_state=42, stratify=X['class'], test_size=0.2)


#Rejoining data sets after split
Xraw['price'] = yraw
Xprediction['price'] = yprediction

#Converting into separate csv files
Xraw.to_csv("./model/raw_data/flight-price-training.csv")
Xprediction.to_csv("./airflow-data/Airflow_data.csv")
