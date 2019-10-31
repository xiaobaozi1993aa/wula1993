# coding: utf-8
import pytest
# import public
# import read_testcase
# import record

# 获取一个账号token，全局变量
public.getalltoken()
# 测试用例实例化
testcase = read_testcase.case()


# 所有测试用例开始前执行的文件，只执行一次
def setup_module(module):  # 每次开始测试执行一次
    print("setup_module")


# 所有测试用例结束后执行的文件，只执行一次
def teardown_module(module):  # 每次测试完成执行一次
    print("teardown_module")


# 每个测试用开始执行一次
def setup_function(function):
    print("setup_function")


# 每个测试用例执行完执行一次
def teardown_function(function):
    print("teardown_function")


# 装饰器 pytest 整合的测试用例生成多个结果
@pytest.mark.parametrize('mycase', testcase.testcase_list, ids=testcase.testcasename)
def test_all(mycase):
    testcase = mycase['Testcase_name'] + str(mycase['Testcase_ID']) + '.' + str(mycase['ID']) + ":" + mycase['Name']
    # print(mycase['Name'])
    # pytest.skip("skip testcase: (%s)" % mycase['Name'])
    # pytest.xfail("previous test skip (%s)" % mycase['Name'])
    mycase = public.get_Precondition(mycase)

    # 执行接口的测试
    r = public.request_method(mycase)
    try:
        print(r.status_code)
        print(r.json())
    except Exception as e:
        print(r.content)
        print(e)
    # 对返回数据进行断言
    public.assert_method(r, mycase)
    # 记录测试用例名称存储log
    record.record_testcase_name(testcase)
    # 记录测试时使用的数据
    record.record_testcase_msg(mycase)

