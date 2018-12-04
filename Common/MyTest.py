#coding:utf-8
import unittest,os,time
from Common import Driver
from appium import webdriver

'''定制appium_driver，继承unittest'''

class MyTest(unittest.TestCase):
    '''1、全部用例执行之前启动driver
       2、
    '''

    @classmethod
    def setUpClass(self):
        print('setUpClass,Prepare for all testcase')
        self.driver = Driver.Driver.Android(self)


    def setUp(self):
        print('用例环境准备完毕，开始执行')
        #启动appium_driver
        self.driver.launch_app()


    def tearDown(self):
        print('用例执行完毕，清理环境')
        self.driver.close_app()


    @classmethod
    def tearDownClass(self):
        print('tearDownClass,Prepare for all testcase')
        self.driver.quit()
