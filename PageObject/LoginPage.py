'''
登录界面需要覆盖的元素
'''
from selenium.webdriver.common.by import By
from PageObject.base import BasePage

class LoginPage(BasePage):
    username = (By.ID, 'email')
    password = (By.ID, 'tg_password')
    loginbtn = (By.ID, 'login_ok')
    username1 = (By.CLASS_NAME,)
    def input_text_username(self,text):
        el = self.driver.find_element(*self.username)
        el.send_keys(text)

    def input_text_password(self,text):
        el = self.driver.find_element(*self.password)
        el.send_keys(text)

    def click_btn(self):
        el = self.driver.find_element(*self.loginbtn)
        el.click()




