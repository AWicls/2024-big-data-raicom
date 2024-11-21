import pymysql
from read_conf import read_yaml


def connect_mysql_to_curser():
    """
    连接到MySQL数据库并返回游标对象。

    从配置文件中读取MySQL数据库的配置信息，并使用这些信息建立到数据库的连接。
    最后返回一个游标对象，用于执行SQL语句和与数据库进行交互。

    Returns:
        cursor: 数据库游标对象。
    """
    # 配置文件路径
    filepath = r'../../practicespark/config/config.yaml'
    # 从配置文件中读取MySQL配置信息
    conf = read_yaml(filepath).get('mysql')

    # 使用读取的配置信息连接到MySQL数据库
    connection = pymysql.connect(
        host=conf.get('host'),
        port=conf.get('port'),
        user=conf.get('user'),
        password=conf.get('password'),
        charset=conf.get('charset'),
    )

    # 返回游标对象
    return connection.cursor()


if __name__ == '__main__':
    # 获取数据库游标
    curser = connect_mysql_to_curser()
    # 执行SQL语句：切换到mysql数据库
    sql = 'use mysql'
    curser.execute(sql)
    # 执行SQL语句：显示所有表
    sql2 = 'show tables'
    curser.execute(sql2)
    # 获取查询结果
    data = curser.fetchall()
    # 打印查询结果
    print(data)
