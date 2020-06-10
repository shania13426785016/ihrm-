# 1导包
import requests
# 2请求登录接口
respone = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                        json={"mobile":"13800000002","password":"123456"},
                        headers={"Content-Type":"application/json"}
                        )
# 3 查看返回的响应数据
print("登录成功:",respone.json())