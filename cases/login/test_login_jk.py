import json
import os
import pytest
import requests
import pymysql
from utils.login_sql_util import get_data
import time

class TestLogin():

    @pytest.mark.parametrize('yzm', get_data())
    def test_login(self, yzm):
        print(yzm)
        url = 'https://b2b2c-api-test.mall4j.com/smsLogin'
        data = {"passWord": yzm, "socialType": 4, "tempUid": "", "userName": "17111111111"}
        res = requests.post(url, json=data).json()
        print(res)
        user_token = res['data']['accessToken']
        print('用户的token为：：' + user_token)
