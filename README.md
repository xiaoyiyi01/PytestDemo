# PytestDemo
python+pytest+allure
首先是对request,yaml,mysql,logging,asssert,excel的封装，其次使用yaml/excel读取数据进行request请求，	 再次断言/连接mysql数据库进行断言，并使用logging打印日志相关数据，最后输出allure报告。
请求时候，使用confitest.py文件使用fixture设置请求前、后置，使用parametrize进行参数化。
输出报告时，使用epic设置项目名称，feature设置模块名称，title设置用例标题，severity设置用例严重程度。
