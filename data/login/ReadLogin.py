# 1、导入yaml模块
from utils.YamlUtil import YamlRead
import os

# 2、读取同目录的配置文件
current_path=os.path.dirname(__file__)
loginfile=current_path+os.sep+"login.yaml"

# 3、新增class 定义，增加返回数据的方法
class LoginData:

    def __init__(self):
        self.yamlReader=YamlRead(loginfile).data()

    def GetLoginData(self):
        return self.yamlReader

LogDt=LoginData()


if __name__ == '__main__':
    print(LogDt.GetLoginData())
