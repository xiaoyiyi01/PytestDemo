import os.path
from utils.YamlUtil import YamlRead

current_path=os.path.dirname(__file__)
update_path=current_path+os.sep+'update.yaml'

class ReaderUpdate:

    def __init__(self):
        self.YamlRead=YamlRead(update_path).data()

    def GetUpdateData(self):
        return self.YamlRead

ReaUpDt=ReaderUpdate()

if __name__ == '__main__':
    print(ReaUpDt.GetUpdateData())