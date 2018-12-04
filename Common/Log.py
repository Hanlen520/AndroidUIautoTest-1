import logging
from datetime import datetime
import threading
from Common import  readConfig
import os


class Log(object):
    def __init__(self):
        global logPath,resultPath,proDir
        proDir = readConfig.parDir
        #存放日志的目录
        resultPath = os.path.join(proDir,"result")
        print('结果目录',resultPath)
        #如果没有改目录，则创建
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)

        #拼接日志目录
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # 如果没有改目录，则创建
        if not os.path.exists(logPath):
            os.mkdir(logPath)


        #日志参考：https://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html
        #定义日志
        self.logger = logging.getLogger()
        #定义日志级别
        self.logger.setLevel(logging.INFO)

        #定义handler，来写入文件
        handler = logging.FileHandler(os.path.join(logPath,'output.log'))
        #定义日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #设置格式
        handler.setFormatter(formatter)
        #添加handler来处理日志
        self.logger.addHandler(handler)


class MyLog(object):
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        print(MyLog)
        if MyLog is not None:
            print('if')
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log

    @staticmethod
    def get_result_path():
        MyLog.log = Log()
        return MyLog.log.resultPath




if __name__ == "__main__":
    p = MyLog()
    p.get_log()
    p.get_result_path()