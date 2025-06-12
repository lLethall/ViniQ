import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from database import load_data

def update_model():
    df = pd.DataFrame(load_data("quality_wine"))
    df = df.drop('id', axis=1)
    X = df.drop('quality', axis=1)
    y = df['quality']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo_rf = RandomForestRegressor(n_estimators=100, random_state=42)

    modelo_rf.fit(X_train, y_train)
    y_pred_rf = modelo_rf.predict(X_test)

    mse = mean_squared_error(y_test, y_pred_rf)
    print(f"Error cuadrático medio (MSE): {mse}")

    return modelo_rf

def predict_quality(model, valores_entrada):
    df = pd.DataFrame([valores_entrada])
    df = df.drop('quality', axis=1)
    return model.predict(df)[0]
