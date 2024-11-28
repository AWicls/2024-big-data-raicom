# 效果评估模块
import pandas as pd
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score

from practice_sklearn.src import data_preprocessing, segmentation_model

# {'reg': RandomForestClassifier(), 'reg__max_depth': 15, 'reg__min_samples_leaf': 3, 'reg__min_samples_split': 3,
# 'reg__n_estimators': 20}
# 0.8317269076305221
# Pipeline(steps=[('scaler', StandardScaler()), ('reg',
# RandomForestClassifier(max_depth=15, min_samples_leaf=3, min_samples_split=3, n_estimators=20))])
# 准确率: 0.81
# 召回率: 0.57
# F1值: 0.56
# K折交叉验证平均准确率: 0.80

if __name__ == '__main__':
    filename = r"../data/Spotify_data.csv"
    xtrain, xtest, ytrain, y_test = data_preprocessing.process(filename)
    model = segmentation_model.load_model(r"../data/segmentation_model.pkl")
    y_pred = model.predict(xtest)


    # 评估指标
    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred, average='macro')
    f1 = f1_score(y_test, y_pred, average='macro')

    print(model.best_params_, "\n", model.best_score_, "\n", model.best_estimator_)
    print(f"准确率: {accuracy:.2f}")
    print(f"召回率: {recall:.2f}")
    print(f"F1值: {f1:.2f}")

    # K折交叉验证
    cv_scores = cross_val_score(model, xtrain, ytrain, cv=5)
    print(f"K折交叉验证平均准确率: {cv_scores.mean():.2f}")