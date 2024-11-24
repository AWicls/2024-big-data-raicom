# 导入必要的模块
from practicespark.src.tools.read_config import get_yaml_data
import happybase
import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def hbase_connect():
    """
    连接到 HBase。

    Returns:
        happybase.Connection: HBase 连接对象
    """
    try:
        hbase_conf = get_yaml_data().get('hbase')
        hbase_connection = happybase.Connection(
            hbase_conf.get('host'),
            hbase_conf.get('port')
        )
        hbase_connection.open()
        logging.info("Connected to HBase")
        return hbase_connection
    except Exception as e:
        logging.error(f"Failed to connect to HBase: {e}")
        return None


def hbase_close(hbase_connection):
    """
    关闭 HBase 连接。

    Args:
        hbase_connection (happybase.Connection): HBase 连接对象
    """
    if hbase_connection:
        hbase_connection.close()


def hbase_get_data(hbase_connection, table_name, row_key):
    """
    获取 HBase 表中指定行的数据。

    Args:
        hbase_connection (happybase.Connection): HBase 连接对象
        table_name (str): 表名
        row_key (str): 行键

    Returns:
        dict: 指定行的数据，键为列族:列名，值为列值
    """
    try:
        table = hbase_connection.table(table_name)
        row = table.row(row_key)
        return row
    except Exception as e:
        logging.error(f"Failed to retrieve data from table '{table_name}': {e}")
        return None


def hbase_scan_data(hbase_connection, table_name):
    """
    获取 HBase 表中的全部数据。

    Args:
        hbase_connection (happybase.Connection): HBase 连接对象
        table_name (str): 表名

    Returns:
        list: 包含所有行数据的列表，每个元素是一个元组 (行键, 数据字典)
    """
    try:
        table = hbase_connection.table(table_name)
        rows = []
        for key, data in table.scan():
            rows.append((key, data))
        return rows
    except Exception as e:
        logging.error(f"Failed to retrieve all data from table '{table_name}': {e}")
        return []


def hbase_insert_data(hbase_connection, table_name, row_key, row_data):
    """
    插入数据到 HBase 表。

    Args:
        hbase_connection (happybase.Connection): HBase 连接对象
        table_name (str): 表名
        row_key (str): 行键
        row_data (dict): 要插入的数据，键为列族:列名，值为列值
    """
    try:
        table = hbase_connection.table(table_name)
        table.put(row_key, row_data)
        logging.info(f'Data inserted into table {table_name} successfully')
    except Exception as e:
        logging.error(f"Failed to insert data into table '{table_name}': {e}")


def hbase_delete_data(hbase_connection, table_name, row_key):
    """
    删除 HBase 表中指定行的数据。

    Args:
        hbase_connection (happybase.Connection): HBase 连接对象
        table_name (str): 表名
        row_key (str): 行键
    """
    try:
        table = hbase_connection.table(table_name)
        table.delete(row_key)
        logging.info(f"Data with row key '{row_key}' deleted from table '{table_name}' successfully")
    except Exception as e:
        logging.error(f"Failed to delete data with row key '{row_key}' from table '{table_name}': {e}")


def hbase_create_table(hbase_connection, table_name, column_families):
    """
    创建 HBase 表。

    Args:
        hbase_connection (happybase.Connection): HBase 连接对象
        table_name (str): 表名
        column_families (list): 列族列表
    """
    try:
        if table_name.encode('utf-8') in hbase_connection.tables():
            logging.warning(f"Table '{table_name}' already exists")
            return
        hbase_connection.create_table(table_name, {cf: {} for cf in column_families})
        logging.info(f"Table '{table_name}' created successfully")
    except Exception as e:
        logging.error(f"Failed to create table '{table_name}': {e}")


def delete_table(hbase_connection, table_name):
    """
    删除 HBase 表。

    Args:
        hbase_connection (happybase.Connection): HBase 连接对象
        table_name (str): 表名
    """
    try:
        if table_name.encode('utf-8') not in hbase_connection.tables():
            logging.warning(f"Table '{table_name}' does not exist")
            return
        hbase_connection.delete_table(table_name, disable=True)
        logging.info(f"Table '{table_name}' deleted successfully")
    except Exception as e:
        logging.error(f"Failed to delete table '{table_name}': {e}")


if __name__ == '__main__':
    # 连接到 HBase
    connection = hbase_connect()

    if connection:
        # 示例操作：获取数据、插入数据、删除数据等
        # 请根据实际需求调用相应的函数

        # 关闭连接
        hbase_close(connection)
