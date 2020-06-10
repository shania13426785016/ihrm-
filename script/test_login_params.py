# 导包
import unittest, logging

from parameterized import parameterized

import app
from api.login_api import LoginApi
from utils import assert_sommon, read_login_data


# 创建类


class TestLogin(unittest.TestCase):
    # 进行初始化
    def setUp(self):
        self.logina_api = LoginApi()

    def tearDown(self):
        pass

    filepath = app.base_dir + "/data/login_data.json"
    @parameterized.expand(read_login_data(filepath))
    # 编写登录成功的接口方法
    def test_01_login(self, case_name,request_body, success,code,message,http_code):
        respone = self.logina_api.login(
            request_body,
            {"Content-Type": "application/json"})
        # 用日志打印响应的结果
        logging.info("登录成功的响应结果为:{}".format(respone.json()))

        # 断言响应是否成功
        assert_sommon(self, http_code, success, code, message, respone)