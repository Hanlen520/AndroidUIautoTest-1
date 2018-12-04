#coding=utf-8
import time, sys
from selenium.webdriver.common.by import By
from Common import BasePage
from Common import ReadData
from Common.Public import Operation
from PO.MinePage import MinePage
import random
from Common.BasePage import LocateError





class HomePage(BasePage.Base):


    def __init__(self,appium_driver):
        BasePage.Base.__init__(self,appium_driver)
        time.sleep(5)
        print('等待主页加载完成')

    login_message = (By.ID,'com.ks.kaishustory:id/view_login_name')
    #左上角头像
    person_achivement = (By.ID,'com.ks.kaishustory:id/myicon')


    '''首页-页面属性'''

    #按钮1
    bottom_icons = (By.ID,'com.ks.kaishustory:id/fixed_bottom_navigation_container')
    search_button = (By.ID,'com.ks.kaishustory:id/icon_tosearch')
    search_go = (By.ID, 'com.ks.kaishustory:id/search_go_search_tv')
    search_input_text =(By.ID,'com.ks.kaishustory:id/et_content')
    search_list_A = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.LinearLayout')
    banner = (By.ID, 'com.ks.kaishustory:id/icon')
    knowledge = (By.ID,'com.ks.kaishustory:id/homebutton_iv1')
    leader_board = (By.ID,'com.ks.kaishustory:id/homebutton_iv2')
    best_story = (By.ID, 'com.ks.kaishustory:id/homebutton_iv3')
    classification = (By.ID, 'com.ks.kaishustory:id/homebutton_iv4')
    #随身听页面
    freedom_listen = (By.ID,'com.ks.kaishustory:id/view_play_icon')
    go_freedom_listen = (By.ID,'com.ks.kaishustory:id/tv_fm_name')
    listen_play = (By.ID,'com.ks.kaishustory:id/iv_play_status')
    i_know = (By.ID,'com.ks.kaishustory:id/tv_iknow')
    #随身听页面四个按钮
    sleep_icons = (By.ID,'com.ks.kaishustory:id/tv_tab_name')


    preferredshop = (By.ID, 'cat_group5')
    getknowledgecare = (By.ID, 'img_knowledge_card')
    littleknowledge1 = (By.ID, 'tv_zhishi1')
    littleknowledge2 = (By.ID, 'tv_zhishi2')
    littleknowledge3 = (By.ID, 'tv_zhishi3')
    littleknowledge4 = (By.ID, 'tv_zhishi4')
    more = (By.ID, 'view_more')


    #已购买按钮
    buyed_icon = (By.ID,'com.ks.kaishustory:id/icon_mybuyed')

    #摸一摸按钮
    touch_icon = (By.ID,'com.ks.kaishustory:id/icon_moyimo')
    guang_tou = (By.ID,'com.ks.kaishustory:id/iv_bg')
    #摸一摸子页面的元素s
    star1_icon = (By.ID, 'com.ks.kaishustory:id/icon1')
    star2_icon = (By.ID, 'com.ks.kaishustory:id/icon2')
    star3_icon = (By.ID, 'com.ks.kaishustory:id/icon3')
    star4_icon = (By.ID, 'com.ks.kaishustory:id/icon4')
    star5_icon = (By.ID, 'com.ks.kaishustory:id/icon5')
    star6_icon = (By.ID, 'com.ks.kaishustory:id/icon6')
    back_icon = (By.ID,'com.ks.kaishustory:id/iv_back')

    #进入个人成就
    def Person_archivement(self):
        print('点击左上角头像，进入宝贝成就页面')
        self.find_element(*self.person_achivement).click()


    #进入个人成就
    def Person_archivement_help(self):
        print('点击左上角头像，进入宝贝成就页面')
        self.find_element(*self.person_achivement).click()
        print('点击右上角帮助')
        po = Operation(self.driver)
        po.clickDot(999,145)
        print('查看帮助提示成功！')



    '''首页-页面封装方法'''
    def get_login_Message(self):
        mo = MinePage(self.driver)
        mname = format(sys._getframe().f_code.co_name)
        # print(mname)
        ro = ReadData.readdata(mname)
        # print('ro列表',ro)
        uname = ro[0]
        pwd = ro[1]
        print('登录用户名和密码：',uname,pwd)
        mo.login(uname,pwd)
        self.login_or_not()



    def login_or_not(self):
        time.sleep(2)
        print('进入app首页，获取左上角登录用户名')
        message = self.find_element(*self.login_message).text
        print('判断用户名是否为请登录')
        if message != '登录查看宝贝成就':
            print("该用户已经登录，开始执行用例！")
        else:
            print("该用户还没有登录，登录APP！")
            self.get_login_Message()


    '''首页搜索框输入方法'''
    def searchinput(self,text):
        print('点击搜索按钮，进入搜索页面')
        self.find_element(*self.search_button).click()
        print('清除搜索框的已有文字')
        self.find_element(*self.search_input_text).clear()
        print('输入搜索内容',text)
        return self.find_element(*self.search_input_text).send_keys(text)

    '''首页搜索按钮点击方法'''
    def searchClick(self):
        print('点击进行搜索')
        return self.find_element(*self.search_go).click()

    def searchNull(self):
        self.search()
        print('点击搜索按钮，进行搜索')
        self.find_element(*self.search_go).click()
        print('搜索成功！')



    def searchBack(self):
        self.search()
        po = Operation(self.driver)
        po.goback()
        print('返回成功！')


    def search(self):
        print('点击首页-搜索按钮，进入搜索页面')
        return self.find_element(*self.search_button).click()

    '''首页搜索完整方法'''
    def searchText(self,text=None):
        self.searchinput(text)
        self.searchClick()



    def leaderboard(self):
        print('进入app首页，点击排行榜--热播榜')
        return self.find_element(*self.leader_board).click()

    def clickbottom(self,x=0):
        '''首页底部按钮：依次代表：0-故事；1-乐园；2-课程；3-我的'''

        L = self.find_elements(*self.bottom_icons)
        # print(L)
        if x == 0:
            print('进入首页，默认故事页面')
            return L[x].click()
        elif x == 1:
            print('进入首页，乐园页面')
            return L[x].click()
        elif x == 2:
            print('进入首页，课程页面')
            return L[x].click()
        else:
            print('进入首页，我的页面')
            return L[x].click()


    #进入小知识页面
    def small_knowlege(self):
        print('点击小知识，进入小知识页面')
        self.find_element(*self.knowledge).click()


    #进入会员中心
    def MemberCenter(self):
        print('进入app首页--会员中心')
        return self.find_element(*self.best_story).click()

    #进入分类
    def Classification(self):
        self.find_element(*self.classification).click()

    #进入随心听
    def Freedomlisten(self):
        print('点击首页随身听播放按钮，进行播放')
        self.find_element(*self.freedom_listen).click()
        print('播放成功！')


    #进入随心听
    def Go_Freedomlisten(self):
        print('点击随身听区域，进入子页面')
        self.find_element(*self.go_freedom_listen).click()
        try:
            self.find_element(*self.i_know).click()
            print('初次进入，点击我知道了，成功！')
        except:
            print('操作成功')

    #进入随心听
    def Go_FreedomlistenPlay(self):
        print('点击随身听区域，进入子页面')
        self.find_element(*self.go_freedom_listen).click()
        try:
            self.find_element(*self.i_know).click()
            print('初次进入，点击我知道了，成功！')
        except:
            print('用户不是初次进入，无需提示！')
        self.find_element(*self.listen_play).click()
        print('播放成功')

    def FreedomListenOneKey(self):
        self.Go_Freedomlisten()
        List = self.find_elements(*self.sleep_icons)
        # x = random.randint(0,len(List))
        print('点击一键哄睡按钮，进入一键哄睡')
        List[0].click()
        print('操作成功！')

    def FreedomListenSleepStory(self):
        self.Go_Freedomlisten()
        List = self.find_elements(*self.sleep_icons)
        # x = random.randint(0,len(List))
        print('点击哄睡故事按钮，进入哄睡故事页面')
        List[1].click()
        print('操作成功！')


    def FreedomListenSleepStory(self):
        self.Go_Freedomlisten()
        List = self.find_elements(*self.sleep_icons)
        # x = random.randint(0,len(List))
        print('点击摇篮曲按钮，进入摇篮曲页面')
        List[2].click()
        print('操作成功！')

    def FreedomListenSleepStory(self):
        self.Go_Freedomlisten()
        List = self.find_elements(*self.sleep_icons)
        # x = random.randint(0,len(List))
        print('点击亲子时光按钮，进入亲子时光页面')
        List[3].click()
        print('操作成功！')


    #点击已购买按钮
    def Click_buyed_course(self):
        print('点击首页上方的已购买按钮')
        self.find_element(*self.buyed_icon).click()
        mo = MinePage(self.driver)
        mo.go_buyed_course()

    def Click_buyed_story(self):
        print('点击首页上方的已购买按钮')
        self.find_element(*self.buyed_icon).click()
        mo = MinePage(self.driver)
        mo.go_buyed_story()

    def Click_buyed_order(self):
        print('点击首页上方的已购买按钮')
        self.find_element(*self.buyed_icon).click()
        mo = MinePage(self.driver)
        mo.go_buyed_order()

    def Click_buyed_updatenotice(self):
        print('点击首页上方的已购买按钮')
        self.find_element(*self.buyed_icon).click()
        mo = MinePage(self.driver)
        mo.go_buyed_updatenotice()

    #点击摸一摸
    def Click_touch(self):
        time.sleep(3)
        print(self.driver.page_source)
        print('点击首页右上角-摸一摸按钮')
        self.find_element(*self.touch_icon).click()
        #等待小光头渲染完成，否则会造成定位失败
        time.sleep(2)
        print('点击凯叔小光头')
        po = Operation(self.driver)
        #判断凯叔光头是否存在
        if po.Element(*self.guang_tou):
            po.clickDot(526,1104)
            print('操作成功')
        time.sleep(5)
        #判断是否进入星球页面
        if po.Element(*self.star1_icon):
            print('进入星球页面成功！')
            time.sleep(2)
        else:
            print('进入星球页面失败')
            raise LocateError

    def Click_touch_back(self):
        time.sleep(3)
        print('点击首页右上角-摸一摸按钮')
        self.find_element(*self.touch_icon).click()
        #等待小光头渲染完成，否则会造成定位失败
        time.sleep(2)
        po = Operation(self.driver)
        print('点击凯叔小光头')
        po.clickDot(526,1250)
        time.sleep(5)
        print('点击成功！')
        self.find_element(*self.back_icon).click()
        print('返回成功')

    def Click_touch1(self):
        self.Click_touch()
        print('等待加载时间')
        time.sleep(12)
        print('点击第1个星球收听！')
        self.driver.find_element(*self.star1_icon).click()
        print('再次点击，关闭收听！')
        time.sleep(3)
        self.driver.find_element(*self.star1_icon).click()
        print('收听-关闭成功！')

    def Click_touch2(self):
        self.Click_touch()
        print('等待加载时间')
        time.sleep(12)
        print('点击第2个星球收听！')
        self.find_element(*self.star2_icon).click()
        print('再次点击，关闭收听！')
        time.sleep(3)
        self.find_element(*self.star2_icon).click()
        print('收听-关闭成功！')



    def Click_touch3(self):
        self.Click_touch()
        print('等待加载时间')
        time.sleep(12)
        print('点击第3个星球收听！')
        self.find_element(*self.star3_icon).click()
        print('再次点击，关闭收听！')
        time.sleep(3)
        self.find_element(*self.star3_icon).click()
        print('收听-关闭成功！')



    def Click_touch4(self):
        self.Click_touch()
        print('等待加载时间')
        time.sleep(12)
        print('点击第4个星球收听！')
        self.find_element(*self.star4_icon).click()
        print('再次点击，关闭收听！')
        time.sleep(3)
        self.find_element(*self.star4_icon).click()
        print('收听-关闭成功！')




    def Click_touch5(self):
        self.Click_touch()
        print('等待加载时间')
        time.sleep(12)
        print('点击第5个星球收听！')
        self.find_element(*self.star5_icon).click()
        print('再次点击，关闭收听！')
        time.sleep(3)
        self.find_element(*self.star5_icon).click()
        print('收听-关闭成功！')



    def Click_touch6(self):
        self.Click_touch()
        print('等待加载时间')
        time.sleep(12)
        print('点击第6个星球收听！')
        self.find_element(*self.star6_icon).click()
        print('再次点击，关闭收听！')
        time.sleep(3)
        self.find_element(*self.star6_icon).click()
        print('收听-关闭成功！')



    def Click_touch_again(self):
        self.Click_touch()
        print('等待加载时间')
        time.sleep(8)
        print('再次点击，进行飞行！')
        po = Operation(self.driver)
        print('点击凯叔小光头')
        po.clickDot(536,849)
        print('等待加载时间')
        time.sleep(5)
        List = [self.find_element(*self.star1_icon),self.find_element(*self.star2_icon),self.find_element(*self.star3_icon),self.find_element(*self.star4_icon),self.find_element(*self.star5_icon),self.find_element(*self.star6_icon)]
        x = random.randint(0,len(List))
        print('xxxx-------',x)
        print('随机选择一个星球收听')
        List[x].click()
        time.sleep(3)
        print('点击关闭收听')
        List[x].click()
        print('关闭成功！')
        self.find_element(*self.back_icon).click()
        print('返回成功')



# #测试用
# if __name__ =="__main__":
#
#     p = HomePage('xxx')
#     print(p.search_area)





