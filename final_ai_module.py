# -*- coding: utf-8 -*-
"""final_ai_module

"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor, VotingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def load_data(filepath):
    df = pd.read_csv(filepath)
    df = df.dropna()
    return df

def feature_engineering(df):
    # Select relevant features and target
    X = df[['hour', 'dc_power', 'daily_yield', 'total_yield']]
    y = df['ac_power']
    return X, y

def train_models(x_train, y_train):
    # Linear Regression
    lr = LinearRegression()
    lr.fit(x_train, y_train)

    # Random Forest
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(x_train, y_train)

    # Gradient Boosting
    gbr = GradientBoostingRegressor(n_estimators=100, random_state=42)
    gbr.fit(x_train, y_train)

    # AdaBoost
    adr = AdaBoostRegressor(n_estimators=100, random_state=42)
    adr.fit(x_train, y_train)

    # Second LR for ensemble
    lr2 = LinearRegression()
    lr2.fit(x_train, y_train)

    # Ensemble Regressor
    ensemble = VotingRegressor([
        ("GBR", gbr),
        ("RFR", rf),
        ("ADR", adr),
        ("LR", lr2)
    ])
    ensemble.fit(x_train, y_train)

    return {
        'linear_regression': lr,
        'random_forest': rf,
        'gradient_boosting': gbr,
        'adaboost': adr,
        'ensemble': ensemble
    }

def evaluate_model(model, x_test, y_test):
    preds = model.predict(x_test)
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    return mse, r2, preds

def save_model(model, filename):
    joblib.dump(model, filename)

def load_model(filename):
    return joblib.load(filename)

