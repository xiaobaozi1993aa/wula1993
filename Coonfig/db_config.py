import pymysql
import pytest

def coon_db():
    coon = pymysql.connect(
        host='xmzt-data.mysql.rds.aliyuncs.com',
        port=3306,
        user='xmztapi',
        password='3GY9kxeY1YZb',
        database='tour_auth',
        charset='utf8'
        )
    cursor = coon.cursor(pymysql.cursors.DictCursor)
    return cursor
#8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92

def test_ceshi_add(cursor):
    username = input('请输入用户名:')
    password = input('请输入密码:')
    sql = "select * from sys_user where username = '{}' and" \
          " `password` = '{}'".format(username, password)
    res = cursor.execute(sql)
    print(sql)
    if res:
        print(cursor.fetchall())
    else:
        print('账号或密码错误')



