# HDFS读写操作模块
# 对 HDFS ⽂件系统中的数据进⾏操作，如上传和读取`word.csv`

from hdfs import InsecureClient

# 配置 HDFS URL 和路径
hdfs_url = 'http://master:9870'  # 替换为你的 HDFS NameNode 地址
hdfs_path = r'/data/word.csv'  # 替换为 HDFS 上的目标路径
local_path = '../data/word.csv'  # 替换为本地文件路径
user = 'root'  # 替换为你的 Hadoop 用户名

# 创建 InsecureClient 对象
client = InsecureClient(hdfs_url, user)


def upload_to_hdfs(hdfs_path, local_path):
    """将本地文件上传到 HDFS"""
    client.upload(hdfs_path, local_path)
    print(f"File uploaded to HDFS: {hdfs_path}")


def read_from_hdfs(hdfs_path):
    """从 HDFS 读取文件内容"""
    with client.read(hdfs_path) as reader:
        content = reader.read().decode('utf-8')  # 将字节流解码为字符串
    return content


def main():
    # 上传本地文件到 HDFS
    upload_to_hdfs(hdfs_path, local_path)

    # 从 HDFS 读取文件内容
    content = read_from_hdfs(hdfs_path)
    print(f"Content of HDFS file: {content}")


if __name__ == "__main__":
    main()
