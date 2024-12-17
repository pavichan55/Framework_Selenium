import xlrd
from pandas import *
import copy
from FrameworkLevel.utilities.DynamicDataManager import DynamicDataManager
class ExcelReader:
    testFlowSuite = {}
    testDataSuite = {}
    
    def __init__(self,dataFile):
        self.workbookpath = ExcelFile(dataFile)
        
    def generateTestFlow(self,tempTestFlow,key,value):
        testFlow = []
        iterration_dict = {}
        for testFlowValues in tempTestFlow.values():
            if testFlowValues[key]=='':
                continue
            testFlow.append(testFlowValues[key])
            iterration_dict[testFlowValues[key]] = iterration_dict.get(testFlowValues[key],0)+1
        maxIterartion = max(iterration_dict.values())
        iterDictTestFlow = {valuekey:None for valuekey in range(1,maxIterartion+1)}
        for appendvalue in testFlow:
            for keyi in iterDictTestFlow:
                if iterDictTestFlow[keyi] == None:
                    iterDictTestFlow[keyi]=[appendvalue]
                elif appendvalue not in iterDictTestFlow[keyi]:
                    iterDictTestFlow[keyi].append(appendvalue)
                elif appendvalue in iterDictTestFlow[keyi]:
                    continue
                break
        ExcelReader.testFlowSuite[value]={"testFlow":testFlow,"iterDictTestFlow":iterDictTestFlow}
        
    def generateTestData(self,dictID, tempTestData,test_case_ids):
        for tcidkey in test_case_ids:
            itr_dict_creator = {key:None for key in range(0,len(dictID[tcidkey]))}
            for datakey,datavalues in tempTestData.items():
                counter=0
                for datakeytcidkey in dictID[tcidkey]:
                    if datavalues[datakeytcidkey]=="":
                        continue
                    if itr_dict_creator.get(counter)==None:
                        itr_dict_creator[counter]={datakey:datavalues[datakeytcidkey]}
                    else:
                        itr_dict_creator[counter].update({datakey:datavalues[datakeytcidkey]})
                    counter+=1
            NewDiCT = {}
            for itrcorrectorkeys,itrcorrectorvalues in itr_dict_creator.items():
                NewDiCT[itrcorrectorkeys+1]=itrcorrectorvalues
            ExcelReader.testDataSuite[tcidkey]={'iterDictTestData':NewDiCT }
        
    def __extractTestFlow(self,test_case_ids):
        testFlow = self.workbookpath.parse(self.workbookpath.sheet_names[0])
        testFlow.fillna('',inplace=True)
        testFlow = testFlow.to_dict()
        tempTestFlow = copy.copy(testFlow)
        idColumn = testFlow['ID']
        tempTestFlow.pop('ID')
        for tc_id in test_case_ids:
            if tc_id in idColumn.values():
                for key,value in idColumn.items():
                    if value==tc_id:
                        self.generateTestFlow(tempTestFlow,key, value)

    def __extractTestData(self,test_case_ids):
        testData = self.workbookpath.parse(self.workbookpath.sheet_names[1])
        testData.fillna('',inplace=True)
        testData = testData.to_dict()
        tempTestData = copy.copy(testData)
        idColumnTestData = testData['ID']
        tempTestData.pop('ID')
        tempTestData.pop('iteration')
        dictID = {}
        for idtc in test_case_ids:
            for idkey in idColumnTestData:
                if idColumnTestData[idkey]==idtc:
                    if dictID.get(idtc)==None:
                        dictID[idtc]=[idkey]
                    else:
                        dictID.setdefault(idtc, []).append(idkey)
        self.generateTestData(dictID, tempTestData,test_case_ids)
        
    def extractData(self,test_case_ids):
        self.__extractTestFlow(test_case_ids)
        DynamicDataManager.runtimedata["testFlowSuite"]=ExcelReader.testFlowSuite
        self.__extractTestData(test_case_ids)
        DynamicDataManager.runtimedata["testDataSuite"]=ExcelReader.testDataSuite