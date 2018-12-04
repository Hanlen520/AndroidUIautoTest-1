#coding=utf-8
from appium import webdriver
import os,time,unittest,random
from selenium.webdriver.common.by import By
from Common import BasePage
from Common.Public import Operation
from PO.HomePage import HomePage
from PO.DownloadPage import DownloadPage


class LeaderPage(BasePage.Base):

    '''首页--排行榜--页面属性'''
    hot_or_vip = (By.CLASS_NAME,'android.support.v7.app.ActionBar$Tab')
    play_all = (By.ID,'com.ks.kaishustory:id/tv_play_status')
    names = (By.ID,'com.ks.kaishustory:id/seed_name')
    downloads = (By.ID,'com.ks.kaishustory:id/iv_state')
    share = (By.ID,'com.ks.kaishustory:id/view_share')
    go_select_all = (By.ID,'com.ks.kaishustory:id/iv_download')


    '''首页--排行榜--热播榜页面封装方法'''


    def hot_play_all(self):
        '''点击播放全部'''
        ho = HomePage(self.driver)
        ho.leaderboard()
        self.find_element(*self.play_all).click()


    def hot_play_random(self):
        '''随机点击播放'''
        ho = HomePage(self.driver)
        ho.leaderboard()
        List = self.find_elements(*self.names)
        x = random.randint(0, len(List) - 1)
        List[x].click()


    def hot_play_download_single(self):
        '''随机点击下载'''
        ho = HomePage(self.driver)
        ho.leaderboard()
        List = self.find_elements(*self.downloads)
        x = random.randint(0,len(List)-1)
        List[x].click()


    def hot_play_download_select_all(self):
        '''全选--勾选全部--下载'''
        ho = HomePage(self.driver)
        ho.leader_board()
        a = self.find_element(*self.go_select_all).click()
        do = DownloadPage(self.driver)
        do.download_select_all()




    '''首页--排行榜--vip榜页面封装方法'''

    def vip_play_all(self):
        '''点击播放全部'''

        print('点击进入精品榜')
        List = self.find_elements(*self.hot_or_vip)
        List[1].click()
        print('点击播放全部')
        self.find_element(*self.play_all).click()
        print('播放成功')



    def hot_play_random(self):
        '''随机点击播放'''
        ho = HomePage(self.driver)
        ho.leaderboard()
        List = self.find_elements(*self.names)
        x = random.randint(0, len(List) - 1)
        List[x].click()


    def hot_play_download_single(self):
        '''随机点击下载'''
        ho = HomePage(self.driver)
        ho.leaderboard()
        List = self.find_elements(*self.downloads)
        x = random.randint(0,len(List)-1)
        List[x].click()


    def hot_play_download_select_all(self):
        '''全选--勾选全部--下载'''
        ho = HomePage(self.driver)
        ho.leaderboard()
        self.find_element(*self.go_select_all).click()
        do = DownloadPage(self.driver)
        do.download_select_all()

    def hot_play_download_random_select(self):
        '''全选--随机勾选--下载'''
        print('点击全部下载的按钮')
        self.driver.find_element(*self.go_select_all).click()
        do = DownloadPage(self.driver)
        do.download_select_random()