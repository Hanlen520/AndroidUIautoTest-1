#coding:utf-8


from Common import MyTest
from Common.Public import Operation
from PO.MemberPage import MemberPage


class MemberTest(MyTest.MyTest):
    '''
    概要：编写以页面为单元的测试用例,，直接调用BestPage下封装好的属性和方法
    规则：必须以test开头
    '''


    def test_AMc_detail(self):
        '''test001验证首页-会员中心--查看详细信息'''
        try:
            fo = MemberPage(self.driver)
            fo.Mc_detail()

        except:
            po = Operation(self.driver)
            po.screenShot()



    def test_BMc_swipe(self):
        '''test002：验证首页--会员中心，上滑查看'''
        try:
            fo = MemberPage(self.driver)
            fo.Mc_swip()
            po = Operation(self.driver)
        except:
            po = Operation(self.driver)
            po.screenShot()