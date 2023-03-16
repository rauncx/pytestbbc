import pymysql
import pytest
import requests

# class LoginYzmSql():
#
#     def test_yzm(self):
#         # 路径，获取yaml配置文件中设置的url
#         url = 'https://b2b2c-api-test.mall4j.com/sms/sendLoginCode'
#         # 需要传入的数据,获取yaml配置文件中设置的参数
#         data = {"mobile": "18144632758"}
#         # 发送post请求
#         res = requests.post(url, json=data).json()
#         print(res)

# 获取用户发送的验证码
def get_data():

    # 路径，获取yaml配置文件中设置的url
    url = 'https://b2b2c-api-test.mall4j.com/sms/sendLoginCode'
    # 需要传入的数据,获取yaml配置文件中设置的参数
    data = {"mobile": "17111111111"}
    # 发送post请求
    res = requests.post(url, json=data).json()
    print(res)

    # 打开数据库连接
    db = pymysql.connect(
        user='test',
        password='test',
        host='192.168.1.18',
        port=30750,
        db='mall4j_b2b2c_test',
        )

    # 创建游标对象
    cursor = db.cursor()

    sql = 'SELECT mobile_code FROM tz_sms_log WHERE user_phone = 17111111111 AND `type` = 13 ORDER BY rec_date DESC LIMIT 1'

    cursor.execute(sql)
    data = cursor.fetchone()
    db.close()
    print(data)
    return data

if __name__ == '__main__':
    get_data()

