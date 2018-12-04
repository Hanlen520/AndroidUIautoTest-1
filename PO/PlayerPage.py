#coding=utf-8
from appium import webdriver
import os,time,unittest,random

from selenium.webdriver.common.by import By
from Common import BasePage
from Common.Public import Operation



class PlayerPage(BasePage.Base):

    '''播放器页面属性'''

    playericon = (By.ID,'com.ks.kaishustory:id/icon_playing')
    playmethod = (By.ID,'com.ks.kaishustory:id/iv_play_mode_status')
    backicon = (By.ID,'com.ks.kaishustory:id/play_pre')
    forwardicon = (By.ID,'com.ks.kaishustory:id/play_next')
    playicon  = (By.ID,'com.ks.kaishustory:id/play_control')
    list = (By.ID,'com.ks.kaishustory:id/play_mid_to_list_iv')
    collection = (By.ID,'com.ks.kaishustory:id/circle')
    download = (By.ID,'com.ks.kaishustory:id/view_download')
    timing = (By.ID, 'com.ks.kaishustory:id/sdv_set_close_time')#文稿
    paper = (By.ID, 'com.ks.kaishustory:id/view_ducument_image')
    share = (By.ID, 'com.ks.kaishustory:id/view_share')
    reback = (By.ID, 'com.ks.kaishustory:id/iv_back')
    noopen = (By.ID, 'com.ks.kaishustory:id/tv_no_open')
    timing_now = (By.ID, 'com.ks.kaishustory:id/tv_play_over_now')
    timing_fifteen = (By.ID, 'com.ks.kaishustory:id/relativeLayout_15')
    timing_thirty = (By.ID, 'com.ks.kaishustory:id/tv_30')
    timing_sixty = (By.ID, 'com.ks.kaishustory:id/tv_60')
    timing_ninty = (By.ID, 'com.ks.kaishustory:id/tv_90')
    timing_now_after = (By.ID, 'com.ks.kaishustory:id/tv_sleep')
    timing_cancel = (By.ID, 'com.ks.kaishustory:id/tv_close')
    goodicons = (By.ID, 'com.ks.kaishustory:id/item_commment_zan_icon')
    leave_message = (By.ID, 'com.ks.kaishustory:id/playing_comment_view')
    goalbum = (By.ID,'com.ks.kaishustory:id/rl_story_player_album_info')
    comment = (By.ID,'com.ks.kaishustory:id/item_comment_content_tv')
    replymessage = (By.ID,'com.ks.kaishustory:id/comment_list_root_layout')
    writemessage = (By.ID,'com.ks.kaishustory:id/editview')
    sendmessage = (By.ID,'com.ks.kaishustory:id/comment_send_tv')
    commenticons = (By.ID,'com.ks.kaishustory:id/item_commment_comment_icon')


    play_name = (By.ID,'com.ks.kaishustory:id/playname_view')




    '''首页--我的页面封装方法'''

    def clickdot(self,x,y,duration=100):
        '''x,y是点击屏幕上的点'''
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        x1 = int((float(x)/width)*width)
        y1 = int((float(y)/height)*height)
        self.driver.tap([(x1,y1),(x1,y1)],duration)

    def go_play(self):
        '''进去播放页面'''
        time.sleep(2)
        print('点击播放器，进入播放器页面')
        self.find_element(*self.play_name).click()
        time.sleep(5)

    def clickplay(self):
        print('点击播放按钮')
        return self.driver.find_element(*self.playicon).click()

    def clickback(self):
        print('点击返回')
        return self.driver.find_element(*self.backicon).click()

    def clickforward(self):
        print('点击下一个')
        return self.driver.find_element(*self.forwardicon).click()

    '''点击播放模式'''
    def clickmethod(self):
        print('点击播放模式，进行切换')
        return self.driver.find_element(*self.playmethod).click()
    '''点击选择列表'''
    def cilckchoicelist(self):
        print('点击选择列表')
        return self.driver.find_element(*self.list).click()

    '''点击收藏'''
    # def clickcollection(self):
    #     return self.driver.find_element(*self.collection).click()

    def clickcollection(self):
        try:
            print('点击收藏')
            return self.driver.find_element(*self.collection).click()
            print('收藏成功')
        except:
            return print('此故事已被收藏过')

    '''点击文稿'''
    def clickpaper(self):
        print('点击文稿')
        return self.driver.find_element(*self.paper).click()

    '''点击分享'''
    def clickshare(self):
        print('点击分享')
        return self.driver.find_element(*self.share).click()
    '''点击下载'''
    def clickdownload(self):
        try:
            print('点击下载')
            return self.driver.find_element(*self.download).click()
            print('下载成功')
        except:
            return print('此故事已经被下载过！')

    '''集中封装定时操作，挨个点击定时选项，最后点击取消'''
    def clicktiming(self):
        L = [self.timing_now,self.timing_fifteen,self.timing_thirty,self.timing_sixty,self.timing_ninty]
        for i in L:
            # print(i)
            print('点击定时方式')
            self.driver.find_element(*self.timing).click()
            time.sleep(2)
            print('选择一种定时方式',i)
            self.driver.find_element(*(i)).click()
        self.driver.find_element(*self.timing).click()
        print('点击取消定时')
        return self.driver.find_element(*self.timing_cancel).click()

    '''点击定时--不开启'''
    def clicknoopen(self):
        print('点击不开启定时')
        self.driver.find_element(*self.timing).click()
        return self.driver.find_element(*self.noopen).click()

    '''点击专辑'''
    def clickalbum(self):
        return self.driver.find_element(*self.goalbum).click()

    '''点击写留言，输入留言内容，点击发送'''
    def click_leave_message(self,text):
        print('点击留言按钮')
        self.driver.find_element(*self.leave_message).click()
        print('输入留言内容',text)
        self.driver.find_element(*self.writemessage).send_keys(text)
        print('点击发送留言')
        self.driver.find_element(*self.sendmessage).click()
        print('留言成功')

    '''随意点击评论图标，输入内容，点击发送'''
    def cilckrandomcommenticon(self,text):
        L = self.driver.find_elements(*self.commenticons)
        L.send_keys(text)
        return self.driver.find_element(*self.sendmessage).click()

    '''随机点赞某一条评论'''
    def givegood(self):
        print('随机找一条评论，进行点赞')
        L = self.driver.find_elements(*self.goodicons)
        x = random.randint(0,len(L)-1)
        L[x].click()
        print('点赞成功')

    '''点击文稿'''
    def clickpaper(self):
        return self.driver.find_element(*self.paper).click()


    '''点击播放器常用操作'''
    def common_play(self):
        self.go_play()
        self.clickplay()
        time.sleep(1)
        self.clickforward()
        time.sleep(1)
        self.clickback()
        time.sleep(2)

    def palyer_collect(self):
        self.go_play()
        self.clickcollection()
        time.sleep(1)
        self.clickpaper()
        po = Operation(self.driver)
        return po.swipeUp()

    def player_download(self):
        self.go_play()
        self.clickdownload()
        po = Operation(self.driver)
        return po.swipeUp()


    def click_play_method(self):
        self.go_play()
        self.clickmethod()
        time.sleep(1)
        self.clickmethod()
        time.sleep(1)
        self.clickmethod()











# if __name__ == '__main__':
#     p = PlayerPage()
#     p.clicktiming()



