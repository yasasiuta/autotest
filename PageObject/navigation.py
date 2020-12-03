
from selenium.webdriver.common.by import By

from PageObject.base_page import BasePage

class navigation(BasePage):
    home_page = (By.CSS_SELECTOR, '#leftside-navigation > ul > li:nth-child(1) > a')
    info_config = (By.ID, 'b46de828-6a8e-11e6-8b77-86f30ca893d3')
    yindao_page = (By.ID, '3b8ea4be-88dd-11e8-9a94-a6cf71072f73')

    def enter_yindao_page(self):
        self.driver.find_element(*self.info_config)
