import os
from utils.YamlUtil import YamlRead

current_path=os.path.dirname(__file__)
addfile=current_path+os.sep+'add.yaml'

class AddData:

    def __init__(self):
        self.YamlRead=YamlRead(addfile).data()

    def GetAddData(self):
        return self.YamlRead

AddDt=AddData()

if __name__ == '__main__':
    print(AddDt.GetAddData())