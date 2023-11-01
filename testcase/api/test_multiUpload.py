import pytest,allure
from config.config import re_config
from common.GetToken import token
from data.upload.ReadUpload import RePath
from utils.RequestUtils import ReqDt
from utils.LoggingUtil import log

@allure.epic('针对单个接口的测试')
@allure.feature('多个文件上传测试用例')
@pytest.mark.usefixtures('myfixture_multiupload')
@pytest.mark.parametrize('path',RePath.MultiUploadData())
def test_multiUpload(path):
    # 参数化时，用allure描述接口用例名称
    allure.dynamic.title('多文件上传')
    log.info(path)
    url=re_config.GetConf_url()['multiUpload_url']
    headers=token
    files=open(path,'rb')
    # # files一定是一个字典形式的参数
    res=ReqDt.post(url=url,headers=headers,files={'multipartFiles':files})
    log.info(f'多文件上传响应数据为{res}')
    # 断言
    data=res['body']['data']
    assert data=='上传成功'