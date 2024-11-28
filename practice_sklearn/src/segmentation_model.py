# 客户细分模型模块
import pickle

import pandas as pd

from data_preprocessing import process
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.preprocessing import StandardScaler


# xtrain, xtest, ytrain, ytest = process()
def train_model(xtrain, ytrain):
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("reg", GradientBoostingClassifier())
    ])
    parameters = [
        {
            "reg": [SVC()],
            "reg__kernel": ["linear", "poly", "sigmoid"],
            "reg__degree": [1, 2, 3],
            "reg__gamma": [0.01, 0.05, 0.15, 0.2],
            "reg__C": [0.1, 0.3, 1, 100, 1000]
        },
        {
            "reg": [RandomForestClassifier()],
            "reg__n_estimators": [20, 30, 50, 100],
            "reg__max_depth": [1, 3, 10, 15, 17],
            "reg__min_samples_leaf": [2, 3, 5, 7, 10],
            "reg__min_samples_split": [2, 3, 5, 10]
        },
        {
            "reg": [GradientBoostingClassifier()],
            "reg__learning_rate": [0.01, 0.05, 0.06, 0.07, 0.08],
            "reg__criterion": ["friedman_mse", "squared_error"],
            "reg__loss": ["log_loss", "exponential"],
            "reg__n_estimators": [50, 60, 80, 90, 100],
            "reg__subsample": [0.05, 0.2, 0.35, 0.4, 0.5]
        }
    ]

    # model = RandomizedSearchCV(estimator=pipeline, param_distributions=parameters, n_iter=20, n_jobs=-1, verbose=1,
    #                            refit=True)

    model = GridSearchCV(estimator=pipeline, param_grid=parameters, n_jobs=-1, verbose=1,
                         refit=True)

    model.fit(xtrain, ytrain)

    print(model.best_params_, "\n", model.best_score_, "\n", model.best_estimator_)
    # res = model.score(xtest, ytest)
    # print(res)
    return model


def sava_model(model_, filename):
    # with open("../data/segmentation_model.pkl", 'wb') as f:
    with open(filename, 'wb') as f:
        pickle.dump(model_, f)


def load_model(filename):
    with open(filename, 'rb') as f:
        load_ = pickle.load(f)
    return load_

if __name__ == '__main__':
    xtrain, xtest, ytrain, ytest = process(r"../data/Spotify_data.csv")

    model = train_model(xtrain, ytrain)

    sava_model(model, r"../data/segmentation_model.pkl")