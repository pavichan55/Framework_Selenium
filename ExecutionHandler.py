import config
import pandas
from FrameworkLevel.utilities.StaticdataManager import StaticdataManager
from FrameworkLevel.utilities.ExcelReader import ExcelReader
from FrameworkLevel.utilities.DynamicDataManager import DynamicDataManager
from FrameworkLevel.utilities.FunctionTrackerFileGenerator import FunctionTrackerFileGenerator
from FrameworkLevel.utilities.BasePage import BasePage
from FrameworkLevel.utilities.GlobalLogger import GlobalLogger

from datetime import date
today = date.today()
f= open(f"{today}.log","w+")
f.close()
GlobalLogger()

if config.functionTrue:
    FunctionTrackerFileGenerator()
    print("Success")
else:
    FunctionTrackerFileGenerator()
    
    url = StaticdataManager.getData("url")
    
    exceutionController_path = f"./AutomationTestLevel/{config.local}/ExecutionController.xlsx"
    
    read_ExecutionController = pandas.read_excel(exceutionController_path,config.testSuite).to_dict()
    
    STATUS_DICT = read_ExecutionController['Status']


    TEST_CASE_ID_DICT = read_ExecutionController['TestCase_ID']
    
    TESTDATA_FILENAME = read_ExecutionController['testdata']
    
    TESTCASE_DESCRIPTION_DICT = read_ExecutionController['TestDescription']
    #print(TESTCASE_DESCRIPTION_DICT)
    
    runstatus_yes_Keys = [key for key,value in STATUS_DICT.items() if value=="Yes"]
    
    test_case_ids = [TEST_CASE_ID_DICT[key]  for key in runstatus_yes_Keys]
    
    testdata_name = [TESTDATA_FILENAME[key] for key in runstatus_yes_Keys]
    
    test_description = [TESTCASE_DESCRIPTION_DICT[key] for key in runstatus_yes_Keys]
    
    ExecutionControllerData = {}
    for indexvalue in range(len(test_case_ids)):
        ExecutionControllerData[test_case_ids[indexvalue]]={"testdata":testdata_name[indexvalue],"testcase_Description":test_description[indexvalue]}
    #print(ExecutionControllerData)
    DynamicDataManager.runtimedata["ExecutionControllerData"]=ExecutionControllerData
    
    testSuiteFile_path=ExcelReader(f"./AutomationTestLevel/{config.local}/testdata/"+config.testSuite+".xlsx")
    testSuiteFile_path.extractData(test_case_ids)
    testFlowSuite = DynamicDataManager.runtimedata["testFlowSuite"]
    
    testDataSuite = DynamicDataManager.runtimedata['testDataSuite']
    
    for key,value in testFlowSuite.items():
        testFlowSuite[key]['iterDictTestData'] = testDataSuite[key]['iterDictTestData']
    
    basePageObject = BasePage()
    basePageObject.execute()
