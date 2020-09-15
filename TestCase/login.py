from selenium import webdriver
from PageObject.LoginPage import LoginPage
import unittest
import time
from Public.RWFile import RWFile


TestCaseId = 'Login_01'

rw = RWFile()



class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\webdriver\chromedriver')
        self.url = r'http://192.168.24.142:8080/clbs/login'
        self.lp = LoginPage(self.driver,self.url)

    def tearDown(self):
        pass

    def testcase_login(self):
        '''获取测试数据'''
        TestData = rw.get_TestData(TestCaseId)
        #操作步骤
        self.lp.open()
        time.sleep(1)
        self.lp.input_text_username(TestData['username'])
        self.lp.input_text_password(TestData['password'])
        time.sleep(1)
        self.lp.click_btn()
        time.sleep(5)




if __name__ == '__main__':
    unittest.main()