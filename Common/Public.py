#coding:utf-8
import os
from Common import BasePage
from Common import readConfig
import time



class Operation(BasePage.Base):
# class Operation(object):

    '''1.2018年8月22日：封装滑动公共操作方法：上滑，下滑，左滑、右滑
       2.2018年8月23日：封装截图公共操作方法
    '''

    #参数：t--滑动时间
    def swipeUp(self,t=500):
        l = self.driver.get_window_size()
        print('上滑页面')
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.65
        y2 = l['height'] * 0.25
        # print(x1, y1, y2)
        time.sleep(1)
        return  self.driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self,t=500):
        l = self.driver.get_window_size()
        print('下滑页面')
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.25
        y2 = l['height'] * 0.75
        # print(x1,y1,y2)
        time.sleep(1)
        return  self.driver.swipe(x1, y1, x1, y2, t)

    def swipeRight(self,t=500):
        l = self.driver.get_window_size()
        print('右滑页面')
        x1 = l['width'] * 0.05
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        # print(x1, y1, x2)
        time.sleep(1)
        return  self.driver.swipe(x1, y1, x2, y1, t)

    def swipeLeft(self,t=500):
        l = self.driver.get_window_size()
        print('左滑页面')
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.05
        # print(x1, y1, x2)
        time.sleep(1)
        return  self.driver.swipe(x1, y1, x2, y1, t)



    def screenShot(self):

        po = readConfig.ReadConfig()
        sign = po.get_screen('switch')
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        file_name = timestrmap
        resultpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\Report\\images\\"
        # print('resultpath',resultpath)
        dir = resultpath + file_name+".png"
        if sign == 'on':
            self.driver.get_screenshot_as_file(dir)
            print('screenshot:', timestrmap, '.png')
            # print('This screenshot switch is on!')
            return 0
        else:
            # return print('This screenshot switch is off!')
            pass



    def clearText(self,text):
        print('清空上次登录痕迹')
        self.driver.press_keycode(123)
        # self.driver.pressKeyCode(123)
        # print(len(text))
        for i in range(0,len(text)):
            # print(i)
            self.driver.press_keycode(67)
        return 0;

    def goback(self):
        return self.driver.press_keycode(4)

    # def player(self):
    #     return self.driver.

    def adbSendText(self,text):
        adb1 = 'adb shell ime set com.sonyericsson.textinput.uxp/.glue.InputMethodServiceGlue'
        adb2 = 'adb shell input text %s' % text
        adb3 = 'adb shell ime set io.appium.android.ime/.UnicodeIME'
        # print(adb2)
        os.system(adb1)
        os.system(adb2)
        os.system(adb3)
        return 0;

    def clickDot(self,x,y):
        self.driver.tap([(x,y)])


    def Element(self,*args):
        # print('*args------',*args)
        # print('*arg1-------',args[1])
        # print('page_source-----',self.driver.page_source)
        source = self.driver.page_source
        if args[1] in source:
            # print('元素',args[1],'存在！')
            return True
        else:
            # print('元素', args[1], '不存在！')
            return False





# if __name__ == '__main__':
#     p = Operation()
#     # p.swipeUp(100)
#     p.clickDot()
