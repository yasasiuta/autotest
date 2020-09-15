from selenium import webdriver
'''
封装UI的基本操作

'''

class BasePage(object):

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def locator(self, loc):
        return self.driver.find_element(*loc)

    def open(self):
        self.driver.get(self.url)



