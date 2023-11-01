import requests
import pytest
from config.config import re_config
import json as complexjson
from utils.LoggingUtil import log


#1.定义一个发送请求的类
class RequestParams:
    #2.初始化session,如果token不是保存在header里面，那么就可以直接用cookies访问
    def __init__(self):
        self.session=requests.session()
    #3.定义get请求方法
    def get(self,url,params=None,**kwargs):
        return self.request(url,"get",params=params,**kwargs)

    # 4.定义post请求
    def post(self,url,json=None,**kwargs):
        return self.request(url,"post",json=json,**kwargs)

    # 5.定义put请求
    def put(self,url,**kwargs):
        return self.request(url,"put",**kwargs)

    # 6.定义delete请求
    def delete(self,url,**kwargs):
        return self.request(url,"delete",**kwargs)

    def request(self, url, method, data=None, json=None, **kwargs):
        # url为主机域名和端口+路径
        url = re_config.GetConf_domain() + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("params")
    # 7.设置请求参数以log形式输出
        self.request_log(url, method, data, json, params, headers, files, cookies)
        if method == "GET":
            return self.session.get(url, **kwargs)
        if method == "POST":
            return self.session.post(url, data, json, **kwargs)
        if method == "PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(json)
            return self.session.put(url, data, **kwargs)
        if method == "DELETE":
            return self.session.delete(url, **kwargs)
        if method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            return self.session.patch(url, data, **kwargs)
    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None,
                    **kwargs):
        log.info("接口请求地址 ==>> {}".format(url))
        log.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        log.info("接口请求头 ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        log.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        log.info("接口请求体 data 参数 ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        log.info("接口请求体 json 参数 ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        log.info("接口上传附件 files 参数 ==>> {}".format(files))
        log.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))
