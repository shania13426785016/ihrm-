# 导包
import unittest, logging
from api.login_api import LoginApi
from utils import assert_sommon

# 创建类


class TestIhrmLogin(unittest.TestCase):
    # 进行初始化
    def setUp(self):
        self.logina_api = LoginApi()

    def tearDown(self):
        pass

    # 编写登录成功的接口方法
    def test_01_login_success(self):
        respone = self.logina_api.login(
            {"mobile": "13800000002", "password": "123456"},
            {"Content-Type": "application/json"})
        # 用日志打印响应的结果
        logging.info("登录成功的响应结果为:{}".format(respone.json()))

        # 断言响应是否成功
        assert_sommon(self, 200, True, 10000, "操作成功", respone)

    # 实现手机号码为空
    def test_02_mobile_is_empty(self):
        respone = self.logina_api.login(
            {"mobile": "", "password": "1234567"},
            {"Content-Type": "application/json"})
        # 用日志打印响应的结果
        logging.info("实现手机号码为空响应结果为:{}".format(respone.json()))

        # 断言响应是否成功
        assert_sommon(self, 200, False, 20001, "户名或密码错误", respone)

    # 密码为空
    def test_03_password_is_eorr(self):
        respone = self.logina_api.login(
            {"mobile": "13800000002", "password": ""},
            {"Content-Type": "application/json"})
        # 用日志打印响应的结果
        logging.info("密码为空响应结果为:{}".format(respone.json()))

        # 断言响应是否成功
        assert_sommon(self, 200, False, 20001, "户名或密码错误", respone)

    # 手机号码不存在
    def test_04_mobile_is_exist(self):
        respone = self.logina_api.login(
            {"mobile": "13888889999", "password": "123456"},
            {"Content-Type": "application/json"})
        # 用日志打印响应的结果
        logging.info("手机号码不存在响应结果为:{}".format(respone.json()))

        # 断言响应是否成功
        assert_sommon(self, 200, False, 20001, "户名或密码错误", respone)

    # 无参
    def test_05_data_is_none(self):
        respone = self.logina_api.login(
            {},
            {"Content-Type": "application/json"})
        # 用日志打印响应的结果
        logging.info("无参响应结果为:{}".format(respone.json()))

        # 断言响应是否成功
        assert_sommon(self, 200, False, 20001, "户名或密码错误", respone)

    # 传入Null
    def test_06_data_is_null(self):
        respone = self.logina_api.login(None,
            {"Content-Type": "application/json"})
        # 用日志打印响应的结果
        logging.info("传入Null响应结果为:{}".format(respone.json()))

        # 断言响应是否成功
        assert_sommon(self, 200, False, 99999, "抱歉，系统繁忙，请稍后重试", respone)

    # 传入多参
    def test_07_data_is_main(self):
        respone = self.logina_api.login(
            {"mobile": "13800000002", "password": "123456", "shd": "1"},
            {"Content-Type": "application/json"})
        # 用日志打印响应的结果
        logging.info("多参响应结果为:{}".format(respone.json()))

        # 断言响应是否成功
        assert_sommon(self, 200, True, 10000, "操作成功", respone)

    # 少参-缺少mobile
    def test_08_data_is_lack(self):
        respone = self.logina_api.login(
            {"password": "123456"},
            {"Content-Type": "application/json"})
        # 用日志打印响应的结果
        logging.info("少参-缺少mobile响应结果为:{}".format(respone.json()))

        # 断言响应是否成功
        assert_sommon(self, 200, False, 20001, "用户名或密码错误", respone)

    # 少参 - 缺少password
    def test_09_data_is_lack(self):
        respone = self.logina_api.login(
            {"mobile": "13800000002"},
            {"Content-Type": "application/json"})
        # 用日志打印响应的结果
        logging.info("少参-缺少mobile响应结果为:{}".format(respone.json()))

        # 断言响应是否成功
        assert_sommon(self, 200, False, 20001, "用户名或密码错误", respone)

    # 错误参数
    def test_10_Error_parameters(self):
        respone = self.logina_api.login(
            {"mobile1": "13800000002","password": "123456"},
            {"Content-Type": "application/json"})
        # 用日志打印响应的结果
        logging.info("少参-缺少mobile响应结果为:{}".format(respone.json()))

        # 断言响应是否成功
        assert_sommon(self, 200, False, 20001, "用户名或密码错误", respone)

    # 密码错误
    def test_11_password_is_eorr(self):
        respone = self.logina_api.login(
            {"mobile1": "13800000002", "password": "1234567"},
            {"Content-Type": "application/json"})
        # 用日志打印响应的结果
        logging.info("密码错误响应结果为:{}".format(respone.json()))

        # 断言响应是否成功
        assert_sommon(self, 200, False, 20001, "用户名或密码错误", respone)
