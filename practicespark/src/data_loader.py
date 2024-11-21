# 数据加载模块
# 加载 `word.csv` 中的单词数据并准备数据输⼊。

import pandas as pd


def load_data(file_path):
    data = pd.read_csv(file_path)
    words = data.iloc[:, 0].tolist()
    return words


if __name__ == '__main__':
    file_path = r'../data/word.csv'
    data = load_data(file_path)
    print(data)
