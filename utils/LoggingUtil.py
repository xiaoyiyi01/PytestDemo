import logging,os,time

# 定义日志存放路径
base_path=os.path.abspath(__file__)
proj_path=os.path.dirname(os.path.dirname(base_path))
log_path=proj_path+os.sep+"logs"

if not os.path.exists(log_path):
    os.mkdir(log_path)

# 封装logger
class Logger:

    def __init__(self):
        # 设置日志文件名输出格式
        self.logname ="{}.log".format(time.strftime("%Y%m%d%H%M"))
        # 设置日志文件输出等级
        self.logger = logging.getLogger("log")

        self.logger.setLevel(logging.DEBUG)

    #     设置日志输出格式
        self.formater=logging.Formatter(
            " [%(asctime)s][%(filename)s %(lineno)d][ %(levelname)s] %(message)s")

        # 编入日志文件（encoding='utf-8'防止日志出现乱码）
        # FileHandler是指定日志文件处理的方法，
        # 指定输出文件(包含文件的路径，如果不指定文件的绝对路径则表示在当前目录)，
        # 指定日志文件处理模式(追加a, 覆盖....)
        # 指定日志文件的编码格式(utf-8)
        self.filelogger = logging.FileHandler(os.path.join(log_path, self.logname),mode="a",encoding='utf-8')
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        # 输出控制台
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.console.setFormatter(self.formater)
        # 添加handler
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

log=Logger().logger

if __name__ == '__main__':
    log.info("测试开始...")
    log.debug("...测试结束")
