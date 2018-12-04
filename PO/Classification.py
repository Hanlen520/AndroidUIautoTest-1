#coding=utf-8
from appium import webdriver
import os,time,unittest,random
from selenium.webdriver.common.by import By
from Common import BasePage
from Common.Public import Operation
from PO.HomePage import HomePage



class ClassificationPage(BasePage.Base):


    '''分类页面属性'''
    icons = (By.CLASS_NAME,'android.widget.TextView')
    albums = (By.ID,'com.ks.kaishustory:id/linearLayout_middle')
    look_more = (By.ID,'com.ks.kaishustory:id/bt_lookmore')



    '''分类页面封装方法'''

    def Cl_random_listen(self):
        fo = HomePage(self.driver)
        fo.Classification()
        i = 1
        while i<5:
            Icon_List = self.find_elements(*self.icons)
            x = random.randint(0,len(Icon_List)-1)
            x.lick()
            '''随机选择故事/专辑'''
            album_list = self.find_elements(*self.albums)
            y = random.randint(0,len(album_list)-1)
            y.click()
            i = i + 1


