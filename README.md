# PytestDemo
python+pytest+allure
首先是对request,yaml,mysql,logging,asssert,excel的封装，其次使用yaml/excel读取数据进行request请求，	 再次断言/连接mysql数据库进行断言，并使用logging打印日志相关数据，最后输出allure报告。
请求时候，使用confitest.py文件使用fixture设置请求前、后置，使用parametrize进行参数化。
输出报告时，使用epic设置项目名称，feature设置模块名称，title设置用例标题，severity设置用例严重程度。
框架结构：
common：获取token值
config:配置文件-数据库和url配置
log:日志文本输出
data:测试数据管理（yaml/excel）
report:allure报告输出
testcase：测试用例(单个接口，场景测试)
untils:工具封装（request,yaml,mysql,logging,asssert,excel）
