import pytest
import requests
import pytest_html
import public
from Coonfig.yum_config import add_path

def test_login():
    path = '/user/login'
    url = add_path(path)
    data = {"client":"w'x","password":123456,"phone":13066909086,"version":3}
    r = requests.post(url=url, data=data)
    print('用户登陆:',r.json().get('reMsg'),'耗时{}S'.format(r.elapsed.total_seconds()))
    print(r.json())
    assert '成功' in r.json().get('reMsg')     #断言接口返回包含哪些
    assert r.elapsed.total_seconds() < 0.01     #断言返回时间小于0.1S
    return r.json().get('rel')




#域名抽离
#数据库、Redis抽离
#数据和用例抽离
#日志，报告，邮件，断言

#先只做个集成；然后是自动化；
#集成只做正确的，主要的接口



pytest.main()


