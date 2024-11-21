import yaml
from yaml import FullLoader


# 读取配置文件
def read_yaml(FilePath):
    data = None
    try:
        with open(FilePath, 'r', encoding='GBK') as file:
            data = yaml.load(file, Loader=FullLoader)
    except UnicodeDecodeError:
        with open(FilePath, 'r', encoding='UTF-8') as file:
            data = yaml.load(file, Loader=FullLoader)
    except Exception as e:
        print(f"{__file__}文件read_yaml方法发生了一个异常: {e}")
    finally:
        return data


# 测试
if __name__ == '__main__':
    filepath = r'../../practicespark/config/config.yaml'
    conf = read_yaml(filepath)
    print(conf)
