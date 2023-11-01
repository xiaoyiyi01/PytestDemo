import os
from utils.YamlUtil import YamlRead

# 1.获取项目基本目录
# 1.1获取当前项目的绝对路径
current=os.path.abspath(__file__)
# print("1",current)
base_dir=os.path.dirname(os.path.dirname(current))
# print("2",base_dir)
# 1.2定义config目录的路径
config_path=base_dir+os.sep+"config"
# print("3",config_path)
# 1.3定义confi.yaml目录的路径
config_yaml_path=config_path+os.sep+"config.yaml"
# print("4",config_yaml_path)
#1.4将config_path变为可调用
def ConfigPath():
    return config_path
#1.5将config_yaml_path路径变为可调用
def ConfigYamlPath():
    return config_yaml_path
# 2.读取配置文件
# 2.1定义一个类初始化yaml读取配置文件
class Config_yaml:
    def __init__(self,config_yaml_path):
        self.config_yaml=YamlRead(config_yaml_path).data()
# 2.2定义方法获取domain
    def GetConf_domain(self):
        return self.config_yaml["domain"]
# 2.3定义方法获取url
    def GetConf_url(self):
        return self.config_yaml["url"]

re_config=Config_yaml(config_yaml_path)


if __name__ == '__main__':
    re_config=Config_yaml(config_yaml_path)
    print(re_config.GetConf_url())
    print(re_config.GetConf_domain())



