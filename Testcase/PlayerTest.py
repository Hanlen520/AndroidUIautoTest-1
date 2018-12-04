#coding:utf-8

import sys

from Common import MyTest
from Common import ReadData
from Common.Public import Operation
from PO.PlayerPage import PlayerPage


class PlayerTest(MyTest.MyTest):

    # @unittest.skip(u'强制跳过')
    def test_Aplay(self):
        '''进入播放器--点击播放-前进-后退-循环方式'''
        try:
            po = PlayerPage(self.driver)
            po.common_play()
            print('操作成功')
        except:
            po = Operation(self.driver)
            po.screenShot()


    def test_Aplay_(self):
        '''进入播放器--点击收藏'''
        try:
            po = PlayerPage(self.driver)
            po.palyer_collect()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()


    def test_Aplay(self):
        '''进入播放器--点击下载'''
        try:
            po = PlayerPage(self.driver)
            po.player_download()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()



    # @unittest.skip(u'强制跳过')
    def test_Bplay_timing(self):
        '''播放器--调整定时策略-挨个切换定时选项'''
        try:
            po = PlayerPage(self.driver)
            po.go_play()
            po.clicktiming()
            po.clicknoopen()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()

    # @unittest.skip(u'强制跳过')
    def test_Cplay_leavemessage(self):
        '''播放器--点击留言，输入留言内容'''
        try:
            po = PlayerPage(self.driver)
            po.go_play()
            fo = Operation(self.driver)
            fo.swipeUp()
            mname = format(sys._getframe().f_code.co_name)
            data = ReadData.readdata(mname)
            print(data[0])
            po.click_leave_message(data[0])
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()

    # @unittest.skip(u'强制跳过')
    def test_Egivegood(self):
        '''播放器--浏览区--随机点赞'''
        try:
            po = PlayerPage(self.driver)
            po.go_play()
            fo = Operation(self.driver)
            fo.swipeUp()
            po.givegood()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()

    # @unittest.skip(u'强制跳过')
    def test_Fclick_play_method(self):
        '''播放器--循环切换播放方式'''
        try:
            po = PlayerPage(self.driver)
            po.click_play_method()
            print('操作成功！')

        except:
            po = Operation(self.driver)
            po.screenShot()


















