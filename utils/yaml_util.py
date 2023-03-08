'''
    YAML的工具包
'''
import yaml

class YamlUtil:

    def __init__(self, yaml_file):
        '''
        通过init方法把YAML文件传入到这里类
        :param yaml_file:
        '''
        self.yaml_file = yaml_file

    # 读取YAML文件
    def read_yaml(self):
        '''
        读取yaml,对yaml反序列化，就是把yaml格式转换成dict(字典)格式
        :return:
        '''
        # 打开文件
        with open(self.yaml_file, encoding='utf-8') as f:
            # 把文件加载进来， Loader=yaml.FullLoader表示加载的方式
            value = yaml.load(f, Loader=yaml.FullLoader)
            # print(value)
            return value

if __name__ == '__main__':
    YamlUtil('test_api.yaml').read_yaml()