import happybase
import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def connect_to_hbase(host='master', port=2181):
    """
    连接到 HBase。

    Args:
        host (str, optional): HBase 主机地址，默认是 'master'
        port (int, optional): ZooKeeper 客户端连接端口，默认是 2181

    Returns:
        happybase.Connection: HBase 连接对象
    """
    try:
        connection = happybase.Connection(host=host, port=port)
        connection.open()
        logging.info("Connected to HBase")
        return connection
    except Exception as e:
        logging.error(f"Failed to connect to HBase: {e}")
        return None


def create_table(connection, table_name, column_families):
    """
    创建 HBase 表。

    Args:
        connection (happybase.Connection): HBase 连接对象
        table_name (str): 表名
        column_families (list): 列族列表
    """
    try:
        if table_name.encode('utf-8') in connection.tables():
            logging.warning(f"Table '{table_name}' already exists")
            return
        connection.create_table(table_name, {cf: {} for cf in column_families})
        logging.info(f"Table '{table_name}' created successfully")
    except Exception as e:
        logging.error(f"Failed to create table '{table_name}': {e}")


def insert_data(connection, table_name, row_key, data):
    """
    插入数据到 HBase 表。

    Args:
        connection (happybase.Connection): HBase 连接对象
        table_name (str): 表名
        row_key (str): 行键
        data (dict): 要插入的数据，键为列族:列名，值为列值
    """
    try:
        table = connection.table(table_name)
        table.put(row_key, data)
        logging.info(f"Data inserted into table '{table_name}' successfully")
    except Exception as e:
        logging.error(f"Failed to insert data into table '{table_name}': {e}")


def get_data(connection, table_name, row_key):
    """
    从 HBase 表中获取数据。

    Args:
        connection (happybase.Connection): HBase 连接对象
        table_name (str): 表名
        row_key (str): 行键

    Returns:
        dict: 查询结果
    """
    try:
        table = connection.table(table_name)
        row = table.row(row_key)
        logging.info(f"Data retrieved from table '{table_name}' successfully")
        return row
    except Exception as e:
        logging.error(f"Failed to retrieve data from table '{table_name}': {e}")
        return {}


def delete_table(connection, table_name):
    """
    删除 HBase 表。

    Args:
        connection (happybase.Connection): HBase 连接对象
        table_name (str): 表名
    """
    try:
        if table_name.encode('utf-8') not in connection.tables():
            logging.warning(f"Table '{table_name}' does not exist")
            return
        connection.delete_table(table_name, disable=True)
        logging.info(f"Table '{table_name}' deleted successfully")
    except Exception as e:
        logging.error(f"Failed to delete table '{table_name}': {e}")


def close_connection(connection):
    """
    关闭 HBase 连接。

    Args:
        connection (happybase.Connection): HBase 连接对象
    """
    if connection:
        connection.close()
        logging.info("Connection closed")


if __name__ == '__main__':
    # HBase 连接参数
    host = 'master'  # 根据你的配置文件，ZooKeeper 集群的主机列表中的第一个主机
    port = 2181  # ZooKeeper 客户端连接端口

    # 连接到 HBase
    connection = connect_to_hbase(host, port)

    if connection:
        # 创建表
        table_name = 'test_table'
        column_families = ['cf1', 'cf2']
        create_table(connection, table_name, column_families)

        # 插入数据
        row_key = 'row1'
        data = {
            'cf1:col1': 'value1',
            'cf1:col2': 'value2',
            'cf2:col1': 'value3'
        }
        insert_data(connection, table_name, row_key, data)

        # 获取数据
        row = get_data(connection, table_name, row_key)
        print(row)

        # 删除表
        delete_table(connection, table_name)

        # 关闭连接
        close_connection(connection)
