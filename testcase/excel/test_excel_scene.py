import json,pytest,allure
from data.excel.ReadExcel import ExcDt
from utils.RequestUtils import ReqDt
from utils.AssertUtils import AssRes
from common.GetToken import token
from utils.LoggingUtil import log

@allure.epic("使用excel管理场景测试用例")
@allure.feature('场景：登录-测试')
@pytest.mark.parametrize('excel',ExcDt.GetExcelData())
def test_excle(excel):
    url = excel['请求URL']
    method=excel['请求类型']
    params=excel['请求参数']
    expect_data=excel['预期结果']
    allure.dynamic.title('登录')
    if str(method).lower()=="post":
        res=ReqDt.post(url=url,json=json.loads(params))
        log.info(f'post请求返回结果{res}')
        #断言
        acture_data=res['body']['data']
        assert acture_data == expect_data
        allure.dynamic.title('查询')
    elif str(method).lower()=='get':
        #参数需要放在url里面
        url_get=url+"/"+params
        #需要在请求头添加token
        res=ReqDt.get(url=url_get,headers=token)
        log.info(f'get请求返回结果{res}')
        #断言
        acture_data=res['body']['platformid']
        log.info(AssRes.Assert_json(acture_data,expect_data))










