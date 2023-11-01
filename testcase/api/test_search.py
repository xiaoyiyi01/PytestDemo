import pytest,allure
from data.search.ReadSearch import SeaDt
from config.config import re_config
from common.GetToken import scene_login
from utils.RequestUtils import ReqDt
from utils.LoggingUtil import log

@allure.epic('针对单个接口的测试')
@allure.feature('查找测试用例')
@pytest.mark.usefixtures('myfixture_search')
@pytest.mark.parametrize('search',SeaDt.GetSearchData())
def test_search(search):
    # 参数化时，用allure描述接口用例名称
    allure.dynamic.title('查找')
    log.info(search)
    url=re_config.GetConf_url()['search_url']+'/'+search
    headers=scene_login()
    res=ReqDt.get(url=url,headers=headers)
    log.info(f'查找数据为{res}')
    code=res['code']
    assert code==200


if __name__ == '__main__':
    pytest.main(['test.search.py','-vs'])