import os


current_path=os.path.dirname(__file__)
a_path = current_path + os.sep + 'a.jpg'
b_path = current_path + os.sep + 'b.jpg'
c_path = current_path + os.sep + 'c.jpg'
learn_path = current_path + os.sep + 'learn.png'
excel_path=current_path+os.sep+'excel_data.xlsx'
single_file=excel_path
multi_files = [a_path, b_path, c_path, learn_path]

class ReadUploadPath:

    def SingleUploadData(self):
        return single_file

    def MultiUploadData(self):
        return multi_files

RePath=ReadUploadPath()

if __name__ == '__main__':
    print(RePath.MultiUploadData())

