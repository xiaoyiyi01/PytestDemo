import os
from utils.YamlUtil import YamlRead

current_path=os.path.dirname(__file__)
searchfile=current_path+os.sep+'search.yaml'

class SearchData:

    def __init__(self):
        self.YamlRead=YamlRead(searchfile).data()

    def GetSearchData(self):
        # 注意返回的数据一定是列表
        return self.YamlRead['platformid']

SeaDt=SearchData()
if __name__ == '__main__':
    print(SeaDt.GetSearchData())

