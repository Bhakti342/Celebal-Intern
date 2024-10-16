import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Loading the data in pandas
df = pd.read_csv("Data/train.csv")

# dropping 3 columns
cols = ['Name', 'Ticket', 'Cabin']
df = df.drop(cols, axis = 1)

# #dropping rows having missing values
# df = df.dropna()

dummies = []
cols = ['Pclass', 'Sex', 'Embarked']
for col in cols:
    dummies.append(pd.get_dummies(df[col]))
titanic_dummies = pd.concat(dummies, axis=1)
df = pd.concat((df,titanic_dummies), axis=1)
df = df.drop(['Pclass', 'Sex', 'Embarked'], axis = 1)

# Taking care of missing Data
df['Age'] = df['Age'].interpolate()
# df.info()

# Converting the Dataframe to numpy
X = df.values
y = df['Survived'].values
X = np.delete(X, 1, axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
