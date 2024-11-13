import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('HousingData.csv')
df = df.apply(lambda x: x.fillna(x.mean()), axis = 0)

X = df.drop(columns = ['MEDV'])
y = df.MEDV

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

print('mse', mean_squared_error(y_test, y_pred))
print('r2_score', r2_score(y_test, y_pred))