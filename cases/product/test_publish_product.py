import json
import os
import pytest
import requests

from utils.yaml_util import YamlUtil

# 发布商品
class TestPublishProduct():
    # 这样获取不到yaml文件的路径
    # @pytest.mark.parametrize('args', YamlUtil('test_api.yaml').read_yaml())
    @pytest.mark.parametrize('args', YamlUtil(os.getcwd()+'/config/product/PublishProduct.yaml').read_yaml())
    def test_publish_product(self, args, multishop_token):
        # 路径，获取yaml配置文件中设置的url
        url = args['request']['url']
        # 需要传入的数据,获取yaml配置文件中设置的参数
        data = args['request']['json']
        # headers = args['request']['headers']
        headers = multishop_token
        # 发送post请求
        res = requests.post(url, json=data, headers=headers).json()
        print(res)
        prodId = res['data']
        print('商品id为:' + str(prodId))

        return prodId