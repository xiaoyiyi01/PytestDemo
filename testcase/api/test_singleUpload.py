import pytest,allure
from data.upload.ReadUpload import RePath
from config.config import re_config
from common.GetToken import token
from utils.RequestUtils import ReqDt
from utils.LoggingUtil import log

@allure.epic('针对单个接口的测试')
@allure.feature('单个文件上传测试用例')
@pytest.mark.usefixtures('myfixture_singleupload')
def test_singleUpload():
    # 参数化时，用allure描述接口用例名称
    allure.dynamic.title('单个文件上传')
    url=re_config.GetConf_url()['singleUpload_url']
    headers=token
    files=open(RePath.SingleUploadData(),'rb')
    # 传入的文件必须是一个字典
    res=ReqDt.post(url=url,headers=headers,files={'multipartFile':files})
    log.info(f'单文件响应数据为{res}')
    #断言
    data=res['body']['data']
    assert data == '上传成功'

