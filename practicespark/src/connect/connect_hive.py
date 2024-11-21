from pyhive import hive
from read_conf import read_yaml
from logview import log_config


# 连接hive并返回curser对象
def connect_hive_to_curser():
    filepath = r'../../config/config.yaml'
    conf = read_yaml(filepath).get('hive')

    conn = hive.Connection(
        host=conf.get('host'),
        port=conf.get('port'),
        username=conf.get('username'),
        database=conf.get('database'),
        auth=conf.get('auth'),
        configuration=conf.get('configuration'))

    return conn.cursor()


# 连接测试
if __name__ == '__main__':
    curser = connect_hive_to_curser()
    sql = 'show tables'
    curser.execute(sql)
    result = curser.fetchall()
    print(result[0][0])
