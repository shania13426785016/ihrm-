# 导包
import requests
# 创建呀封装的类
class EmpolyeeApi:
    # 类的初始化方法
    def __init__(self):
        self.emp_url = "http://ihrm-test.itheima.net/api/sys/user/"

    # 类方法--添加员工
    def add_emp(self, username, mobile, headers):
        # 需要外部出入的数据
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-06-08",
            "formOfEmployment": 1,
            "departmentName": "测试部",
            "departmentId": "1063678149528784896",
            "correctionTime": "2020-05-30T16:00:00.000Z"
        }
        return requests.post(url=self.emp_url, json=data, headers=headers)

    # 类方法--查询员工
    def query_emp(self, emp_id, headers):
        # 查询员工url
        query_url=self.emp_url + emp_id
        # 发送查询员工的接口请求，并return返回结果
        return requests.get(url=query_url, headers=headers)

    # 类方法--修改员工
    def modify_emp(self, emp_id, jsondata, headers):
        # 拼接修改员工的URL
        modify_url =self.emp_url + emp_id
        # 发送修改员工的接口请求，并 return返回结果
        return requests.put(url=modify_url, headers=headers, json=jsondata)

    # 类方法--删除员工
    def delete_emp(self, token_id, headers):
        query_url = self.emp_url + token_id
        return requests.delete(url=query_url,headers=headers)