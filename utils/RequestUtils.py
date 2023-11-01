import requests
from config.config import re_config

#1.定义一个发送请求的类
class RequestData:

    # 2.初始化session,如果token不是保存在header里面，那么就可以直接用cookies访问
    def __init__(self):
        self.session = requests.session()

    # 3.定义get请求方法
    def get(self, url, params=None, **kwargs):
        return self.requestdata(url, "get", params=params, **kwargs)

    # 4.定义post请求
    def post(self, url, json=None, files=None, **kwargs):
        return self.requestdata(url, "post", json=json, files=files, **kwargs)

    # 5.定义put请求
    def put(self, url, **kwargs):
        return self.requestdata(url, "put", **kwargs)

    # 6.定义delete请求
    def delete(self, url, **kwargs):
        return self.requestdata(url, "delete", **kwargs)

    # 7.定义一个公共的方法获取影响数据
    def requestdata(self, url, method=None, params=None, files=None,data=None, json=None, **kwargs):
        url = re_config.GetConf_domain() + url
        r = self.session.request(url=url,method=method,params=params, files=files,data=data, json=json, **kwargs)
        # 7.1获取响应的内容
        code = r.status_code
        cookies = r.cookies
        headers = r.headers
        try:
            body = r.json()
        except Exception as error:
            body = r.text
        # 7.2将响应的内容放入字典内
        res = dict()
        res["code"] = code
        res["body"] = body
        res["cookies"] = cookies
        res["headers"] = headers
        # 7.3字典返回数据
        return res

ReqDt=RequestData()