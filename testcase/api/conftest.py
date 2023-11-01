import pytest
from utils.LoggingUtil import log


# 1.设置function级别函数夹具
@pytest.fixture(scope="function")
def myfixture_login():
    log.info("...........登录开始...........")
    yield
    log.info("...........登录结束...........")

@pytest.fixture(scope="function")
def myfixture_add():
    log.info("...........新增开始...........")
    yield
    log.info("...........新增结束...........")

@pytest.fixture(scope="function")
def myfixture_search():
    log.info("...........查询开始...........")
    yield
    log.info("...........查询结束...........")

@pytest.fixture(scope="function")
def myfixture_delete():
    log.info("...........删除开始...........")
    yield
    log.info("...........删除结束...........")

@pytest.fixture(scope="function")
def myfixture_updata():
    log.info("...........更新开始...........")
    yield
    log.info("...........更新结束...........")

@pytest.fixture(scope="function")
def myfixture_singleupload():
    log.info("...........单个文件上传开始...........")
    yield
    log.info("...........单个文件上传结束...........")

@pytest.fixture(scope="function")
def myfixture_multiupload():
    log.info("...........单个文件上传开始...........")
    yield
    log.info("...........单个文件上传结束...........")
