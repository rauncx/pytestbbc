import pymysql
import pytest
import requests


# 发送并获取验证码
def get_data():

    # 发送验证码的接口路径
    url = 'https://b2b2c-api-test.mall4j.com/sms/sendLoginCode'
    # 参数
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
    # sql语句
    sql = 'SELECT mobile_code FROM tz_sms_log WHERE user_phone = 17111111111 AND `type` = 13 ORDER BY rec_date DESC LIMIT 1'
    # 执行sql语句
    cursor.execute(sql)
    data = cursor.fetchone()
    # 关闭数据库
    db.close()
    print(data)
    return data

if __name__ == '__main__':
    get_data()

