from pyhive import hive
from read_conf import read_yaml


# 连接hive并返回cursor对象
def connect_hive_to_curser():
    """
    从配置文件中读取Hive的配置信息，并建立到Hive的连接，返回cursor对象。

    Returns:
        hive.Cursor: Hive数据库的cursor对象，用于执行SQL查询。
    """
    # 配置文件路径
    filepath = r'../config/config.yaml'
    # 读取配置文件中的Hive配置信息
    conf = read_yaml(filepath).get('hive')

    # 使用Hive配置信息创建Hive连接
    conn = hive.Connection(
        host=conf.get('host'),
        port=conf.get('port'),
        username=conf.get('username'),
        database=conf.get('database'),
        auth=conf.get('auth'),
        configuration=conf.get('configuration'))

    # 返回Hive数据库的cursor对象
    return conn.cursor()


# 连接测试
if __name__ == '__main__':
    # 测试连接Hive并执行SQL查询
    curser = connect_hive_to_curser()
    # 执行SQL语句，显示数据库中的所有表
    sql = 'show tables'
    curser.execute(sql)
    # 获取并打印查询结果的第一个表名
    result = curser.fetchall()
    print(result[0][0])
