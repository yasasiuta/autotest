'''
登录界面需要覆盖的元素
'''

from selenium.webdriver import ActionChains
from PageObject.base_page import Base_Page

class Login(Base_Page):
    def __init__(self):
        self.open_url()

    def login(self):
        self.find_by_id("email").send_keys('cry')
        self.find_by_id('tg_password').send_keys('123456')
        huakuai = self.find_by_id('label')
        action = ActionChains(self.driver)
        action.click_and_hold(huakuai).perform()
        action.drag_and_drop_by_offset(huakuai, 500, 0).perform()
        self.find_by_id('login_ok').click()
        self.driver.implicitly_wait(3)
        displaypage = self.find_by_xpath('//*[@id="main-content"]/div[1]/div/ul/li/a').text
        if displaypage == '首页':
            print("登录成功！")
        else:
            print("登录失败")





if __name__ == '__main__':
    Login().login()





