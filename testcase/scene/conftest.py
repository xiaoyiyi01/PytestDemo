import pytest
from utils.LoggingUtil import log


# 1.设置class函数级别的夹具
@pytest.fixture(scope='class')
def myfixture_class():
    log.info("...........场景测试开始...........")
    yield
    log.info("...........情景测试结束...........")

# 2.设置function级别函数夹具
@pytest.fixture(scope="function")
def myfixture_login():
    log.info("...........登录测试开始...........")
    yield
    log.info("...........登录测试结束...........")

@pytest.fixture(scope="function")
def myfixture_add():
    log.info("...........新增测试开始...........")
    yield
    log.info("...........新增测试结束...........")

@pytest.fixture(scope="function")
def myfixture_updata():
    log.info("...........更新测试开始...........")
    yield
    log.info("...........更新测试结束...........")

@pytest.fixture(scope="function")
def myfixture_search():
    log.info("...........查询测试开始...........")
    yield
    log.info("...........查询测试结束...........")

@pytest.fixture(scope="function")
def myfixture_delete():
    log.info("...........删除测试开始...........")
    yield
    log.info("...........删除测试结束...........")

@pytest.fixture(scope="function")
def myfixture_singleupload():
    log.info("...........单个文件测试开始...........")
    yield
    log.info("...........单个文件测试结束...........")

@pytest.fixture(scope="function")
def myfixture_multiupload():
    log.info("...........多个文件测试开始...........")
    yield
    log.info("...........多个文件测试结束...........")