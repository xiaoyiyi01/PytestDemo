import os,pymysql
from utils.YamlUtil import YamlRead


# 1.获取数据库yaml文件路径
current_proj=os.path.dirname(__file__)
dbfile=current_proj+os.sep+"db.yaml"

# 2.定义一个类
class MysqlData:

    # 3.初始化数据库文件
    def __init__(self):
        self.dbfile=dbfile

    # 4.定义一个方法获取数据库详细信息
    def db_info(self):
        # 4.1获取所有数据库详细信息
        self.dbf_info = YamlRead(self.dbfile).data()
        return self.dbf_info

    #5.连接数据库
    def db_conn(self):
        # 5.1获取数据库db1详细信息
        db_info=SqlDt.db_info()["db1"]
        # 5.2配置好db1
        conn = pymysql.connect(
            host=db_info["host"],
            user=db_info["user"],
            password=db_info["password"],
            database=db_info["database"],
            charset=db_info["charset"],
            port=db_info["port"]
        )
        return conn

SqlDt=MysqlData()
if __name__ == '__main__':
    print("获取全部数据库详细信息：",SqlDt.db_info())
    print("数据库链接成功：",SqlDt.db_conn())
    #数据库链接成功： <pymysql.connections.Connection object at 0x000001F72F42E278>

