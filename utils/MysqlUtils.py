from config.MysqlConn import SqlDt
import pymysql
from utils.LoggingUtil import log



# 1.定义一个类
class MysqlUtilData:

    # 2.链接数据数db1
    def __init__(self):
        self.conn=SqlDt.db_conn()
    # 3.获取执行sql的光标对象(括号内的命令是让数据自动组织成字典,结果会是[{}]的结构)
        self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 4.创建查询、执行方法
    #    4.1查询数据库单条数据
    def fetchone(self, sql):
            # 执行sql语句
        self.cursor.execute(sql)
            # 获取查询结果
        return self.cursor.fetchone()
    #     4.2查询数据库全部数据
    def fetchall(self, sql):
            # 执行sql语句
        self.cursor.execute(sql)
            # 获取查询结果
        return self.cursor.fetchall()

    # 5.创建增删改、执行方法
    def exec_db(self,sql):
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            log.error("操作Mysql出现错误，错误原因：{}".format(ex))
        return True
    # 6.关闭对象
    def __del__(self):
        # 关闭光标对象
        self.cursor.close()
        # 关闭连接对象
        self.conn.close()

MysqlDt=MysqlUtilData()

if __name__ == '__main__':
    MysqlDt=MysqlUtilData()
    # print(MyslDt.yfetchone("select username from BLUESKY_BASIC_USERINFO where userid=1688310684032" ))
    print(MysqlDt.fetchall("select * from BLUESKY_BASIC_USERINFO" ))
    # print(MysqlDt.exec_db("UPDATE BLUESKY_BASIC_USERINFO SET username = '李四' WHERE userid = '1688310684032'"))
    # print(MysqlDt.exec_db("DELETE FROM BLUESKY_BASIC_USERINFO WHERE username='小红'"))

