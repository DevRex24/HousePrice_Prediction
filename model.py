import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import os


BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "Housing_Price.csv")
MODEL_PATH = os.path.join(BASE_DIR, "house_price_model.pkl")

def train():
    df = pd.read_csv(DATA_PATH)

    df['Price_per_sqft'] = df['Price'] / df['Size']
    avg_price_per_sqft = df['Price_per_sqft'].mean()
    
    print(f"Average price per sq ft: ${avg_price_per_sqft:.2f}")

    
    X = df[["Size"]]
    y = df["Price"]
    print("X head:")
    print(X.head())
    print("y head:")
    print(y.head())


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression().fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Model Performance on test set:")
    print(f"Mean Absolute Error: ${mae:,.2f}")
    print(f"R² Score: {r2:.4f}")

    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    print("Model trained & saved to", MODEL_PATH)

if __name__ == "__main__":
    train()