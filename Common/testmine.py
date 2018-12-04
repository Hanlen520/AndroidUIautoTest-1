import os,sys


# # class Fun():
# #     def __init__(self):
# #         self.a = 'a'
# #         print(self.a)
# #
# #
# #     def get_a(self):
# #         return self.a
# #
# # if __name__ == '__main__':
# #     p = Fun()
#
# '''
# # coding : uft-8
# __author__ = 'Phtih0n'
# import threading, time
# class MyThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         global n, lock
#         time.sleep(1)
#         if lock.acquire():
#             print(n , self.name)
#             n += 1
#             lock.release()
# if "__main__" == __name__:
#     n = 1
#     ThreadList = []
#     lock = threading.Lock()
#     for i in range(1, 200):
#         t = MyThread()
#         ThreadList.append(t)
#     for t in ThreadList:
#         t.start()
#     for t in ThreadList:
#         t.join()
# '''
#
# import threading
# import time
#
# counter = 0
# counter_lock = threading.Lock()  # 只是定义一个锁,并不是给资源加锁,你可以定义多个锁,像下两行代码,当你需要占用这个资源时，任何一个锁都可以锁这个资源
# counter_lock2 = threading.Lock()
# counter_lock3 = threading.Lock()
#
#
# # 可以使用上边三个锁的任何一个来锁定资源
#
# class MyThread(threading.Thread):  # 使用类定义thread，继承threading.Thread
#     def __init__(self, name):
#         threading.Thread.__init__(self)
#         self.name = "Thread-" + str(name)
#         #print(self.name)
#
#     def run(self):  # run函数必须实现
#         #print('ok')
#         global counter, lock  # 多线程是共享资源的，使用全局变量
#         time.sleep(1);
#
#         if lock.acquire():  # 当需要独占counter资源时，必须先锁定，这个锁可以是任意的一个锁，可以使用上边定义的3个锁中的任意一个
#             counter += 1
#             # print
#             # "I am %s, set counter:%s" % (self.name, counter)
#             print('%s这是counter%s'% (counter,self.name))
#             lock.release()  # 使用完counter资源必须要将这个锁打开，让其他线程使用
#
#
# if __name__ == "__main__":
#     lock = threading.Lock()
#     for i in range(1, 101):
#
#         my_thread = MyThread(i)
#         my_thread.start()
#
# class A():
#     print('out A')
#     def __init__(self):
#         print('A')
# class B(A):
#     def PP(self):
#         print('B')
# p = B()
#

from selenium import webdriver
import os



# chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver=webdriver.Chrome(chromedriver)
#
# driver.get("http://www.baidu.com")
# cookies = driver.get_cookies()
#
# print(cookies)
# for cookie in cookies:
#     cookie[cookie['name']]=cookie['value']
# print(cookie)
#
# driver.quit()


#
# #把字符串'123.456'转换成浮点数123.456：
# from functools import reduce
#
# def fun(x,y):
#     return x*10 +y
#
#
#
#
#
# def xiao(L):
#     L = L.split('.')
#     if len(L)==1:
#         return reduce(fun,map(int,L[0]))
#     else:
#         return reduce(fun,map(int,L[0]+L[1]))/pow(10,len(L[1]))
#
#
# print(xiao('0.123'))
#
#
# #----------------------------------------------
#
# def fun(x,y):
#     return x*10+y
#
# L = [1,2,3]
# for i in L:
#
#     fun(L[],L[j+1])

# #集合之间的操作+-&|
# dreamers = {'ljl','wc','xy','zb','lsy'}
# girls = {'mmf','lsy','syj'}
# result = dreamers.difference(girls)# result = a + b
# print(result)
#
# print(dreamers-girls)



#2018年8月23日15:01:29--获取类名和方法名
# #
# import sys
#
# #
# class Hello():
#
#     def hello(self):
#         print('the name of method is ## {} ##'.format(sys._getframe().f_code.co_name))
#         print('the name of class is ## {} ##'.format(self.__class__.__name__))
#
#
# if __name__ == "__main__":
#     h = Hello()
#     h.hello()
#
# #2018年8月23日15:10:31--os的操作方法
#
# print(help(os))

#2018年8月28日
#
# import random
# L = [1,2,3]
# print(L.index(1))
# print(len(L))
# while(True):
#     x = random.randint(0, len(L)-1)
#     if x >2:
#         print('fuck')

#Python和adb交互

import os,sys


# os.system('adb version')

import time

# filepath = 'C:\\return.html'
#
# result = os.path.getctime(filepath)
# print(time.ctime(result))
#
# result = os.path.getmtime(filepath)
# print(time.ctime(result))

import os

# print(os.listdir('c:'))

# os.system('adb shell dumpsys battery |grep status')
# result = os.popen('adb shell dumpsys battery |grep status').read()
# print(result)
# L = result.split(':')
# for i in L:
#     print(len(i),i)

# path = 'D:\gitlab\KaiShuUIautomation\kaishu\Report'
# result = os.path.getctime(path)
# print(result)

#
# # ls=['c.txt','b.txt','d.txt','a.txt']
# #
# # ls.sort(key=lambda lists:lists[0])
# #
# # print(ls)
# # lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
#
#
#
# #coding=utf-8
#
# '''
# Created on 2017/12/24 0024
# @author:Changge
# '''
#
# from appium import webdriver
# import time
# import threading
#
# desired_caps = {
#     'platformName':'Android',
#     'deviceName':'127.0.0.1:62025',
#     'platformVersion':'5.1.1',
#     'appPackage':'com.taobao.taobao',
#     'appActivity':'com.taobao.tao.welcome.Welcome',
# }
#
# desired_caps2 = {
#     'platformName':'Android',
#     'deviceName':'127.0.0.1:62001',
#     'platformVersion':'4.4.2',
#     'appPackage':'com.taobao.taobao',
#     'appActivity':'com.taobao.tao.welcome.Welcome',
# }
# def task1():
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#     ##休眠20s等待页面加载完成
#     time.sleep(20)
#     print(driver.contexts)
#     driver.quit()
#
# def task2():
#     driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps2)
#     ##休眠20s等待页面加载完成
#     time.sleep(20)
#     print(driver.contexts)
#     driver.quit()
#
# threads = []
# t1 = threading.Thread(target=task1)
# threads.append(t1)
#
# t2 = threading.Thread(target=task2)
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.start()



# for i in len('900'):
#     print(i)


#
# print('---------start')
# try:
#     raise NameError('未定位到元素')
# except Exception as e:
#     print('msg',e)

# import os
# path='https://tcdn.kaishustory.com/kstory/app/a.txt'
#
# data = os.path.basename(path)
# name = os.path.splitext(path)
# print('name',name)
# print(data)

#
# ftp_param = {
#     'host': '172.16.1.191',
#     'port': 21,
#     'user': 'ftpuser',
#     'pwd': 'ftpuser2099',
#     'points_dir': 'comm/cust_point/',
#     'xsl': 'xsl/dps'
# }

from ftplib import FTP

#实例化变量ftp
ftp = FTP()
#打开调试级别2，显示详细信息
# ftp.set_debuglevel(2)
#连接目标机器IP和端口
ftp.connect("172.16.1.191",21)
#登录用户名和密码
ftp.login("ftpuser","ftpuser2099")

#打印ftp登录成功后的欢迎提示语
print(ftp.getwelcome())
#执行dir命令
ftp.dir()

ftp.pwd()
#设置的缓冲区大小
bufsize=1024
#上传目标文件位置
localfile="D:\\code\\AndroidUIAutotest\\kaishu\\Result\\UIautotest-Report.zip"
#定义上传变量
fd=open(localfile,'rb')
#设置主动模式
ftp.set_pasv(1)
#上传目标文件
ftp.storbinary('STOR %s ' % os.path.basename(localfile),fd)
#关闭连接
fd.close()
#退出ftp
ftp.quit()
ftp.dir()
#跳转到目标路径
ftp.cwd("/data/javasoft/tomcat/apache-tomcat-7.0.73/webapps/")
ftp.dir()


