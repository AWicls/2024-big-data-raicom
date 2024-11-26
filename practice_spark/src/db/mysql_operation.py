# 导入必要的模块
from practice_spark.src.utils.read_config import get_yaml_data
import logging
import pymysql

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def mysql_connect():
    """
    连接到 MySQL 数据库并返回连接对象。

    Returns:
        pymysql.connections.Connection: 数据库连接对象
    """
    mysql_conf = get_yaml_data().get('mysql')
    conn = pymysql.connect(
        host=mysql_conf.get('host'),          # MySQL 主机地址
        port=mysql_conf.get('port'),          # MySQL 端口号
        user=mysql_conf.get('user'),          # MySQL 用户名
        password=mysql_conf.get('password'),  # MySQL 密码
        database=mysql_conf.get('database'),  # 数据库名称
        ssl=mysql_conf.get('ssl'),            # SSL 配置
        charset=mysql_conf.get('charset'),    # 字符集
        use_unicode=mysql_conf.get('use_unicode'),  # 是否使用 Unicode
    )
    logging.info("Connected to MySQL database")
    return conn


def mysql_execute(mysql_connect, sql):
    """
    执行 SQL 语句并返回查询结果。

    Args:
        mysql_connect (pymysql.connections.Connection): 数据库连接对象
        sql (str): 要执行的 SQL 语句

    Returns:
        list: 查询结果
    """
    try:
        mysql_cursor = mysql_connect.cursor()  # 创建游标对象
        mysql_cursor.execute(sql)           # 执行 SQL 语句
        result = mysql_cursor.fetchall()    # 获取所有查询结果
        logging.info(f"SQL executed successfully: {sql}")
        return result
    except Exception as e:
        logging.warning(f'SQL execution failed: {sql}, error: {e}')
        return []


def mysql_close(mysql_conn):
    """
    关闭 MySQL 数据库连接。

    Args:
        mysql_conn (pymysql.connections.Connection): 数据库连接对象
    """
    if mysql_conn:
        mysql_conn.close()
        logging.info("MySQL connection closed")


# if __name__ == '__main__':
#     # SQL 语句
#     sql = 'SHOW DATABASES'
#
#     # 获取数据库连接
#     mysql_conn = mysql_connect()
#
#     # 执行 SQL 语句并获取结果
#     data = mysql_execute(mysql_conn, sql)
#
#     # 打印查询结果
#     print(data)
#
#     # 关闭数据库连接
#     mysql_close(mysql_conn)
