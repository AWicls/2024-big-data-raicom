# 导入必要的模块
from practice_spark.src.utils.read_config import get_yaml_data
import logging
from hdfs import InsecureClient

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def hdfs_connect_InsecureClient():
    """
    连接到 HDFS 并返回 InsecureClient 对象。

    Returns:
        InsecureClient: 连接到 HDFS 的客户端对象
    """
    hdfs_conf = get_yaml_data().get('hdfs')
    __client = InsecureClient(hdfs_conf.get('url'), hdfs_conf.get('user'))
    return __client


def hdfs_local_upload_to_hdfs(hdfs_client, hdfs_path, local_path):
    """
    将本地文件上传到 HDFS。

    Args:
        hdfs_client (InsecureClient): 连接到 HDFS 的客户端对象
        hdfs_path (str): HDFS 上的目标路径
        local_path (str): 本地文件路径
    """
    try:
        hdfs_client.upload(hdfs_path, local_path)
        print(f"File uploaded to HDFS: {hdfs_path}")
    except Exception as e:
        print(e)


def hdfs_download_from_hdfs(hdfs_client, hdfs_path, local_path):
    """
    从 HDFS 下载文件到本地。

    Args:
        hdfs_client (InsecureClient): 连接到 HDFS 的客户端对象
        hdfs_path (str): HDFS 上的源路径
        local_path (str): 本地目标路径
    """
    hdfs_client.download(hdfs_path, local_path)
    print(f"File downloaded from HDFS: {local_path}")


def hdfs_read_from_hdfs(hdfs_client, hdfs_path):
    """
    从 HDFS 读取文件内容。

    Args:
        hdfs_client (InsecureClient): 连接到 HDFS 的客户端对象
        hdfs_path (str): HDFS 上的文件路径

    Returns:
        str: 读取的文件内容
    """
    try:
        with hdfs_client.read(hdfs_path) as reader:
            read_data = reader.read().decode('utf-8')
        return read_data
    except Exception as e:
        print(e)


def hdfs_delete_file_from_hdfs(hdfs_client, hdfs_path):
    """
    删除 HDFS 上的文件。

    Args:
        hdfs_client (InsecureClient): 连接到 HDFS 的客户端对象
        hdfs_path (str): HDFS 上的文件路径
    """
    try:
        hdfs_client.delete(hdfs_path, recursive=False)
        print(f"File deleted from HDFS: {hdfs_path}")
    except Exception as e:
        print(e)


# if __name__ == '__main__':
#     # HDFS 和本地文件路径
#     hdfs_path = r'/raicom/data/word.csv'
#     local_path = r'../../data/word.csv'
#
#     # 连接到 HDFS
#     client = hdfs_connect_InsecureClient()
#
#     # 上传文件到 HDFS
#     hdfs_local_upload_to_hdfs(client, hdfs_path, local_path)
#
#     # 读取 HDFS 文件内容
#     read = hdfs_read_from_hdfs(client, hdfs_path)
#
#     # 删除 HDFS 文件
#     hdfs_delete_file_from_hdfs(client, hdfs_path)
#
#     # 打印读取的内容
#     print(read)
