# 1导包
import requests
from requests import Response
# 创建封装的接口类
class LoginApi:

    # 初始化数据方法
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    # 类方法--登录
    def login(self, data, headers):
        """
        :type:Response
        :return:
        """
        # 发送登录的请求,并返回reponse的对象
        return requests.post(url=self.login_url,
                             json=data,
                             headers=headers
                             )