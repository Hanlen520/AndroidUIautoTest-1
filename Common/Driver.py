#coding:utf-8
#__author__ = 'lc'


from appium import webdriver
import os,time


#启动浏览器驱动
class Driver(object):

    def Android(self):
        '''定义启动driver的配置（根据手机来决定）'''


        # print('-Android')
        PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '7.1.1'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Android Emulator'
        # desired_caps['app'] = 'http://tcdn.kaishustory.com/kstory/app/kaishustory4.5.apk'
        desired_caps['appPackage'] = 'com.ks.kaishustory'
        desired_caps['appActivity'] = 'com.ks.kaishustory.pages.firstenter.FirstActivity'
        desired_caps['noReset'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['fullReset'] = False

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # self.driver = webdriver.Remote('http://10.0.4.120:4724/wd/hub', desired_caps)

        return self.driver

#用于测试该脚本是否有效
if __name__ == '__main__':
    dr = Driver()
    dr.Android()



