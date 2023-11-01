import pytest,allure
from config.config import re_config
from data.login.ReadLogin import LogDt
from utils.RequestUtils import ReqDt
from utils.LoggingUtil import log
from utils.AssertUtils import AssertResult

@allure.epic('针对单个接口的测试')
@allure.feature('登录测试用例')
@pytest.mark.usefixtures('myfixture_login')
@pytest.mark.parametrize("login", LogDt.GetLoginData())
# login作为形参传递参数，具体参数从列表LogDt.GetLoginData()获取
def test_login(login):
    # 参数化时，用allure描述接口用例名称
    allure.dynamic.title('登录')
    # url为主机域名和端口+路径
    url=re_config.GetConf_url()["login_url"]
    # login为包含username和password的字典
    res=ReqDt.post(url=url,json=login)
    log.info("登录结果为{}".format(res))
    data=res['body']['desc']
    log.info(AssertResult().Assert_json(data,'用户名或密码错误!'))

if __name__ == '__main__':
    pytest.main(["test_login.py","-vs"])