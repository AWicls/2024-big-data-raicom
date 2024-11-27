# 导入sklearn的决策树相关类库
from sklearn.tree import DecisionTreeClassifier
# 导入数据拆分库
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
# 导入pandas
import pandas as pd

# 读取训练数据集
data = pd.read_csv(r"practice_sklearn\data\drug200.csv", )

# 提取特征值和训练数据
data_target = data["Drug"]
data_train = data.drop(columns=["Drug"])

# 对类别型特征进行独热编码
data_features_encoded = pd.get_dummies(data_train, columns=["Sex", "BP", "Cholesterol"], drop_first=True)

# 拆分数据集为训练集（0.8）和测试集（0.2）
X_train, X_test, y_train, y_test = train_test_split(data_features_encoded, data_target, train_size=0.8, random_state=42)

# 训练模型
# model = tree.DecisionTreeClassifier(
#     criterion="entropy"
#     , splitter="best"
#     , max_depth=10
#     , min_samples_split=10
#     , min_samples_leaf=10
# )

scaler = StandardScaler()

x_scaler = scaler.fit_transform(X_train)
y_scaler = scaler.fit_transform(X_test)

parameters = {"criterion": ["gini", "entropy"]
    , "splitter": ["best", "random"]
    , "max_depth": [1, 2, 4, 8, 10, 15, 20, None]
    , "min_samples_leaf": [2, 3, 4, 5, 8, 10]
    , "min_samples_split": [2, 3, 4, 5, 8, 10, 13, ]
              }
model = GridSearchCV(estimator=DecisionTreeClassifier(), param_grid=parameters, n_jobs=-1, cv=5, verbose=1)

model.fit(x_scaler, y_train)

# 测试模型
result = model.score(y_scaler, y_test)

# print准确率
print("最佳参数组合：", model.best_params_)
print("最佳参数组合得分：", model.best_score_)
print(result)
