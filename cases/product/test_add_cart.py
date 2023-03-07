import json
import os
import pytest
import requests

from lib.yaml_util import YamlUtil


class TestAddCart():

    # # 获取商品详情
    # @pytest.mark.parametrize('args', YamlUtil(os.getcwd()+'/lib/product/addcart.yaml').read_yaml())
    # def test_product_details(self, args):
    #     # 路径，获取yaml配置文件中设置的url
    #     url = args['request']['url']
    #     # print(url)
    #     # 需要传入的数据,获取yaml配置文件中设置的参数
    #     params = args['request']['params']
    #     # print(params)
    #     headers = args['request']['headers']
    #     # print(headers)
    #     # 发送get请求
    #     res = requests.get(url, params=params, headers=headers).json()
    #     prodId = res['data']['prodId']
    #     shopid = res['data']['shopId']
    #     # print('店铺id' + str(shopid))
    #     skuid = res['data']['skuList'][0]['skuId']
    #     # print('skuid为' + str(skuid))
    #     # print(res)
    #     return prodId, shopid, skuid

    # 将商品加入购物车
    @pytest.mark.parametrize('args', YamlUtil(os.getcwd()+'/lib/product/addcart.yaml').read_yaml())
    def test_add_cart(self, args):
        # 路径，获取yaml配置文件中设置的url
        url = args['request']['url']
        print(url)
        # 需要传入的数据,获取yaml配置文件中设置的参数
        params = args['request']['params']
        print(params)
        headers = args['request']['headers']
        print(headers)
        # 发送post请求
        res = requests.post(url, json=params, headers=headers)
        print(res.text)