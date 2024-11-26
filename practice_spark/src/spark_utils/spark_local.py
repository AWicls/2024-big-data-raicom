# 导入所需的模块
import os
from pyspark.sql import SparkSession

# 设置环境变量，指定 PySpark 使用的 Python 解释器
os.environ['PYSPARK_PYTHON'] = r'C:\Users\AWII\.conda\envs\spark\python.exe'
# 设置 Hadoop 用户名
os.environ['HADOOP_USER_NAME'] = 'root'

# 创建 SparkSession 对象，用于与 Spark 进行交互
# appName 设置应用程序的名称
# master 设置为 local[*] 表示在本地模式下运行，使用所有可用的核心
spark = SparkSession.builder.appName(__name__).master('local[*]').getOrCreate()

# 定义 CSV 文件的路径
csv_file_path = r'../../data/word.csv'

# 读取 CSV 文件并进行处理
(
    spark.read.format('csv')  # 指定读取格式为 CSV
    .option('header', 'false')  # 设置不将第一行作为列名
    .load(csv_file_path)  # 加载 CSV 文件
    .rdd  # 将 DataFrame 转换为 RDD
    .map(lambda word: (word[0], 1))  # 将每个单词映射为 (word, 1) 的键值对
    .reduceByKey(lambda a, b: a + b)  # 按键（单词）聚合，计算每个单词的出现次数
    .toDF(['word', 'count'])  # 将 RDD 转换为 DataFrame，并指定列名为 'word' 和 'count'
    .show()  # 显示结果
)
