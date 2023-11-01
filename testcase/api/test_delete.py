import pytest,allure
from config.config import re_config
from common.GetToken import token
from utils.RequestUtils import ReqDt
from utils.LoggingUtil import log
from data.delete.ReadDelete import DelDt

@allure.epic('针对单个接口的测试')
@allure.feature('删除测试用例')
@pytest.mark.usefixtures('myfixture_delete')
@pytest.mark.parametrize('delete',DelDt.GetDeleteData())
def test_delete(delete):
    # 参数化时，用allure描述接口用例名称
    allure.dynamic.title('删除')
    log.info(delete)
    url=re_config.GetConf_url()['delete_url']
    headers=token
    res=ReqDt.get(url=url,headers=headers,params=delete)
    print(f"删除结果{res}")