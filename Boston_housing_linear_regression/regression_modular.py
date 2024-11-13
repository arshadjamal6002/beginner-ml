import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    # Fill missing values with the column mean
    df = df.apply(lambda x: x.fillna(x.mean()), axis=0)
    return df

def split_data(df, target_column, test_size=0.2, random_state=42):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    return lr

def evaluate_model(lr, X_test, y_test):
    y_pred = lr.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2

def main():
    # Load and preprocess the data
    df = load_and_preprocess_data('HousingData.csv')
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(df, target_column='MEDV')
    
    # Train the model
    lr = train_model(X_train, y_train)
    
    # Evaluate the model
    mse, r2 = evaluate_model(lr, X_test, y_test)
    
    # Print the results
    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')

if __name__ == "__main__":
    main()
