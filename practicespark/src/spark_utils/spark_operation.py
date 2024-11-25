from pyspark.sql import SparkSession
import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def spark_create_session(app_name='PySpark', master='local[*]'):
    try:
        spark = (SparkSession.builder
                 .appName(app_name)
                 .master(master)
                 .getOrCreate())
        logging.info(f"SparkSession created with application name: {app_name}")
        return spark
    except Exception as e:
        logging.error(f"Failed to create SparkSession: {e}")
        return None
