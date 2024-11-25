# 导入所需的模块
from pyspark.sql import SparkSession
import os

# 设置Hadoop用户名环境变量
# 这是为了确保Hadoop操作时使用正确的用户名
# 在Hadoop集群中，用户名会影响权限和资源分配
os.environ['HADOOP_USER_NAME'] = 'root'

# 创建SparkSession
# SparkSession是Spark SQL的主要入口点，用于创建DataFrame、执行SQL查询等操作
spark = (SparkSession
         .builder
         .appName(__name__)  # 设置应用程序名称，这里使用当前模块的名称
         .master('local')  # 设置Spark运行模式为本地模式，适用于开发和测试
         .config('spark.sql.warehouse.dir', 'hdfs://master:8020/hive')  # 设置Spark SQL仓库目录，指向HDFS上的Hive仓库
         .config('hive.metastore.uris', 'thrift://master:9083')  # 设置Hive元存储服务的URI，指向Thrift服务地址
         .enableHiveSupport()  # 启用Hive支持，允许Spark与Hive进行交互
         .getOrCreate()  # 获取或创建SparkSession实例
         )

# 设置日志级别为INFO
# 这可以减少日志输出，使日志更简洁，便于调试
spark.sparkContext.setLogLevel(logLevel='INFO')

# 执行SQL查询，显示所有数据库
# 使用SparkSession的sql方法执行SQL查询，并使用show方法显示结果
# 这里查询Hive中的所有数据库，并显示结果
spark.sql("""show databases""").show()
