#coding:utf-8

from appium import webdriver
import os,time,unittest,sys,shutil
from Common import MyTest,Public
from Common.BasePage import LocateError
from Common.Public import Operation
from PO.HomePage import HomePage
from PO.SmallPage import SmallPage
from Common import ReadData


class ATest(MyTest.MyTest):

    # @unittest.skip(u'强制跳过')
    def test_ALogin(self):
        '''首页--小知识--随机播放'''
        try:
            ho = HomePage(self.driver)
            ho.login_or_not()

        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')

