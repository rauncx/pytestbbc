import os
import pytest
from selenium import webdriver

from utils.yaml_util import YamlUtil
from utils.drivers import drivers

class TestLogin:
    @pytest.mark.parametrize('args', YamlUtil(os.getcwd()+'/config/login/login.yaml').read_yaml())
    def test_login(self, args):
        # 浏览器驱动
        driver = webdriver.Chrome(drivers())
        # 访问网站
        url = args['url']
        driver.get(url)
        driver.maximize_window()
        # 隐式等待
        driver.implicitly_wait(5)
        # 输入账号
        username_sender = driver.find_element_by_xpath(args['data']['usernamexpath'])
        username_sender.send_keys(args['data']['username'])
        # 输入密码
        password_sender = driver.find_element_by_xpath(args['data']['passwordxpath'])
        password_sender.send_keys(args['data']['password'] + '\n')
        driver.quit()