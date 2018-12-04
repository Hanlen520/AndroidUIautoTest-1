#coding:utf-8

import os, time,unittest
from Common.configEmail import MyEmail
from Common.FtpMethod import FtpMethod
import HTMLTestRunner
import shutil


# import HTMLTestRunnerCN
'''
    1、建立测试套件，获取用例脚本，组装测试套件
    2、创建报告实例，配置报告模板，执行用例，生成报告
'''

now_dir =os.path.dirname(os.path.abspath(__file__))
test_dir = now_dir + '\\'+'Testcase'
test_report = now_dir + '\\'+'Report'
test_result = now_dir + '\\' + 'Result'

print('test_casedir',test_dir)


def create_suite():
    '''获取用例脚本，组装测试套件'''
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='SmallTest.py')
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    print(testunit)
    return testunit

def clean_dir(goal_path):
    '''运行前清理以前生成的日志和报告'''
    ls = os.listdir(goal_path)
    for i in ls:
        file = os.path.join(goal_path,i)
        if os.path.isdir(file):
            clean_dir(file)
        else:
            os.remove(file)

def move_file(goal_dir):
    ls = os.listdir(goal_dir)
    for i in ls:
        file = os.path.join(goal_dir,i)
        if os.path.isdir(file):
            move_file(file)
        elif os.path.splitext(file)[1] == '.html':
            shutil.move(file,'C:\\apache-tomcat-7.0.90\\webapps\\uiautotest')
        elif os.path.splitext(file)[1] == '.png':
            shutil.move(file,'C:\\apache-tomcat-7.0.90\\webapps\\uiautotest\\images')


if __name__ == "__main__":
    #清理报告目录和结果目录
    clean_dir(test_result)
    clean_dir(test_report)
    # 1、创建测试容器；2、加载测试用例
    # 1、创建报告实例；2、配置报告内容、3、运行容器内的用例
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'
    print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description=u"运行环境Android")
    runner.run(create_suite())
    print('已经运行完discover')
    fp.close()
    mo = MyEmail()
    file = os.path.split(filename)[1]
    mo.send_email(file)
    move_file(test_report)
    fo = FtpMethod()
    fo.uploadFtpFile()

