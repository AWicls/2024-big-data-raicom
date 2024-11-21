# Hive查询与数据整合模块
# 利⽤ Hive 对数据进⾏ SQL 查询操作，进⼀步进⾏数据分析。

from pyhive import hive


# 连接Hive
def connect_hive(Host='localhost', Port=10000, DataBase='default',
                 UserName='root', PassWord=None, Auth='NOSASL',
                 Configuration=None):
    connect = hive.Connection(host=Host, port=Port, database=DataBase,
                              username=UserName, password=PassWord, auth=Auth,
                              configuration=Configuration)
    return connect


# Hive执行语句
def exec_hive(ConnetHive, ExecSQL):
    cursor = ConnetHive.cursor()
    cursor.execute(ExecSQL)
    return cursor.fetchall()


if __name__ == '__main__':
    host = 'master'
    port = 10000
    database = 'tdatabase'
    username = 'root'
    password = None
    auth = 'NOSASL'
    hive_config = {  # 配置Hive参数

    }

    table_name = 'test1'
    sql = fr'select * from {database}.{table_name} where id = 1'

    conn = connect_hive(host, port, database,
                        username, password, auth
                        , hive_config)
    data = exec_hive(conn, sql)
    print(data)  # [(1, 'AWi')]
