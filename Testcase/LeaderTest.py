#coding:utf-8

from appium import webdriver
import os,time,unittest,sys,shutil
from Common import MyTest,Public
from Common.BasePage import LocateError
from Common.Public import Operation
from PO.HomePage import HomePage
from PO.LeaderPage import LeaderPage
from Common import ReadData


class LeaderTest(MyTest.MyTest):


    def test_Ahot_play_download_select_all(self):
        '''首页--热播榜--随机下载'''
        try:
            ho = HomePage(self.driver)
            ho.leaderboard()
            lo = LeaderPage(self.driver)
            lo.hot_play_download_random_select()
            print('操作成功')

        except:
            po = Operation(self.driver)
            po.screenShot()



    def test_Bvip_play_all(self):
        '''首页--小知识--vip榜--播放全部'''
        try:
            ho = HomePage(self.driver)
            ho.leaderboard()
            lo = LeaderPage(self.driver)
            lo.vip_play_all()

        except:
            po = Operation(self.driver)
            po.screenShot()