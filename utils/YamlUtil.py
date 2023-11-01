import yaml

# 1.创建一个类
class YamlRead:
# 2.以列表字典形式读取单个yaml文件
    def __init__(self,yamlf):
        self.yamlf=yamlf

    def data(self):
        with open(self.yamlf,"rb") as f:
            data=yaml.safe_load(f)
            # data_list=[]
            # data_list.append(data)
            # print(data_list)
        return data

# 3.以列表字典形式读取多个yaml文件
    def data_all(self):
        with open(self.yamlf,"rb") as f:
            data_all=yaml.safe_load_all(f)
            for i in data_all:
                data_all_list=[]
                data_all_list.append(data_all)
                # print(data_all_list)
            return data_all_list


if __name__ == '__main__':
    yaml_read_data = YamlRead(r"G:\zmyWorkSpace\10.20pytest\config\config.yaml")
    print(yaml_read_data.data())

