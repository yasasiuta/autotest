import time

from PageObject.base_page import Base_Page

class Device_Page(Base_Page):

    def go_to_device_mode(self):
        '''进入终端管理'''
        self.find_by_id('96327f6e-6aab-11e6-8b77-86f30ca893d3').click()
        self.driver.implicitly_wait(3)
        self.find_by_id('238286ce-6aad-11e6-8b77-86f30ca893d3').click()
        self.driver.implicitly_wait(3)
        self.find_by_id('stretch2').click()
        self.driver.implicitly_wait(3)


    def add_device_model(self,device_model_number):
        '''新增终端型号'''
        self.driver.find_element_by_id('dropdownMenu').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[@id="stretch2-body"]/div[1]/div[1]/div[2]/ul/li[1]/a').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('terminalType').send_keys(device_model_number)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[@id="videoInformation-content"]/div[4]/div/label[1]/input').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('doSubmit').click()
        time.sleep(2)


    def delete_device_model(self):
        self.driver.find_element_by_xpath('//*[@id="dataTables"]/tbody/tr[1]/td[3]/button[2]').click()
        time.sleep(3)
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        self.driver.implicitly_wait(3)