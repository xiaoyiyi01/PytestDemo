import pytest,allure
from config.config import re_config
from utils.RequestUtils import ReqDt
from utils.LoggingUtil import log
from utils.AssertUtils import AssertResult
from data.upload.ReadUpload import RePath
from common.GetToken import token

@allure.epic('针对场景测试用例')
@allure.feature('场景：登录-新增-查询-修改-删除-上传单个文件-上传多个文件')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures('myfixture_class')
class TestScene:

    #登录
    @allure.story('登录测试')
    @allure.title('登录')
    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures('myfixture_login')
    def test_scene_login(self):
        url = re_config.GetConf_url()["login_url"]
        data = {"userName": "zhangmingyue",
                "password": "1qaz@WSX"
                }
        res = ReqDt.post(url, json=data)
        # 将结果以日志的方式打印出来
        # log.info("登录返回结果为{}".format(res))
        # 设置断言并打印出日志文件
        data=res['body']['data']
        log.info(AssertResult().Assert_json(data,"login success"))

    # 新增数据
    @allure.story('新增数据测试')
    @allure.title('新增')
    @pytest.mark.run(order=2)
    @pytest.mark.usefixtures('myfixture_add')
    def test_scene_add(self):
        url=re_config.GetConf_url()["add_url"]
        data={"platformname":"张三sdfa",
            "ipaddress":"192.168.3.10"}
        #将token值通过confitest.py文件导入到请求头
        headers = token
        res=ReqDt.post(url,json=data,headers=headers)
        # 将结果以日志的方式打印出来
        # log.info("新增数据为{}".format(res))
        #将platformid声明为全局变量，以便一下的类方法可以调用
        global platformid
        platformid=res["body"]["platformid"]
        # print("platformid的值为",platformid)
        data=res['body']['platformname']
        log.info(AssertResult().Assert_inbody(data,'张三sdfa'))

    #查询数据
    @allure.story('查询数据测试')
    @allure.title('查询')
    @pytest.mark.run(order=3)
    @pytest.mark.usefixtures('myfixture_search')
    def test_scene_search(self):
        #platformid参数通过url传入,将platformid拼接到url内
        url=re_config.GetConf_url()["search_url"]+'/'+platformid
        headers = token
        res=ReqDt.get(url=url,headers=headers)
        # log.info("查询结果为{}".format(res))
        data=res['body']['platformid']
        log.info(AssertResult().Assert_json(data,platformid))

    #修改数据
    @allure.story('修改数据测试')
    @allure.title('修改')
    @pytest.mark.run(order=4)
    @pytest.mark.usefixtures('myfixture_updata')
    def test_scene_updata(self):
        url=re_config.GetConf_url()['update_url']
        headers = token
        #通过id查找要修改的数据
        data={"platformid": platformid,
                "platformname": "白云区",
                "ipaddress": "192.168.3.10" }
        res=ReqDt.post(url=url,headers=headers,json=data)
        # log.info("修改后的数据为{}".format(res))
        data=res['body']['platformname']
        log.info(AssertResult().Assert_json(data,"白云区"))

    # 删除数据
    @allure.story('删除数据测试')
    @allure.title('删除')
    @pytest.mark.run(order=5)
    @pytest.mark.usefixtures('myfixture_delete')
    def test_scene_delete(self):
        url=re_config.GetConf_url()['delete_url']
        headers = token
        #这个platformid是通过params传参
        params={'id':platformid}
        res=ReqDt.get(url=url,headers=headers,params=params)
        # log.info("删除后的数据为{}".format(res))
        data=res['body']['statusCode']
        log.info(AssertResult().Assert_json(data,'000000'))

    #单个文件上传
    @allure.story('单个文件上传测试')
    @allure.title('单个文件上传')
    @pytest.mark.run(order=6)
    @pytest.mark.usefixtures('myfixture_singleupload')
    def test_singleUpload(self):
        url = re_config.GetConf_url()['singleUpload_url']
        headers = token
        files = open(RePath.SingleUploadData(), 'rb')
        # 传入的文件必须是一个字典
        res = ReqDt.post(url=url, headers=headers, files={'multipartFile': files})
        # log.info(f"上传文件结果为{res}")
        # 断言
        data = res['body']['data']
        assert data == '上传成功'

    #多个文件上传
    @allure.story('多个文件上传测试')
    @allure.title('多个文件上传')
    @pytest.mark.run(order=7)
    @pytest.mark.usefixtures('myfixture_multiupload')
    @pytest.mark.parametrize('files', RePath.MultiUploadData())
    def test_multiUpload(self, files):
        log.info(files)
        url = re_config.GetConf_url()['multiUpload_url']
        headers=token
        files = open(files,'rb')
        # # files一定是一个字典形式的参数
        res = ReqDt.post(url=url, headers=headers, files={'multipartFiles': files})
        # log.info(f'上传多个文件结果为{res}')
        # 断言
        data = res['body']['data']
        assert data == '上传成功'


if __name__ == '__main__':
    pytest.main(['test_scene_all.py','-vs'])
