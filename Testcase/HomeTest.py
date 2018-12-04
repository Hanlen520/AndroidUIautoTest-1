#coding:utf-8


import time, sys
from Common import MyTest
from Common.Public import Operation
from PO.HomePage import HomePage
from PO.MinePage import MinePage
from Common import ReadData
from Common.BasePage import LocateError


class HomeTest(MyTest.MyTest):
    '''
    概要：编写以页面为单元的测试用例,，直接调用xxPage下封装好的属性和方法
    规则：必须以test开头
    '''


    def test_AHomeTest_Search(self):
        '''test001验证首页搜索功能'''
        try:
            po = HomePage(self.driver)
            print('打开app，进入首页')
            mname = format(sys._getframe().f_code.co_name)          #获取当前的类名和方法名
            data = ReadData.readdata(mname)
            po.searchText(data[0])
            po = Operation(self.driver)
            time.sleep(1)
            po.swipeUp(500)
        except:
            po = Operation(self.driver)
            po.screenShot()


    def test_Bclick_Bottomicon(self):
        '''test002：验证首页底部按钮切换功能'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            print('点击课程，进入课程页面')
            po.clickbottom(2)
            po = Operation(self.driver)
            time.sleep(1)
            po.swipeUp(500)
            print('查看成功')
        except:
            po = Operation(self.driver)
            po.screenShot()


    def test_Cclick_buyed_course(self):
        '''test003：验证首页点击已购买--课程页面'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            po.Click_buyed_course()
            print('查看成功')
        except:
            po = Operation(self.driver)
            po.screenShot()



    def test_Dclick_touch(self):
        '''test004：验证首页点击摸一摸'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            po.Click_touch()

        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError

    def test_Eclick_buyed_story(self):
        '''test005：验证首页点击已购买--故事页面'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            po.Click_buyed_story()
            print('查看成功')
        except:
            po = Operation(self.driver)
            po.screenShot()

    def test_Fclick_buyed_order(self):
        '''test006：验证首页点击已购买--订单页面'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            po.Click_buyed_order()
            print('查看成功')
        except:
            po = Operation(self.driver)
            po.screenShot()


    def test_Gclick_buyed_updatenotice(self):
        '''test007：验证首页点击已购买--更新提醒页面'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            po.Click_buyed_updatenotice()
            print('查看成功')
        except:
            po = Operation(self.driver)
            po.screenShot()


    def test_HClick_touch1(self):
        '''test008：验证首页摸一摸-点击星球1收听'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            po.Click_touch1()

        except:
            po = Operation(self.driver)
            po.screenShot()



    def test_HClick_touch2(self):
        '''test009：验证首页摸一摸-点击星球2收听'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            po.Click_touch2()

        except:
            po = Operation(self.driver)
            po.screenShot()


    def test_HClick_touch3(self):
        '''test010：验证首页摸一摸-点击星球3收听'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            po.Click_touch3()

        except:
            po = Operation(self.driver)
            po.screenShot()


    def test_HClick_touch4(self):
        '''test011：验证首页摸一摸-点击星球4收听'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            po.Click_touch4()

        except:
            po = Operation(self.driver)
            po.screenShot()



    def test_HClick_touch5(self):
        '''test012：验证首页摸一摸-点击星球5收听'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            po.Click_touch5()

        except:
            po = Operation(self.driver)
            po.screenShot()



    def test_HClick_touch6(self):
        '''test013：验证首页摸一摸-点击星球6收听'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            po.Click_touch6()

        except:
            po = Operation(self.driver)
            po.screenShot()

    def test_HClick_touch_close(self):
        '''test015：验证首页摸一摸-飞行-收听-关闭'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            po.Click_touch_again()

        except:
            po = Operation(self.driver)
            po.screenShot()




    def test_HClick_touch_back(self):
        '''test016：验证首页摸一摸-飞行-返回'''
        try:
            print('进入app首页')
            po = HomePage(self.driver)
            po.Click_touch_back()

        except:
            po = Operation(self.driver)
            po.screenShot()

    def test_Home_login_yesterday(self):
        '''test017：验证首页查看宝贝成就昨天'''
        try:
            print('进入app首页')
            ho = HomePage(self.driver)
            ho.Person_archivement()
            mo = MinePage(self.driver)
            mo.login_days_yesterday()

        except:
            po = Operation(self.driver)
            po.screenShot()


    def test_Home_login_sevenday(self):
        '''test017：验证首页查看宝贝成就最近7天'''
        try:
            print('进入app首页')
            ho = HomePage(self.driver)
            ho.Person_archivement()
            mo = MinePage(self.driver)
            mo.login_days_sevenday()

        except:
            po = Operation(self.driver)
            po.screenShot()

    def test_Home_login_thirtyday(self):
        '''test017：验证首页查看宝贝成就最近30天'''
        try:
            print('进入app首页')
            ho = HomePage(self.driver)
            ho.Person_archivement()
            mo = MinePage(self.driver)
            mo.login_days_thirtyday()

        except:
            po = Operation(self.driver)
            po.screenShot()


    def test_IHomeTest_Search_None(self):
        '''test0018验证首页搜索功能'''
        try:
            po = HomePage(self.driver)
            po.searchNull()

        except:
            po = Operation(self.driver)
            po.screenShot()


    def test_IHomeTest_Search_Back(self):
        '''test0019验证首页搜索返回功能'''
        try:
            po = HomePage(self.driver)
            po.searchBack()

        except:
            po = Operation(self.driver)
            po.screenShot()

    def test_JHomeTest_Person_Help(self):
        '''test0019验证首页-宝贝成就-帮助提示'''
        try:
            po = HomePage(self.driver)
            po.Person_archivement_help()
        except:
            po = Operation(self.driver)
            po.screenShot()

    def test_Kclick_freedom_listen(self):
        '''test0019验证首页-点击随身听播放'''
        try:
            po = HomePage(self.driver)
            po.Freedomlisten()
        except:
            po = Operation(self.driver)
            po.screenShot()


    def test_Kclick_freedom_listen_play(self):
        '''test0019验证首页-点击随身听-进入子页面'''
        try:
            po = HomePage(self.driver)
            po.Go_Freedomlisten()
        except:
            po = Operation(self.driver)
            po.screenShot()

    def test_Kclick_freedom_listen_OneKey(self):
        '''test0019验证首页-点击随身听-一键哄睡'''
        try:
            po = HomePage(self.driver)
            po.FreedomListenOneKey()
        except:
            po = Operation(self.driver)
            po.screenShot()

