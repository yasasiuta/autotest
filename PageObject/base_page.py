from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

'''
封装UI的基本操作

'''


class Base_Page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = "http://192.168.24.142:8080/clbs/login"

    def send_key(self,str):
        return self.send_key(str)

    def find_by_id(self,id):
       return self.driver.find_element_by_id(id)

    def find_by_xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)

    def open_url(self):
        return self.driver.get(self.url)

    def waitfor(self,time,location):
         return  WebDriverWait(self.driver, time).until(location)













