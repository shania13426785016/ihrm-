# 1导包
import logging
import unittest
import app
from api.empolyee_api import EmpolyeeApi
from api.login_api import LoginApi
from utils import assert_sommon


# 2定义测试类
class TestIhrmEmpliyee(unittest.TestCase):
    # 3定义类初始化方法
    def setUp(self):
        self.login_api1 = LoginApi()
        self.empolyeeapi = EmpolyeeApi()

    def tearDown(self):
        pass

    # 4定义测试方法
    # 实现登录成功的接口
    def test01_login_success(self):
        # 发送登录的接口请求
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api1.login(jsonData,
                                         {"Content-Type": "application/json"})
        # 打印登录接口返回的结果
        logging.info("登录接口返回的结果为：{}".format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # 打印请求头
        logging.info("保存到全局变量中的请求头为：{}".format(app.HEADERS))
        # 断言
        assert_sommon(self, 200, True, 10000, "操作成功", response)

    # 2添加员工
    def test_02_add_emp(self):
        respone = self.empolyeeapi.add_emp("花花1","13477047807", app.HEADERS)
        # 打印添加员工的结果
        logging.info("打印添加员工的结果:{}".format(respone.json()))
        # 提取员工公的id保存到全局变量当中
        app.EMP_ID=respone.json().get("data").get("id")
        # 打印出保存的员工id
        logging.info("保存的员工id:{}".format(app.EMP_ID))
        # 断言
        assert_sommon(self, 200, True, 10000, "操作成功", respone)

    # 3 查询员工
    def test_03_modify_emp(self):
        # 发送查询员工的接口请求
        respone = self.empolyeeapi.query_emp(app.EMP_ID, app.HEADERS)
        # 打印查询员工接口的响应数据
        # print("查询员工接口的响应数据:", respone.json())
        logging.info("查询员工接口的响应数据:{}".format(respone.json()))
        # 断言
        assert_sommon(self, 200, True, 10000, "操作成功", respone)

    # 4 修改员工信息
    def test_04_modify_emp(self):
        # 发送修改员工的请求
        respone = self.empolyeeapi.modify_emp(app.EMP_ID, {"username": "妈妈"}, app.HEADERS)
        # 查看修改后的响应体
        logging.info("查看修改后的响应体:{}".format(respone.json()))
        # 断言
        assert_sommon(self, 200, True, 10000, "操作成功", respone)

    # 5 删除员工
    def test_05_delete_emp(self):
        # 发送删除员工的请求
        respone= self.empolyeeapi.delete_emp(app.EMP_ID, app.HEADERS)
        # 查看删除员工后的状态
        logging.info("删除员工后的状态:{}".format(respone.json()))
        # 断言
        assert_sommon(self, 200, True, 10000, "操作成功", respone)
