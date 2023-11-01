from utils.LoggingUtil import log


class AssertResult:

    def __init__(self):
        self.log=log
    # 设置状态断言
    def Assert_Status(self,code,expected_code):
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            self.log.error("code错误,code是{},期望code是{}".format(code, expected_code))
            raise

    # 设置body包含某内容断言
    def Assert_inbody(self,body,expected_body):
        try:
            assert expected_body in body
            return True
        except:
            self.log.error(f"body数据有误，返回body是{body}，期望body是{expected_body}")

    # 设置body的json值断言
    def Assert_json(self,data,expected_data):
        try:
            assert expected_data ==data
            return True
        except:
            self.log.error(f"json数据有误，返回data是{data},期望data是{expected_data}")

AssRes=AssertResult()