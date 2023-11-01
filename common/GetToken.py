from config.config import re_config
from utils.RequestUtils import ReqDt

def scene_login():
    url = re_config.GetConf_url()["login_url"]
    data = {"userName": "zhangmingyue",
            "password": "1qaz@WSX"
            }
    res = ReqDt.post(url, json=data)
    token_value = str(res["headers"]["accessTokenHeader"])
    token = dict()
    token["accessTokenHeader"] = token_value
    # print("登录结果为：",res)
    return token

token=scene_login()

scene_login()