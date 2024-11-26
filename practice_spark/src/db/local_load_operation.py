# 导入必要的模块
import logging
import pandas as pd


def pandas_read_local_data_of_csv(file_path, sep=',', header=0):
    return pd.read_csv(file_path, sep=sep, header=header)
