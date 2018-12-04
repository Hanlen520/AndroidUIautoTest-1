#coding=utf-8
import time
from selenium.webdriver.common.by import By
from Common.Public import Operation
import random
from Common import MyTest, BasePage


class MinePage(BasePage.Base, MyTest.MyTest):


    '''首页--我的页面属性'''
    i = 1

    login_name = (By.ID,'com.ks.kaishustory:id/view_login_name')
    username = (By.ID,'com.ks.kaishustory:id/et_login_mobile')
    password = (By.ID,'com.ks.kaishustory:id/et_validate_code')
    login_button = (By.ID,'com.ks.kaishustory:id/tv_login')


    '''页面元素属性'''
    myicon = (By.ID,'com.ks.kaishustory:id/fixed_bottom_navigation_container')
    my_message = (By.ID,'com.ks.kaishustory:id/iv_message_mine')
    '''通知子页面元素'''
    dynamicOrnotices = (By.ID,'com.ks.kaishustory:id/tv_tab_title')
    back = (By.ID,'	com.ks.kaishustory:id/iv_back')

    login_count = (By.ID,'com.ks.kaishustory:id/tv_baby_achi_login_count')
    '''登录天数'''

    listen_count = (By.ID,'com.ks.kaishustory:id/tv_baby_achi_listened_count')
    '''最近登录子页面元素'''

    duration = (By.ID,'com.ks.kaishustory:id/tv_baby_achi_listened_duration')

    buyed = (By.ID,'com.ks.kaishustory:id/view_mybuyed')
    '''已购买子页面'''
    b_cource = (By.XPATH,"//*[@class='android.support.v7.app.ActionBar$Tab' and @index = '1']")
    b_story = (By.XPATH,"//*[@class='android.support.v7.app.ActionBar$Tab' and @index = '0']")
    b_recent_buy = (By.ID,'com.ks.kaishustory:id/tv_recently_buy')
    b_recent_update = (By.ID,'com.ks.kaishustory:id/tv_recently_update')
    b_more = (By.ID,'com.ks.kaishustory:id/title_more_iv')
    b_order = (By.ID,'com.ks.kaishustory:id/ly_item1')
    b_update = (By.ID,'com.ks.kaishustory:id/ly_item2')


    '''充值K币子页面元素'''#(By.ID,'')
    Kcoin = (By.ID,'com.ks.kaishustory:id/view_buykb')
    K_recharge_icon =(By.ID,'com.ks.kaishustory:id/btn_custom_charge')
    K_edit = (By.ID,'com.ks.kaishustory:id/cz_kbcustom')
    K_recharge_record = (By.ID,'com.ks.kaishustory:id/view_chargelist')
    K_recharge_no = (By.ID,'com.ks.kaishustory:id/tv_order_no')
    K_recharge_list1 = (By.ID,'com.ks.kaishustory:id/kball1')
    K_recharge_list2 = (By.ID, 'com.ks.kaishustory:id/kball2')
    K_recharge_list3 = (By.ID, 'com.ks.kaishustory:id/kball3')
    K_recharge_list4 = (By.ID, 'com.ks.kaishustory:id/kball4')
    K_recharge_list5 = (By.ID, 'com.ks.kaishustory:id/kball5')
    K_recharge_list6 = (By.ID, 'com.ks.kaishustory:id/kball6')


    '''兑换码子元素'''
    dhcode = (By.ID,'com.ks.kaishustory:id/mine_duihuan_layout')
    dh_input = (By.ID,'com.ks.kaishustory:id/exchange_input_edit')
    dh_icon = (By.ID,'com.ks.kaishustory:id/exchange_duihuan_btn')
    dh_message = (By.ID,'com.ks.kaishustory:id/exchange_tip_tv')


    '''礼品卡页面子元素'''
    lipincard = (By.ID,'com.ks.kaishustory:id/mine_lipinka_layout')
    lpc_names = (By.ID,'com.ks.kaishustory:id/lipinka_name')
    lpc_see = (By.ID,'com.ks.kaishustory:id/lipinka_see')
    lpc_shop = (By.ID,'com.ks.kaishustory:id/bar_right')
    lpc_shop_more = (By.ID,'com.ks.kaishustory:id/view_more')
    lpc_change_message = (By.ID,'com.ks.kaishustory:id/gift_card_editmodify_layout')
    lpc_gift = (By.ID,'com.ks.kaishustory:id/gift_card_editmodify_layout')
    lpc_order = (By.ID,'com.ks.kaishustory:id/bar_right')
    lpc_order_record = (By.ID,'com.ks.kaishustory:id/tv_order_no')


    '''优惠券页面子元素'''
    coupon = (By.ID,'com.ks.kaishustory:id/mine_youhui_layout')
    couponA = (By.PARTIAL_LINK_TEXT,u'优惠券')
    couponB = (By.PARTIAL_LINK_TEXT,u'已失')
    click_areas = (By.CLASS_NAME,'android.support.v7.app.ActionBar$Tab')
    couponB_names = (By.ID,'com.ks.kaishustory:id/item_coupon_name_tv')


    '''我的专辑页面子元素'''
    my_album = (By.ID,'com.ks.kaishustory:id/view_myalbum')
    # new_album = (By.ID,'com.ks.kaishustory:id/tv_new_album')
    new_album = (By.XPATH, '//android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView[@class = "android.widget.TextView"]')
    album_list = (By.ID,'com.ks.kaishustory:id/linearLayout_middle')
    new_album_name = (By.ID,'com.ks.kaishustory:id/et_album_name')
    new_album_sure = (By.ID,'com.ks.kaishustory:id/bar_right')
    new_album_cancel = (By.ID,'com.ks.kaishustory:id/iv_back')

    '''最近播放页面子元素'''
    recent_play = (By.ID,'com.ks.kaishustory:id/view_mylistened')
    rp_storyOrcources_icons = (By.CLASS_NAME,'android.support.v7.app.ActionBar$Tab')
    rp_download_icons = (By.ID,'com.ks.kaishustory:id/iv_state')
    #列表中任取一个记录的名字
    rp_list_name = (By.ID,'com.ks.kaishustory:id/seed_name')
    rp_back = (By.ID, 'com.ks.kaishustory:id/iv_back')

    '''最近登录子页面元素'''
    days = (By.CLASS_NAME, 'android.widget.TextView')

    '''我喜欢的子页面元素'''
    my_like = (By.ID,'com.ks.kaishustory:id/view_myfavor')
    ml_click_areas = (By.CLASS_NAME,'android.support.v7.app.ActionBar$Tab')
    ml_play_all = (By.ID,'com.ks.kaishustory:id/tv_play_status')
    ml_download_ones = (By.ID,'com.ks.kaishustory:id/iv_state')
    ml_download_all = (By.ID,'com.ks.kaishustory:id/iv_download')
    ml_choose_one = (By.ID,'com.ks.kaishustory:id/iv_select_state')
    ml_choose_all = (By.ID,'com.ks.kaishustory:id/batch_download_iv_all_select')
    ml_choose_downloadicon = (By.ID,'com.ks.kaishustory:id/batch_download_down_v')
    ml_play_time = (By.ID,'com.ks.kaishustory:id/tv_currenttime')


    '''我的下载页面子元素'''
    my_download = (By.ID,'com.ks.kaishustory:id/view_mydownloaded')
    md_storyOrcourse = (By.ID,'com.ks.kaishustory:id/tab_story')
    md_albums =  (By.ID,'com.ks.kaishustory:id/tab_weike')
    md_storys = (By.ID,'com.ks.kaishustory:id/tab_story')
    md_play_all = (By.ID,'com.ks.kaishustory:id/tv_play')
    md_delete = (By.ID,'com.ks.kaishustory:id/iv_delete')
    md_play_time = (By.ID,'com.ks.kaishustory:id/tv_currenttime')
    md_delete_all = (By.ID,'com.ks.kaishustory:id/iv_all_select')
    md_delete_icon = (By.ID,'com.ks.kaishustory:id/view_delete')


    '''我的作品页面子元素'''
    my_creation = (By.ID,'com.ks.kaishustory:id/view_mydownloaded')
    mc_list = (By.ID,'com.ks.kaishustory:id/item_works_seed_icon')
    mc_give_thumb = (By.ID,'com.ks.kaishustory:id/item_works_seed_icon')
    mc_play_icon = (By.ID,'com.ks.kaishustory:id/works_info_play_iv')
    mc_give_thumb_icon = (By.ID,'com.ks.kaishustory:id/works_info_zan_icon')
    mc_share_cancel = (By.ID,'com.ks.kaishustory:id/works_share_tv_cancel')
    mc_share_wechat = (By.LINK_TEXT,u'微信')
    mc_share_circle_of_friends = (By.LINK_TEXT,u'朋友圈')


    '''优选商城页面子元素'''
    youxuan_shop = (By.ID,'com.ks.kaishustory:id/view_youzan_layout')

    '''优选订单页面子元素'''
    youxuan_order =(By.ID,'com.ks.kaishustory:id/view_yzorder')


    '''超级体验官子元素'''
    tiyan_officer =(By.ID,'com.ks.kaishustory:id/view_expreince_layout')
    to_close = (By.ID,'com.ks.kaishustory:id/common_webview_iv_colse')
    to_change = (By.ID,'com.ks.kaishustory:id/tv_phone_state')
    to_bind = (By.ID,'com.ks.kaishustory:id/tv_weixin_state')
    to_cancel = (By.ID,'com.ks.kaishustory:id/tv_cancel')
    to_verify = (By.ID,'com.ks.kaishustory:id/tv_ok')
    to_verify_send_code = (By.ID,'com.ks.kaishustory:id/tv_send_code')
    to_bind_bind = (By.ID,'com.ks.kaishustory:id/btn_p')
    to_bind_cancel = (By.ID,'com.ks.kaishustory:id/btn_p')
    to_bind_wechat_back = (By.ID,'com.tencent.mm:id/j8')



    zh_bing = (By.ID,'com.ks.kaishustory:id/view_bangding_layout')
    '''联系客服'''
    customer = (By.ID,'com.ks.kaishustory:id/view_kefu')

    '''给个好评'''
    give_five = (By.ID,'com.ks.kaishustory:id/view_pingjia')

    '''当前版本'''
    current_version =(By.ID,'com.ks.kaishustory:id/item_currentv')
    cv_update = (By.ID,'com.ks.kaishustory:id/bt_update')


    copy_icon = (By.ID,'com.ks.kaishustory:id/home_uid_copy_tv')

    '''头像子元素'''

    head_portrait = (By.ID,'com.ks.kaishustory:id/myicon')
    head_take_photo = (By.ID,'com.ks.kaishustory:id/mine_duihuan_layout')
    head_photo_choose = (By.ID,'com.ks.kaishustory:id/view2')
    head_portrait_cancel = (By.ID,'com.ks.kaishustory:id/view3')
    photos = (By.ID,'com.android.documentsui:id/icon_mime')
    photos2 = (By.CLASS_NAME,'android.widget.ImageView')
    photo_choose_sure1 = (By.ID,'com.ks.kaishustory:id/menu_crop')
    photo_choose_sure2 = (By.XPATH, '//android.widget.TextView[@content-desc="裁剪"]')
    #外层取消
    photo_chosse_cancel1 = (By.ID,'com.ks.kaishustory:id/view3')
    #内层取消按钮-X
    photo_choose_cancel2 = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')


    '''head_portrait子页面元素'''
    head_name = (By.ID, 'com.ks.kaishustory:id/tv_name')
    hp_nickname = (By.ID,'com.ks.kaishustory:id/tv_name')
    hp_sex = (By.ID,'com.ks.kaishustory:id/genderview')
    hp_date = (By.ID,'com.ks.kaishustory:id/tv_birthday')
    hp_sure = (By.ID,'com.ks.kaishustory:id/tv_ok')
    hp_cancel = (By.ID,'com.ks.kaishustory:id/tv_cancel')
    hp_sex_options = (By.ID,'com.ks.kaishustory:id/main_wheel_curved')
    hp_save = (By.ID,'com.ks.kaishustory:id/bar_right')


    def login(self,uname,pwd):
        print('点击登录用户名，进入登录页面')
        self.find_element(*self.login_name).click()
        print('获取用户名登录框的文字')
        text = self.find_element(*self.username).text
        print(text)
        print('点击用户名输入框')
        self.find_element(*self.username).click()
        po = Operation(self.driver)
        po.clearText(text)
        '''调用更加稳定的adb输入'''
        print('点击用户名输入框')
        self.find_element(*self.username).click()
        print('输入用户名')
        po.adbSendText(uname)
        print('点击密码输入框')
        self.find_element(*self.password).click()
        po.adbSendText(pwd)
        print('点击登录')
        self.find_element(*self.login_button).click()




    '''首页--我的页面的方法'''
    def clickmessage(self):
        return self.driver.find_element(*self.my_message)


    def messagetest(self):
        self.clickmessage()
        List = self.driver.find_elements(*self.dynamicOrnotices)
        list = List.reverse()
        for i in list:
            i.click()
            po = Operation(self.driver)
            po.swipeUp()


    '''最近登录页面封装方法'''
    def recentlogin(self):
        print('点击最近登录')
        self.find_element(*self.login_count).click()
        self.driver.implicitly_wait(2)
        po = Operation(self.driver)
        time.sleep(1)
        po.swipeLeft(500)
        time.sleep(1)
        po.swipeUp(500)
        time.sleep(1)
        po.swipeLeft(500)
        time.sleep(1)
        po.swipeUp(500)
        time.sleep(1)
        po.swipeRight(500)
        time.sleep(1)



    '''个人信息页面方法封装'''
    def go_head_name(self):
        print('点击用户名，进入修改页面')
        return self.driver.find_element(*self.head_name).click()


    def hn_change_sex(self):
        self.driver.find_element(*self.hp_sex).click()
        # self.driver.find_elements(*self.hp_sex_options)
        self.driver.swipe(630,1695,630,1595, 500)
        self.driver.swipe(630,1595,630,1695, 500)
        time.sleep(1)
        return self.driver.find_element(*self.hp_sure).click()

    def hn_change_name(self):
        new_name = u'小明' + str(random.randint(0,1000))
        print(new_name)
        self.driver.find_element(*self.hp_nickname).clear()
        return self.driver.find_element(*self.hp_nickname).send_keys(new_name)

    def hn_change_birthday(self):
        print('选择出生年月')
        self.driver.find_element(*self.hp_date).click()
        time.sleep(1)
        self.driver.swipe(175,1079,175,1199, 500)
        time.sleep(1)
        print('点击确定')
        return self.driver.find_element(*self.hp_sure).click()

    def headname_test(self):
        self.driver.implicitly_wait(1)
        self.go_head_name()
        # self.hn_change_name()
        # self.hn_change_sex()
        self.hn_change_birthday()
        print('点击保存')
        return self.driver.find_element(*self.hp_save).click()

    '''已购买子页面封装方法'''
    def go_buyed(self):
        print('进入已购买页面--默认故事页面')
        return self.driver.find_element(*self.buyed).click()

    def go_buyed_course(self):
        '''进入已购买-课程页面'''
        time.sleep(1)
        print('点击课程')
        self.driver.find_element(*self.b_cource).click()
        #点击最近更新-上滑-截图
        try:
            print('点击最近更新')
            self.driver.find_element(*self.b_recent_update).click()
        except:
            print('没有已购买的课程，无法点击最近更新！')
        po = Operation(self.driver)
        time.sleep(1)
        po.swipeUp()
        try:
            print('点击最近购买')
            self.driver.find_element(*self.b_recent_buy).click()
        except:
            print('没有已购买的课程，无法点击最近购买！')
        #return self.driver.swipe(540,540,540,1332,500)



    def go_buyed_story(self):
        '''进入已购买的-故事页面'''
        # self.go_buyed()
        time.sleep(1)
        #点击最近更新-上滑-截图
        try:
            print('点击最近更新')
            self.driver.find_element(*self.b_recent_update).click()
        except:
            print('没有已购买的故事，无法点击最近更新！')
        po = Operation(self.driver)
        time.sleep(1)
        po.swipeUp()
        try:
            print('点击最近购买')
            self.driver.find_element(*self.b_recent_buy).click()

        except:
            print('没有已购买的故事，无法点击最近购买！')



    def go_buyed_order(self):
        '''进入已购买的-更多-我的订单页面'''
        # self.go_buyed()
        print('点击右上角更多')
        self.driver.find_element(*self.b_more).click()
        print('点击我的订单')
        self.driver.find_element(*self.b_order).click()
        po = Operation(self.driver)
        return po.swipeUp()

    def go_buyed_updatenotice(self):
        '''进入已购买的-更多-更新提醒'''
        # self.go_buyed()
        print('点击右上角更多')
        self.driver.find_element(*self.b_more).click()
        print('点击更新提醒')
        self.driver.find_element(*self.b_update).click()
        po = Operation(self.driver)
        return po.swipeUp()



    '''更改头像方法'''
    def change_portrait_sure(self):
        self.driver.implicitly_wait(2)
        print('点击用户头像')
        self.driver.find_element(*self.head_portrait).click()
        print('点击从相册选择')
        self.driver.find_element(*self.head_photo_choose).click()
        po = Operation(self.driver)
        # n = random.randint(100,1000)
        time.sleep(2)
        po.swipeUp()
        List = []
        while len(List) == 0:
            print('随机选择一张图片')
            List = self.driver.find_elements(*self.photos2)
        x = random.randint(0,len(List)-1)
        List[x].click()
        print('点击确定，更新成功')

        return self.driver.find_element(*self.photo_choose_sure1).click()

    def change_portrait_cancel(self):

        self.driver.implicitly_wait(2)
        print('点击用户头像')
        self.driver.find_element(*self.head_portrait).click()
        print('点击从相册选择')
        self.driver.find_element(*self.head_photo_choose).click()
        time.sleep(1)
        print('选择一张图片')
        self.driver.find_element(*self.photos).click()
        print('点击取消，取消成功')
        return self.find_element(*self.photo_choose_cancel2).click()
        # return self.driver.find_element(*self.photo_chosse_cancel).click()



    '''充值K币封装方法'''
    def Kcoin_record_list(self):
        print('点击充值K币')
        self.find_element(*self.Kcoin).click()
        print('点击充值按钮')
        self.find_element(*self.K_recharge_icon).click()
        print('点击充值记录，进行查看')
        return self.find_element(*self.K_recharge_record).click()



    '''兑换码封装方法'''

    def Dh_code_test(self,num):
        print('点击兑换码')
        self.find_element(*self.dhcode).click()
        print('点击输入金额')
        self.find_element(*self.dh_input).click()
        po = Operation(self.driver)
        print('输入兑换码',num)
        po.adbSendText(num)

        print('点击充值按钮!')
        # self.find_element(*self.dh_input).send_keys('9443222914030903')
        time.sleep(1)

        self.find_element(*self.dh_icon).click()

        text = self.find_element(*self.dh_message).get_attribute("text")
        return print('兑换后提示：',text)


    '''礼品卡封装方法'''
    def Li_pin_card(self):
        print('进入礼品卡页面')
        return self.find_element(*self.lipincard).click()


    def Li_pin_card_look(self):
        self.Li_pin_card()
        try:
            print('随机选择一张礼品卡')
            List = self.find_elements(*self.lpc_names)
            x = random.randint(0, len(List) - 1)
            List[x].click()
            po = Operation(self.driver)
            time.sleep(1)
            po.swipeUp()
            print('查看礼品卡订单')
            self.find_element(*self.lpc_order).click()
            print('查看成功')
        except:
            print('该用户没有购买礼品卡，所以无法查看礼品卡！')



    def Li_pin_card_shop(self):
        self.Li_pin_card()
        print('点击礼品卡商城，进行查看')
        self.find_element(*self.lpc_shop).click()
        print('点击更多')
        self.find_element(*self.lpc_shop_more).click()
        print('查看成功')




    '''优惠券页面封装方法'''
    def go_coupon(self):
        po = Operation(self.driver)
        time.sleep(1)
        po.swipeUp()
        print('点击优惠券')
        return self.find_element(*self.coupon).click()

    def Gc_coupon(self):
        self.go_coupon()
        print('点击优惠券子页面-已失效')
        List = self.find_elements(*self.click_areas)
        List[1].click()
        po = Operation(self.driver)
        time.sleep(1)
        po.swipeUp()
        print('点击优惠券子页面-优惠券')
        List[0].click()
        print('查看成功')




    '''我的专辑封装方法'''
    def go_album(self):
        po = Operation(self.driver)
        time.sleep(1)
        po.swipeUp()
        print('点击我的专辑')
        return self.find_element(*self.my_album).click()

    def Ga_album_list(self):
        self.go_album()
        List = self.find_elements(*self.album_list)
        if len(List) != 0:
            print('随机选择一个专辑，点击查看')
            x = random.randint(0, len(List) - 1)
            List[x].click()
            print('查看成功')
        else:
            print('该用户还未新建专辑')

    def Ga_album_new(self,text):
        self.go_album()
        print('点击新建专辑')
        self.find_element(*self.new_album).click()
        print('清空文本框')
        self.find_element(*self.new_album_name).clear()
        print('输入新专辑名称',text)
        # text = text + str(random.randint(0,1000))
        self.find_element(*self.new_album_name).send_keys(text)
        print('点击确定，以保存新专辑名称')
        self.find_element(*self.new_album_sure).click()
        print('保存成功')


    '''我喜欢的封装方法'''
    def go_my_like(self):
        po = Operation(self.driver)
        time.sleep(1)
        po.swipeUp()
        print('点击我喜欢的，进入子页面')
        return self.find_element(*self.my_like).click()

    def my_like_story(self):
        '''点击播放全部'''
        self.go_my_like()
        time.sleep(1)
        po = Operation(self.driver)
        po.swipeUp()
        print('点击播放全部')
        self.find_element(*self.ml_play_all).click()
        print('播放成功')



    def my_like_story_download(self):
        '''随机下载一个故事'''
        self.go_my_like()
        print('随机选择一个故事，点击下载')
        List = self.find_elements(*self.ml_download_ones)
        x = random.randint(0,len(List)-1)
        List[x].click()
        print('下载成功！')

    def my_like_story_download_all(self):
        '''下载全部'''
        self.go_my_like()
        print('点击批量下载')
        self.find_element(*self.ml_download_all).click()
        print('点击全选')
        self.find_element(*self.ml_choose_all).click()
        print('点击下载按钮')
        self.find_element(*self.ml_choose_downloadicon)
        print('下载成功')



    def my_like_spetialtopic(self):
        '''我喜欢的--专题页面'''
        self.go_my_like()
        print('点击专题，进入子页面')
        List = self.find_elements(*self.ml_click_areas)
        List[1].click()
        time.sleep(1)
        po = Operation(self.driver)
        po.swipeUp()
        print('查看成功！')

    def my_like_album(self):
        '''我喜欢的--专辑页面'''
        self.go_my_like()
        print('点击专辑，进入子页面')
        List = self.find_elements(*self.ml_click_areas)
        List[2].click()
        po = Operation(self.driver)
        po.swipeUp()
        print('查看成功！')

    def my_like_minicourse(self):
        '''我喜欢的--微课'''
        self.go_my_like()
        print('点击微课')
        List = self.find_elements(*self.ml_click_areas)
        List[3].click()
        po = Operation(self.driver)
        po.swipeUp()
        print('查看成功！')




    '''最近播放封装方法'''
    def go_recent_play(self):
        print('进入首页--我的-最近播放页面')
        po = Operation(self.driver)
        time.sleep(1)
        po.swipeUp()
        self.find_element(*self.recent_play).click()

    def recent_play_story_list(self):
        self.go_recent_play()
        po = Operation(self.driver)
        print('随机选择一个故事，进行点击，收听')
        List = self.find_elements(*self.rp_list_name)
        if len(List) != 0:
            x = random.randint(0,len(List)-1)
            if x > 0:
                time.sleep(1)
                po.swipeUp()
                List[x].click()
                print('收听成功！')
        else:
            print('该用户最近没有收听故事\n')

    def  recent_play_course_list(self):
        self.go_recent_play()
        print('点击课程，进入子页面')
        course = self.find_elements(*self.rp_storyOrcources_icons)[1]
        course.click()
        po = Operation(self.driver)
        print('随机选择一个内容，进行收听！')
        try:
            List = self.find_elements(*self.rp_list_name)
            if len(List) != 0:
                x = random.randint(0, len(List) - 1)
                if x>0:
                    time.sleep(1)
                    po.swipeUp()
                    List[x].click()
                    print('收听成功！')
        except:
            print('该用户最近没有收听课程\n')

    def login_days_yesterday(self):
        print('默认进入昨天成就页面')
        po = Operation(self.driver)
        po.swipeUp()
        print('查看成功')


    def login_days_sevenday(self):
        print('左滑页面查看7天成就页面')
        po = Operation(self.driver)
        po.swipeLeft()
        time.sleep(2)
        po.swipeUp()
        print('查看成功')


    def login_days_thirtyday(self):
        print('左滑两次页面查看30天成就页面')
        po = Operation(self.driver)
        po.swipeLeft()
        time.sleep(2)
        po.swipeLeft()
        time.sleep(2)
        po.swipeUp()
        print('查看成功')

    '''页面封装方法'''

    '''页面封装方法'''

    '''页面封装方法'''

    '''页面封装方法'''

    '''页面封装方法'''

