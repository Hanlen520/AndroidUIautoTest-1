#coding=utf-8
from appium import webdriver
import os,time,unittest,random
from selenium.webdriver.common.by import By
from Common import BasePage
from Common.Public import Operation



class DownloadPage(BasePage.Base):

    '''页面元素属性'''
    select_all = (By.ID, 'com.ks.kaishustory:id/batch_download_iv_all_select')
    download_single_icons = (By.ID,'com.ks.kaishustory:id/iv_select_state')
    download_icon = (By.ID,'com.ks.kaishustory:id/batch_download_down_v')



    '''页面元素属性'''

    def download_select_all(self):
        self.find_element(*self.select_all).click()
        return self.find_element(*self.download_icon).click()


    def download_select_random(self):
        po = Operation(self.driver)
        # n = random.randint(1,2)
        k = random.randint(100,1000)
        po.swipeUp(k)
        print('随机点击下载按钮')
        List = self.find_elements(*self.download_single_icons)
        # print('List',List)
        x = random.randint(0,len(List)-1)

        List[x].click()

        downloadsign = self.find_element(*self.download_icon)
        print('判断选择的记录是否被下载过')
        if downloadsign == "true":
            self.find_element(*self.download_icon).click()
            return print('下载成功！')
        else:
            print('该内容已经被下载过！')