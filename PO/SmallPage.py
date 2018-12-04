#coding=utf-8
from appium import webdriver
import os,time,unittest,random
from selenium.webdriver.common.by import By
from Common import BasePage
from Common.Public import Operation
from Common.BasePage import LocateError





class SmallPage(BasePage.Base):

    '''首页--小知识页面属性'''
    knowledge_list = (By.ID,'com.ks.kaishustory:id/seed_name')
    list_sort = (By.ID, 'com.ks.kaishustory:id/iv_sort')

    download_icon = (By.ID,'com.ks.kaishustory:id/iv_state')

    knowledge_cards_close = (By.ID,'com.ks.kaishustory:id/simple_close')
    share_wechat_circle = (By.ID,'com.ks.kaishustory:id/simple_iconcircle')
    share_wechat =(By.ID,'com.ks.kaishustory:id/simple_iconwx')
    knowledge_cards_download = (By.ID, 'com.ks.kaishustory:id/simple_icondownload')

    #知识卡
    knowledge_cards = (By.ID, 'com.ks.kaishustory:id/iv_header')

    #今日文字
    today_text = (By.ID,'com.ks.kaishustory:id/tv_header')


    #播放界面
    play_time = (By.ID,'com.ks.kaishustory:id/tv_currenttime')

    #订阅
    subscribe = (By.ID,'com.ks.kaishustory:id/tv_dingyue')
    subscribe_yes = (By.ID,'com.ks.kaishustory:id/btn_n')
    subscribe_nocancel = (By.ID, 'com.ks.kaishustory:id/btn_p')

    share_icon = (By.ID,'com.ks.kaishustory:id/view_share_pro_detail')

    '''首页--小知识页面封装方法'''
    def random_play(self):
        '''首页---小知识--随机播放'''
        fo = Operation(self.driver)
        fo.swipeUp()
        print('随机选择一条记录收听')
        List = self.find_elements(*self.knowledge_list)
        x = random.randint(0,len(List)-1)
        List[x].click()
        time.sleep(3)
        print('等待3s，获取播放时间')
        playtime = self.find_element(*self.play_time).text
        print('判断是否播放成功')
        if time != '00:00':
            print('播放成功！')
        else:
            print('播放失败！')
            raise LocateError


    def Subscribe_ok(self):
        if self.Subscribe_or_not() == 0:
            print('点击订阅')
            self.find_element(*self.subscribe).click()
            time.sleep(2)
            print('获取页面文字')
            text = self.find_element(*self.subscribe).text
            print('判断是否订阅成功？')
            if text == '已订阅':
                print('订阅成功！')
            else:
                print('订阅失败！')
                raise LocateError
        else:
            print('不能重复订阅')
            raise LocateError


    def Subscribe_cancel(self):
        if self.Subscribe_or_not() == 1:
            print('点击已订阅按钮，来取消订阅')
            self.find_element(*self.subscribe).click()
            time.sleep(2)
            print('提示是否取消，点击“是”')
            self.find_element(*self.subscribe_yes).click()
            print('获取页面文字')
            text = self.find_element(*self.subscribe).text
            print('判断是否订阅成功？')
            if text == '订阅':
                print('取消订阅成功！')
            else:
                print('取消订阅失败！')
                raise LocateError
        else:
            print('该用户还未订阅，不能取消订阅')
            raise LocateError

    def Subscribe_noCancel(self):
        if self.Subscribe_or_not() == 1:
            print('点击已订阅按钮，来取消订阅')
            self.find_element(*self.subscribe).click()
            time.sleep(2)
            print('提示是否取消，点击“先不取消”')
            self.find_element(*self.subscribe_nocancel).click()
            print('获取页面文字')
            text = self.find_element(*self.subscribe).text
            print('判断是否取消订阅成功？')
            if text == '已订阅':
                print('暂不取消订阅成功')
            else:
                print('暂不取消订阅失败！')
                raise LocateError
        else:
            print('该用户还未订阅，不能取消订阅')
            raise LocateError

    def Subscribe_or_not(self):
        time.sleep(2)
        print('获取页面文字')
        text = self.find_element(*self.subscribe).text
        print('判断用户是否已经订阅？')
        if text == '已订阅':
            print('该用户已订阅！')
            return 1
        elif text == '订阅':
            print('该用户未订阅！')
            return 0


    def Knowledge_list_sort(self):
        time.sleep(2)
        print('点击排序按钮，进行排序')
        List = self.find_elements(*self.list_sort)
        List[0].click()
        time.sleep(2)
        print('判断排序是否成功')
        text = self.find_element(*self.today_text).text
        if text != '今日':
            print('排序成功!')
        else:
            print('排序失败！')
            raise LocateError


