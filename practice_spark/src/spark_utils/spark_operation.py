from pyspark.sql import SparkSession
from practice_spark.src.utils.read_config import get_yaml_data
import logging

# 配置日志记录
# 设置日志级别为 INFO，并指定日志格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 定义一个函数，创建一个简单的 SparkSession
def spark_SparkSession_simple(app_name=__name__, master='local[*]'):
    try:
        # 创建 SparkSession
        # appName: 应用程序的名称
        # master: 指定运行模式，local[*] 表示在本地模式下运行，使用所有可用的核心
        spark = (SparkSession.builder
                 .appName(app_name)
                 .master(master)
                 .getOrCreate())

        # 记录日志，表示 SparkSession 创建成功
        logging.info(f"SparkSession created with application name: {app_name}")

        # 返回创建的 SparkSession 对象
        return spark
    except Exception as e:
        # 记录错误日志，表示创建 SparkSession 失败
        logging.error(f"Failed to create SparkSession: {e}")

        # 返回 None 表示创建失败
        return None

# 定义一个函数，创建一个支持 Hive 的 SparkSession
def spark_SparkSession_hive(app_name=__name__, master='local[*]',
                            spark_sql_warehouse_dir=None,
                            hive_metastore_uris=None):
    # 从配置文件中读取 Spark 和 Hive 相关的配置
    spark_conf = get_yaml_data().get('spark').get('hive')

    # 如果没有提供 spark_sql_warehouse_dir，则从配置文件中获取
    if spark_sql_warehouse_dir is None:
        spark_sql_warehouse_dir = spark_conf.get('spark_sql_warehouse_dir')

    # 如果没有提供 hive_metastore_uris，则从配置文件中获取
    if hive_metastore_uris is None:
        hive_metastore_uris = spark_conf.get('hive_metastore_uris')

    try:
        # 创建支持 Hive 的 SparkSession
        # appName: 应用程序的名称
        # master: 指定运行模式，local[*] 表示在本地模式下运行，使用所有可用的核心
        # config: 设置 Spark 配置项
        # enableHiveSupport: 启用对 Hive 的支持
        spark = (
            SparkSession.builder
            .appName(app_name)
            .master(master)
            .config('spark.sql.warehouse.dir', spark_sql_warehouse_dir)
            .config('hive.metastore.uris', hive_metastore_uris)
            .enableHiveSupport()
            .getOrCreate()
        )

        # 记录日志，表示 SparkSession 创建成功
        logging.info(f"SparkSession created with application name: {app_name}")

        # 返回创建的 SparkSession 对象
        return spark
    except Exception as e:
        # 记录错误日志，表示创建 SparkSession 失败
        logging.error(f"Failed to create SparkSession: {e}")

        # 返回 None 表示创建失败
        return None
