# 导包
import json
import logging

import app

from logging import handlers

# 编写初始化日志代码
#1 定义初始化日志函数
def init_logging():

    # 2,创建日志器,日志严重等级
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 3,创建处理器
    sh = logging.StreamHandler()  # 控制台输出

    # 4创建文件处理器(作用保存文件存放的地址)
    log_path = app.base_dir + "./log/ihrm_repot.log"
    # 文件的保存方式
    fh = logging.handlers.TimedRotatingFileHandler(log_path,
                                                   when="M",
                                                   interval=1,
                                                   backupCount=3,
                                                   encoding="utf-8"
                                                   )

    # 5创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 6把格式化放在处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 7把处理器方在日志器中
    logger.addHandler(sh)  # 控制台输出
    logger.addHandler(fh)  # 保存到文件


# 封装通用断言函数
def assert_sommon(self, status_code, success, code, message, respone):
    """

    :param self:类方法中的传参变量名
    :param status_code: 操作成功响应状态码：200
    :param success: bool(True or False)
    :param code: int(10000,20001,99999)
    :param message: string(操作成功！,用户名或密码错误,抱歉，系统繁忙，请稍后重试)
    :param respone:请求接口响应返回的变量名
    :return:
    """
    self.assertEqual(status_code, respone.status_code)
    self.assertEqual(success, respone.json().get("success"))
    self.assertEqual(code, respone.json().get("code"))
    self.assertIn(message, respone.json().get("message"))


# 参数化--登录模块参数化
def read_login_data(filepath):
    # 打开数据文件
    with open(filepath, mode='r', encoding='utf-8') as f:
        # 使用json加载数据文件为json格式
        jsonData = json.load(f)
        # 遍历json格式的数据文件，并把数据处理成列表元组形式（[(),(),()]）添加到空列表中
        result_list = list()
        for login_data in jsonData:  # type:dict
            # 把每一组登录数据的所有values转化为元组形式，并添加到空列表当中
            result_list.append(tuple(login_data.values()))

    print("查看读取的登录数据为：", result_list)
    return result_list


# 员工管理系统参数化
def read_mep_data(filepath, interface_name):
    # 打开数据文件
    with open(filepath, "r", encoding="utf-8") as f:
        # 把数据文件加载成json格式
        json_data = json.load(f)
        # 读取加载的json数据当中对应接口的数据
        emp_data = json_data.get(interface_name)
        # print("emp_data的值为:",emp_data)
        # 把数据处理成列表元组对象，然后添加到空列表当中
        result_list = list()
        result_list.append(tuple(emp_data.values()))
        # 返回数据
        print("读取的{}员工数据为:{}".format(interface_name, result_list))
        return result_list


if __name__ == '__main__':
    # 定义数据文件的目录（注意这个路径指向数据文件一定需要存在）
    # filepath = app.base_dir + "/data/login_data.json"
    # # 读取路径中的数据，并接收返回结果
    # result = read_login_data(filepath)
    # # 打印返回的结果
    # print("返回的result_list的结果为：", result)

    # 定义员工数据路径
    filepath2 = app.base_dir + "/data/emp_data.json"
    # 读取员工数据
    read_mep_data(filepath2, 'add_emp')
    read_mep_data(filepath2, 'query_emp')
    read_mep_data(filepath2, 'modify_emp')
    read_mep_data(filepath2, 'delete_emp')