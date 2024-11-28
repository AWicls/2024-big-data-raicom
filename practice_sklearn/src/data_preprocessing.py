# 数据预处理模块
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# print("前五行：", source.iloc[:5])
# print(source.isna().sum())
# print(source.columns)
# print(source.shape)

# for i in source.columns:
#     print(source[i].value_counts())


# nona_source = source.drop(columns=["preffered_premium_plan", "fav_pod_genre", "preffered_pod_format", "pod_host_preference","preffered_pod_duration"])
#
# print(nona_source.isna().sum())
def process(filename):
    source = pd.read_csv(filename)
    features = source.drop(columns=["spotify_subscription_plan"], axis=1)
    target = source["spotify_subscription_plan"]
    decode_features = pd.get_dummies(features)
    return train_test_split(decode_features.fillna(0), target, random_state=45, train_size=0.8)
