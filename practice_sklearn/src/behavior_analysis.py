import segmentation_model
import data_preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def predict_():
    filename = r"../data/Spotify_data.csv"
    xtrain, xtest, ytrain, ytest = data_preprocessing.process(filename)

    data = pd.read_csv(filename)

    model = segmentation_model.load_model(r"../data/segmentation_model.pkl")

    # 5. 使用模型进行预测
    x_plan = model.predict(xtrain)
    y_plan = model.predict(xtest)

    # 将预测结果合并
    result = np.concatenate((x_plan, y_plan), axis=0)

    # 删除原有的 "spotify_subscription_plan" 列，并添加新的预测结果
    data = data.drop(columns=["spotify_subscription_plan"], errors='ignore')
    data["spotify_subscription_plan"] = result
    return data

# group_ = data.groupby("Age")
# keys = group_.keys
#
# print()
#
# for i in data.columns:
#     data.groupby("Age")[i].value_counts()


