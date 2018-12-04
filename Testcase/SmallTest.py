#coding:utf-8

from appium import webdriver
import os,time,unittest,sys,shutil
from Common import MyTest,Public
from Common.BasePage import LocateError
from Common.Public import Operation
from PO.HomePage import HomePage
from PO.SmallPage import SmallPage
from Common import ReadData


class SmallTest(MyTest.MyTest):

    # @unittest.skip(u'强制跳过')
    def test_Arangdom_play(self):
        '''首页--小知识--随机播放'''
        try:
            ho = HomePage(self.driver)
            ho.small_knowlege()
            so = SmallPage(self.driver)
            so.random_play()
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError()

    # @unittest.skip(u'强制跳过')
    def test_BSubscribe_ok(self):
        '''首页--小知识--订阅成功'''
        try:
            ho = HomePage(self.driver)
            ho.small_knowlege()
            so = SmallPage(self.driver)
            so.Subscribe_ok()
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError()


    # @unittest.skip(u'强制跳过')
    def test_CSubscribe_noCancel(self):
        '''首页--小知识--暂不取消订阅'''
        try:
            ho = HomePage(self.driver)
            ho.small_knowlege()
            so = SmallPage(self.driver)
            so.Subscribe_noCancel()
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError()


    # @unittest.skip(u'强制跳过')
    def test_DSubscribe_cancel(self):
        '''首页--小知识--取消订阅'''
        try:
            ho = HomePage(self.driver)
            ho.small_knowlege()
            so = SmallPage(self.driver)
            so.Subscribe_cancel()
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError()

    # @unittest.skip(u'强制跳过')
    def test_EKnowledge_list_sort(self):
        '''首页--小知识--排序'''
        try:
            ho = HomePage(self.driver)
            ho.small_knowlege()
            so = SmallPage(self.driver)
            so.Knowledge_list_sort()
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError()