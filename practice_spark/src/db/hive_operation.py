# 导入必要的模块
from practice_spark.src.utils.read_config import get_yaml_data
import logging
from pyhive import hive

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def hive_connect_cursor():
    """
    获取 Hive 连接的游标对象。

    Returns:
        cursor: Hive 游标对象
    """
    # 从 YAML 配置文件中读取 Hive 配置信息
    hive_conf = get_yaml_data().get('hive')

    # 创建 Hive 连接
    conn = hive.Connection(
        host=hive_conf.get('host'),  # Hive 服务器地址
        port=hive_conf.get('port'),  # Hive 服务器端口
        username=hive_conf.get('username'),  # 用户名
        database=hive_conf.get('database'),  # 数据库名称
        auth=hive_conf.get('auth')  # 认证方式
    )

    # 返回连接的游标对象
    return conn.cursor()


def hive_execute(hive_cursor, sql):
    """
    执行 Hive SQL 语句并返回查询结果。

    Args:
        hive_cursor: Hive 游标对象
        sql: 要执行的 SQL 语句

    Returns:
        result: 查询结果
    """
    try:
        # 执行 SQL 语句
        hive_cursor.execute(sql)
    except Exception as e:
        # 捕获并打印执行 SQL 语句时的异常
        logging.error(f'ERROR hive_execute Function -> hive_cursor.execute(sql): {e}')
        logging.error(f'ERROR hive_execute Function -> hive_cursor.execute(sql): {sql}')

    try:
        # 获取查询结果
        return hive_cursor.fetchall()
    except Exception as e:
        # 捕获并打印获取查询结果时的异常
        logging.warning(f'{sql} 不是查询语句,报错为 {e}')
        # print('ERROR hive_execute Function -> hive_cursor.fetchall():', sql)


def hive_close(close_cursor):
    close_cursor.close()


# if __name__ == '__main__':
#     # 获取 Hive 游标对象
#     cursor = hive_connect_cursor()
#
#     # 定义创建表的 SQL 语句
#     sql_create = 'create table if not exists table2(id int, name string)'
#
#     # 定义查询表的 SQL 语句
#     sql_query = "show tables"
#
#     # 执行创建表的 SQL 语句
#     hive_execute(cursor, sql_create)
#
#     # 执行查询表的 SQL 语句并获取结果
#     data = hive_execute(cursor, sql_query)
#
#     hive_close(cursor)
#
#     # 打印查询结果
#     print(data)
