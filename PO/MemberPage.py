#coding=utf-8
from appium import webdriver
import os,time,unittest,random
from selenium.webdriver.common.by import By
from Common import BasePage
from Common.Public import Operation
from PO.HomePage import HomePage



class MemberPage(BasePage.Base):


    '''会员中心页面属性'''
    names = (By.ID,'com.ks.kaishustory:id/seed_name')
    prices = (By.ID,'com.ks.kaishustory:id/bt_buy')
    free_listen = (By.ID,'com.ks.kaishustory:id/vip_detail_listend_tv')
    now_buy = (By.ID,'com.ks.kaishustory:id/vip_detail_left_buystate_tv')
    like_icon = (By.ID,'com.ks.kaishustory:id/vip_detail_left_buystate_tv')
    confirm_buy = (By.ID,'com.ks.kaishustory:id/view_confirm')
    close = (By.ID,'com.ks.kaishustory:id/view_close_sheet')
    detail = (By.ID,'com.ks.kaishustory:id/tv_member_card_details')



    '''会员中心页面封装方法'''
    #查看会员详情
    def Mc_detail(self):
        fo = HomePage(self.driver)
        fo.MemberCenter()
        print('点击查看详细信息')
        self.find_element(*self.detail).click()
        time.sleep(2)
        print('查看成功！')



    def Mc_swip(self):
        ho = HomePage(self.driver)
        ho.MemberCenter()
        po = Operation(self.driver)
        po.swipeUp()
