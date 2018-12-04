#coding:utf-8
from appium import webdriver
import os,time,unittest,sys,shutil
from Common import MyTest,Public
from Common.BasePage import LocateError
from Common.Public import Operation
from PO.HomePage import HomePage
from PO.MinePage import MinePage
from Common import ReadData


class MineTest(MyTest.MyTest):


    def test_Arecent_login(self):
        '''我的页面-test001验证最近登录'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.recentlogin()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')


    def test_Bmine_head_name(self):
        '''我的页面test002-更换姓名'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.headname_test()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')


    def test_Cbuyed_notice(self):
        '''我的页面test003-已购买的--课程'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.go_buyed()
            po.go_buyed_course()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')


    def test_Dbuyed_story(self):
        '''我的页面test004-已购买的--故事'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.go_buyed()
            po.go_buyed_story()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')

    def test_Ebuyed_order(self):
        '''我的页面test005-已购买的--我的订单页面'''
        try:

            ho = HomePage(self.driver)
            ho.clickbottom(3)
            mo = MinePage(self.driver)
            mo.go_buyed()
            mo.go_buyed_order()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')


    def test_Fbuyed_update(self):
        '''我的页面test006-已购买的--更新提醒页面'''
        try:
            ho = HomePage(self.driver)
            ho.clickbottom(3)
            mo = MinePage(self.driver)
            mo.go_buyed()
            mo.go_buyed_updatenotice()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')


    def test_Gchange_portrait_sure(self):
        '''我的页面test007-点击头像-更换头像-确定'''
        try:
            ho = HomePage(self.driver)
            ho.clickbottom(3)
            mo = MinePage(self.driver)
            mo.change_portrait_sure()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')


    def test_Gchange_portrait_cancel(self):
        '''我的页面test008-点击头像-更换头像-取消'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.change_portrait_cancel()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')


    def test_Hkcoin_rechare_record(self):
        '''我的页面test009-充值K币-充值记录'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.Kcoin_record_list()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')


    def test_IDh_code_test(self):
        '''我的页面test010-兑换码-兑换'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            mname = format(sys._getframe().f_code.co_name)  # 获取当前的类名和方法名
            data = ReadData.readdata(mname)
            po = MinePage(self.driver)
            po.Dh_code_test(data[0])
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')

    def test_JLi_pin_card_look(self):
        '''我的页面test011-礼品卡-查看'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.Li_pin_card_look()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')

    def test_JLi_pin_card_shop(self):
        '''我的页面test012-礼品卡-商城-更多'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.Li_pin_card_shop()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')


    def test_KGc_coupon(self):
        '''我的页面test013-优惠券-已失效'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.Gc_coupon()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')


    def test_KGa_album_list(self):
        '''我的页面test014-我的专辑--查看列表'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.Ga_album_list()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')

    # @unittest.skip(u'强制跳过')
    def test_KGa_new_album(self):
        '''我的页面test015-我的专辑--新建专辑'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            mname = format(sys._getframe().f_code.co_name)
            newname = ReadData.readdata(mname)
            po.Ga_album_new(newname)
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')




    '''我的页面-我喜欢的封装方法'''

    # @unittest.skip(u'强制跳过')
    def test_Lmy_like_story(self):
        '''我的页面--我喜欢的--故事-点击播放全部'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.my_like_story()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')

    # @unittest.skip(u'强制跳过')
    def test_Mmy_like_story_download(self):
        '''我的页面--我喜欢的--故事-随机下载一个'''
        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.my_like_story_download()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')

    # @unittest.skip(u'强制跳过')
    def test_Nmy_like_story_download_all(self):
        '''我的页面--我喜欢的--故事-下载全部'''

        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.my_like_story_download_all()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')

    # @unittest.skip(u'强制跳过')
    def test_Omy_like_minicourse(self):
        '''我的页面--我喜欢的--微课'''

        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.my_like_minicourse()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')

    # @unittest.skip(u'强制跳过')
    def test_Pmy_like_spetialtopic(self):
        '''我的页面--我喜欢的--专题'''

        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.my_like_spetialtopic()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')

    # @unittest.skip(u'强制跳过')
    def test_Qmy_like_album(self):
        '''我的页面--我喜欢的--专辑'''

        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.my_like_album()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')

    # @unittest.skip(u'强制跳过')
    def test_Rrecent_play_story_list(self):
        '''我的页面--最近播放--故事列表'''

        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.recent_play_story_list()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')

    # @unittest.skip(u'强制跳过')
    def test_Rrecent_play_course_list(self):
        '''我的页面--最近播放--课程列表'''

        try:
            po = HomePage(self.driver)
            po.clickbottom(3)
            po = MinePage(self.driver)
            po.recent_play_course_list()
            print('操作成功！')
        except:
            po = Operation(self.driver)
            po.screenShot()
            raise LocateError('定位失败，请核查原因！')






