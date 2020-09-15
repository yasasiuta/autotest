import xlrd
import json

class Variable():

    # excel表中每一列的索引
    Id = 0
    CaseName = 1
    TestData = 2
    Expectation = 3
    Result = 4
    IsRun = 5



class RWFile():

    def __init__(self):
        self.workBook = xlrd.open_workbook(r'D:\MyProjects\AutoTest\Data\testcase_01.xlsx')
        self.sheetTable = self.workBook.sheet_by_name('login')

    def get_Id_index(self,caseId):
        #获取到所有的caseid
        IdList = self.sheetTable.col_values(Variable.Id)
        if caseId not in IdList:
            raise TypeError("用例编号：{}不存在".format(caseId))
        else:
            idIndex =IdList.index(caseId)
        return idIndex

    def get_CaseName(self,caseId):
        '''获取用例名称'''
        return self.sheetTable.cell(self.get_Id_index(caseId),Variable.CaseName).value

    def get_TestData(self,caseId):
        '''获取测试数据,因为读取的测试数据为字符串格式，需转化为字典，dump（字典转字符串）loads（字符串转字典）'''
        strData = self.sheetTable.cell(self.get_Id_index(caseId),Variable.TestData).value
        try:
            jsonData = json.loads(strData)
        except:
            raise TypeError("用例编号：{}的TestData数据格式有误，必须为字典格式的字符串".format(caseId))
        return jsonData


    def get_Expectation(self,caseId):
        '''获取期望结果'''
        return self.sheetTable.cell(self.get_Id_index(caseId),Variable.Expectation).value

    def get_IsRun(self,caseId):
        '''获取用例是否执行字段'''
        flag = self.sheetTable.cell(self.get_Id_index(caseId),Variable.IsRun).value
        if flag == "yes":
            flag = True
        elif flag == "no":
            flag = False
        else:
            raise TypeError("用例编号：{}的IsRun字段有误，只能是yes或no".format(caseId))

    def get_all_testdata(self,caseId):
        '''组合从excel中读取的所有数据，放在字典中方面调用'''
        allTestdata = {}
        allTestdata['CaseId'] = caseId
        allTestdata['CaseName'] = self.get_CaseName(caseId)
        allTestdata["TestData"] = self.get_TestData(caseId)
        allTestdata["Expectation"] = self.get_Expectation(caseId)
        allTestdata["IsRun"] = self.get_IsRun(caseId)

        return {**allTestdata,**self.get_all_testdata(caseId)}

    def get_ddt_data(self,caseId):
        '''将所有数据组合成ddt接收的数据格式'''
        if type(caseId).__name__ != "list":
            raise TypeError("ddt 类型的测试数据组合，传入的caseId必须是列表 ！")
        ddtData = []
        for id in caseId:
            ddtData.append(self.get_all_testdata(id))
        return ddtData





if __name__ == '__main__':
    ddtTestCaseId = ['Login_01']
    testdata = RWFile.get_TestData(ddtTestCaseId)
    print(testdata)



















