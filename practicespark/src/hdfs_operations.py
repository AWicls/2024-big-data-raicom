# HDFS读写操作模块
# 对 HDFS ⽂件系统中的数据进⾏操作，如上传和读取`word.csv`

from hdfs import InsecureClient

hdfs_url = ''
hdfs_path = ''
local_path = ''

client = InsecureClient(hdfs_url)

# 于将本地⽂件上传到 HDFS
client.upload(hdfs_path=hdfs_path, local_path=local_path)


def read_hdfs(hdfs_path):
    with client.read(hdfs_path) as reader:
        return reader.read()
