#coding:utf-8

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os,time
from Common import MyTest,Public
from Common import Driver



'''定义基类，统一用例配置'''


class Base(Driver.Driver):
    # print('--Base')
    driver = None

    def __init__(self,appium_driver):
        # print('--Base-__init')
        self.driver = appium_driver


    '''重写定位方法，提高自动化体验'''
    def find_element(self,*loc):
        # print(u'元素的定位属性为：',*loc)
        try:
            po = Public.Operation(self.driver)
            if po.Element(*loc):
                WebDriverWait(self.driver,5).until(lambda driver:driver.find_element(*loc))
                print('操作成功')
                return self.driver.find_element(*loc)
            else:
                raise LocateError
        except Exception as e:
            print(u"页面中找不到元素", loc)
            raise LocateError()

    def find_elements(self,*loc):
        # print(u'元素的定位属性为：',*loc)
        try:
            po = Public.Operation(self.driver)
            if po.Element(*loc):
                WebDriverWait(self.driver,5).until(lambda driver:driver.find_elements(*loc))
                print('操作成功')
                return self.driver.find_elements(*loc)
            else:
                raise LocateError
        except Exception:
            print(u"页面中找不到元素",loc)
            raise LocateError()

    # def page_source(self):
    #     print(self.page_source)
    #     return self.driver.page_source

    def back(self):
        # print(u'运行back')
        return self.keyevent(4)



class LocateError(Exception):
    pass
