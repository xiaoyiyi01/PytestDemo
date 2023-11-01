import os.path
from utils.YamlUtil import YamlRead

current_path=os.path.dirname(__file__)
delete_path=current_path+os.sep+"delete.yaml"

class DeleteData:

    def __init__(self):
        self.YamlRead=YamlRead(delete_path).data()

    def GetDeleteData(self):
        return self.YamlRead

DelDt=DeleteData()

if __name__ == '__main__':
    print(DelDt.GetDeleteData())