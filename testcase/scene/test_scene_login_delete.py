import pytest,allure
from config.config import re_config
from utils.RequestUtils import ReqDt
from utils.LoggingUtil import log
from utils.AssertUtils import AssertResult
from common.GetToken import token
from utils.MysqlUtils import MysqlDt

@allure.epic('针对场景测试用例')
@allure.feature('场景：登录-删除')
@pytest.mark.usefixtures('myfixture_class')
class TestLoginDelete:

    #登录
    @allure.title('第一步登录测试')
    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures('myfixture_login')
    def test_scene_login(self):
        url = re_config.GetConf_url()["login_url"]
        data = {"userName": "zhangmingyue",
                "password": "1qaz@WSX"
                }
        res = ReqDt.post(url, json=data)
        # 将结果以日志的方式打印出来
        log.info("登录返回结果为{}".format(res))
        # 设置断言并打印出日志文件
        data=res['body']['data']
        log.info(AssertResult().Assert_json(data,"login success"))

    # 删除用户数据
    @allure.title('第二步删除测试')
    @pytest.mark.run(order=2)
    @pytest.mark.usefixtures('myfixture_delete')
    def test_scene_delete(self):
        url=re_config.GetConf_url()['delete_url']
        headers = token
        #链接数据库db1,查找相关内容，再进行删除
        params=(MysqlDt.fetchall("select platformid from NY_PLATFORM_INFO where platformname='仙剑奇侠1'"))
        print(params)
        #注意参数样式字典的key为id，不是platformid（测试文档要求）
        res=ReqDt.get(url=url,headers=headers,params={'id':params[0]['platformid']})
        log.info("删除后的数据为{}".format(res))
        data=res['body']['statusCode']
        log.info(AssertResult().Assert_json(data,'000000'))


if __name__ == '__main__':
    pytest.main(['test_scene_all.py','-vs'])
