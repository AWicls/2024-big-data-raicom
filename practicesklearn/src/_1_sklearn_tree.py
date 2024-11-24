# 导入sklearn的决策树相关类库
from sklearn import tree
# 导入数据拆分库
from sklearn.model_selection import train_test_split
# 导入pandas
import pandas as pd

# 读取训练数据集
data = pd.read_csv(r"D:\raicom\2024-big-data-raicom\practicesklearn\data\drug200.csv", )

# 提取特征值和训练数据
data_target = data["Drug"]
data_train = data.drop(columns=["Drug"])

# 对类别型特征进行独热编码
data_features_encoded = pd.get_dummies(data_train, columns=["Sex", "BP", "Cholesterol"], drop_first=True)

# 拆分数据集为训练集（0.8）和测试集（0.2）
X_train, X_test, y_train, y_test = train_test_split(data_features_encoded, data_target, train_size=0.8, random_state=42)

# 训练模型
model = tree.DecisionTreeClassifier()
model.fit(X_train, y_train)

# 测试模型
result = model.score(X_test, y_test)

# print准确率
print(result)
