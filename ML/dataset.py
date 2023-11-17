import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import OrdinalEncoder


# Read Data
df=pd.read_csv("data/dataset.csv",header=0,low_memory=True)
df.drop(['Unnamed: 0','track_id'],axis=1, inplace=True)
df.dropna(inplace=True)

# Extract feature and target arrays
X, y = df.drop('track_genre', axis=1), df[['track_genre']]

# Extract text features
cats = X.select_dtypes(exclude=np.number).columns.tolist()


y_encoded = OrdinalEncoder().fit_transform(y)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, random_state=1, stratify=y_encoded)

