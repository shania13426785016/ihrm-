# 导包
import time
import unittest
import HTMLTestRunner_PY3
import app
from script.test_emp_params import TestIhrmEmpliyeeParams



# 实例化测试套件
from script.test_login_params import TestLogin

suit = unittest.TestSuite()
# 添加测试用例
suit.addTest(unittest.makeSuite(TestIhrmEmpliyeeParams))
suit.addTest(unittest.makeSuite(TestLogin))
# 测试报告的命名和存放位置
file_name = app.base_dir + "/report/ihrm.html"
# 将测试报告写入命名好的测试文件里面
with open(file_name, "wb")as f:
    # 选择测试报告模式
    sunner = HTMLTestRunner_PY3.HTMLTestRunner(f, title="ihrm测试报告",
                                               description="漂亮的测试报告-员工的增删改查")
    # 运行测试报告
    sunner.run(suit)
print("*" * 100)
print("增加轮巡构建效果")