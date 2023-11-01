import pytest,allure
from config.config import re_config
from common.GetToken import token
from data.update.ReaderUpdate import ReaUpDt
from utils.RequestUtils import ReqDt
from utils.LoggingUtil import log

@allure.epic('针对单个接口的测试')
@allure.feature('修改测试用例')
@pytest.mark.usefixtures('myfixture_updata')
@pytest.mark.parametrize('update',ReaUpDt.GetUpdateData())
def test_updata(update):
    # 参数化时，用allure描述接口用例名称
    allure.dynamic.title('修改')
    log.info(f"修改数据{update}")
    url=re_config.GetConf_url()['update_url']
    headers=token
    res=ReqDt.post(url=url,headers=headers,json=update)
    log.info(f'修改后数据为{res}')
    #断言
    data=res['body']['statusCode']
    assert data == '100001'


