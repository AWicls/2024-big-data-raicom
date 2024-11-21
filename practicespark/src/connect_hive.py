from pyhive import hive
from read_conf import read_yaml


# 连接hive并返回curser对象
def connect_hive_to_curser():
    filepath = r'../config/config.yaml'
    hiveconf = read_yaml(filepath).get('hive')
    conn = hive.Connection(
        host=hiveconf.get('host'),
        port=hiveconf.get('port'),
        username=hiveconf.get('username'),
        database=hiveconf.get('database'),
        auth=hiveconf.get('auth'),
        configuration=hiveconf.get('configuration'))
    return conn.cursor()


# 连接测试
if __name__ == '__main__':
    curser = connect_hive_to_curser()
    sql = 'show tables'
    curser.execute(sql)
    result = curser.fetchall()
    print(result)
