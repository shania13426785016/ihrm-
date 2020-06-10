# 1导包
import requests

# 2发送请求登录接口
respone = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                        json={"mobile":"13800000002","password":"123456"},
                        headers={"Content-Type":"application/json"}
                        )
# 打印登录的结果
print("登录成功:", respone.json())
# 提取登录返回的令牌
token = "Bearer " + respone.json().get("data")
print("令牌为:", token)


# 3 发送添加员工的接口
data={
    "username": "小名ppppp",
    "mobile": "15984444444",
    "timeOfEntry": "2020-06-08",
    "formOfEmployment": 1,
    "departmentName": "测试部",
    "departmentId": "1063678149528784896",
    "correctionTime": "2020-05-30T16:00:00.000Z"
}
headers={"Content-Type": "application/json", "Authorization": token}
respone = requests.post(url="http://ihrm-test.itheima.net/api/sys/user",
                        headers=headers,
                        json=data
                        )
# 打样添加员工的接口
print("添加员工的接口返回的信息:", respone.json())
# 提取添加员工接口返回的员工id
token_id = respone.json().get("data").get("id")
print("新增员工的token_id:", token_id)


# 4 拼接查询员工接口的url
query_url = "http://ihrm-test.itheima.net" + "/api/sys/user/" + token_id
print("拼接员工的url:", query_url)
# 发送查询员工接口的请求
respone = requests.get(url=query_url,
                       headers=headers)
# 查询打印员工信息的结果
print("查询员工的接口返回的数据:", respone.json())


# 5 拼接修改员工的URL
query_url = "http://ihrm-test.itheima.net" + "/api/sys/user/" + token_id
# 发送修改员工的接口请求
respone = requests.put(url=query_url,
                       headers=headers,
                       json={"username":"小名pppp1"}
                       )
# 打印修改员工的结果
print("修改员工信息返回的响应体:", respone.json())


# 6 拼接删除员工的URL
query_url = "http://ihrm-test.itheima.net" + "/api/sys/user/" + token_id
# 发送删除员工的接口请求
respone = requests.delete(url=query_url,
                       headers=headers
                       )
# 打印删除员工的结果
print("删除员工返回的响体信息:", respone.json())

