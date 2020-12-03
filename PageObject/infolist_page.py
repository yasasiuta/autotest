from PageObject.base_page import Base_Page

class Infolist_Page(Base_Page):

    def go_to_infolist(self):
        '''进入信息列表页面'''
        self.find_by_id("b46de828-6a8e-11e6-8b77-86f30ca893d3").click()
        self.find_by_id("b46dec1a-6a8e-11e6-8b77-86f30ca893d3").click()

    def quick_add(self,brand,device,simcard):
        '''快速录入'''
        self.find_by_id("quickEntryBtn").click()
        self.find_by_id('quickBrands').send_keys(brand)
        self.find_by_id("quickDevices").send_keys(device)
        self.find_by_id("quickSims").send_keys(simcard)
        self.find_by_id('quickGroupId').click()
        self.find_by_id('quickTreeDemo_2').click()
        self.find_by_id('quickSubmits').click()

    def search(self,value,keyword='brand'):
        '''信息列表搜索'''
        self.find_by_id("simpleQueryParam").send_keys(value)
        if keyword == "brand":
            result = self.find_by_xpath('//*[@id="dataTable"]/tbody/tr[1]/td[4]').text
        elif keyword == "device":
            result = self.find_by_xpath('//*[@id="dataTable"]/tbody/tr[1]/td[11]').text
        elif keyword == "simcard":
            result = self.find_by_xpath('//*[@id="dataTable"]/tbody/tr[1]/td[9]').text
        else:
            print("支持brand、device、simcard关键字搜索")
        return result

    def export(self):
        '''导出'''
        self.find_by_id("dropdownMenu1").click()
        self.find_by_id("exportId").click()


    def import_info(self):
        '''导入'''
        self.find_by_id("dropdownMenu1").click()
        self.find_by_id("importId").click()
        importbox = self.find_by_id("importBox")
        self.waitfor(10,importbox)
        self.find_by_id("importForm").click()








