# 词频统计主模块
# 实现词频统计核⼼逻辑，将单词进⾏计数并保存结果。

from collections import Counter
import pandas as pd
from practice_spark.src.db.hdfs_operation import hdfs_connect_InsecureClient, hdfs_read_from_hdfs, \
    hdfs_local_upload_to_hdfs
from practice_spark.src.db.local_load_operation import pandas_read_local_data_of_csv
from pyspark.sql import SparkSession
import os

os.environ['PYSPARK_PYTHON'] = r'C:\Users\AWII\.conda\envs\spark\python.exe'


def count_words(words):
    word_count = Counter(words)
    return word_count


def save_results(word_count, output_file):
    df = pd.DataFrame(word_count.item(), columns=["word", "count"])
    df.to_csv(output_file, index=False)
