import yaml
from yaml import FullLoader


def get_yaml_data(filePath=r'../../config/config.yaml'):
    with open(filePath, encoding='utf8') as file:
        data = yaml.load(file, Loader=FullLoader)
        return data


if __name__ == '__main__':
    conf = get_yaml_data()
    print(conf)
