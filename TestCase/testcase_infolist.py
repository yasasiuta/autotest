import unittest

from PageObject.login_page import Login
from  PageObject.infolist_page import Infolist_Page

'''
信息列表测试用例
'''
class test_addinfo(unittest.TestCase):
    def setUp(self):
        print("开始初始化测试环境")
        loginpage = Login()
        loginpage.login()

    def test_addinfo_ok_1(self):
        infopage = Infolist_Page()
        infopage.go_to_infolist()
        infopage.quick_add("ce13333","789789798","15548754545")





if __name__ == '__main__':
    unittest.main