from pyspark.sql import SparkSession, HiveContext
import logging
import os

os.environ['HADOOP_USER_NAME'] = 'root'
# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# hive_conf_path = r'./hive-site.xml'

spark = (SparkSession.builder
         .appName(__name__)
         .master('local')
         .config('spark.sql.warehouse.dir', 'hdfs://master:8020/hive')
         .config('hive.metastore.uris', 'thrift://master:9083')
         .enableHiveSupport()
         .getOrCreate())

# spark.sparkContext.setLogLevel(logLevel='INFO')

gen_data_path = r'../../data/generated_data.csv'
df = spark.read.csv(gen_data_path, header=True, inferSchema=True)
df.createOrReplaceTempView('table123')

# spark.sql("use raicom")

df2 = spark.sql("""

select Name
    , nvl(Age, 18) as Age
    , round(nvl(Salary, 3000.0)) Salary
    , nvl(City, 'New York') City
    , nvl(Email, 'None') Email
    , nvl(Date, 'None') Date
from table123
order by Date

""").toDF("Name", "Age", "Salary", "City", "Email", "Date")

df2.write.mode(saveMode='overwrite').saveAsTable('raicom.table2')

spark.stop()
