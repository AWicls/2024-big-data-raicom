from logview import log_config
import pymysql

from read_conf import read_yaml


def connect_mysql_to_curser():
    filepath = r'../../config/config.yaml'
    conf = read_yaml(filepath).get('mysql')

    connection = pymysql.connect(
        host=conf.get('host'),
        port=conf.get('port'),
        user=conf.get('user'),
        password=conf.get('password'),
        charset=conf.get('charset'),
    )

    return connection.cursor()


if __name__ == '__main__':
    curser = connect_mysql_to_curser()
    sql = 'use mysql'
    sql2 = 'show tables'
    curser.execute(sql)
    curser.execute(sql2)
    data = curser.fetchall()
    print(data)
