import pytest,allure
from config.config import re_config
from utils.RequestUtils import ReqDt
from common.GetToken import scene_login
from data.add.ReadAdd import AddDt
from utils.LoggingUtil import log
from utils.AssertUtils import AssertResult


@allure.epic('针对单个接口的测试')
@allure.feature('新增测试用例')
@pytest.mark.usefixtures('myfixture_add')
@pytest.mark.parametrize('add',AddDt.GetAddData())
def test_add(add):
    # 参数化时，用allure描述接口用例名称
    allure.dynamic.title('新增')
    url=re_config.GetConf_url()["add_url"]
    headers=scene_login()
    res=ReqDt.post(url,json=add,headers=headers)
    # 打印响应结果
    log.info("新增数据为{}".format(res))
    # 断言
    data=res['body']['statusCode']
    log.info(AssertResult().Assert_json(data,'100001'))

if __name__ == '__main__':
    pytest.main(['test.add.py','-vs'])



