import subprocess

from AutomationTestLevel.POM.MasterPage import MasterPage
from AutomationTestLevel.POM.LoginPage import LoginPage
from AutomationTestLevel.POM.DashboardPage import DashboardPage
from FrameworkLevel.utilities.DynamicDataManager import DynamicDataManager
from FrameworkLevel.utilities.StaticdataManager import StaticdataManager
from FrameworkLevel.utilities.DynameRuntimeDatastorage import DynameRuntimeDatastorage
import copy
from FrameworkLevel.utilities.Common import Common
from FrameworkLevel.utilities.GlobalLogger import GlobalLogger
import config

class BasePage:
    dataforstaticdata = ""
    
    def __init__(self):
        self.driver = None
    
    def setup(self):
        self.driver = Common.getDriver()
        
    def teardown(self):
        self.driver.quit()
        if config.execution_mode == 'docker':
            subprocess.run(["docker-compose", "down"], check=True)
        
    def execute(self):
        testHybridPacakage = DynamicDataManager.runtimedata["testFlowSuite"]
        ExecutionControllerData = DynamicDataManager.runtimedata["ExecutionControllerData"]
        #print(testHybridPacakage)
        for testCaseIDkey,testCaseValue in testHybridPacakage.items():
            testFlow = copy.copy(testCaseValue['testFlow'])
            GlobalLogger.logText(ExecutionControllerData[testCaseIDkey]["testcase_Description"])
            print(ExecutionControllerData[testCaseIDkey]["testcase_Description"])
            print(f"{testCaseIDkey} ->>{testFlow}")
            iterDictTestFlow = copy.copy(testCaseValue['iterDictTestFlow'])
            iterDictTestData = copy.copy(testCaseValue['iterDictTestData'])
            try:
                self.setup()
                for tf in testFlow:
                    DynameRuntimeDatastorage(testCaseIDkey,tf)
                    dynamicrepodata=StaticdataManager.getKWDclassName(tf)

                    func_to_run = getattr(eval(dynamicrepodata[0] + "()"), dynamicrepodata[1])


                    func_to_run()
                    (DynamicDataManager.runtimedata["testFlowSuite"][testCaseIDkey]['testFlow']).pop(0)
                    dydata=(DynamicDataManager.runtimedata["testFlowSuite"][testCaseIDkey]['iterDictTestFlow']).items()
                    for itDictkey,itrValue in dydata:
                        if tf in DynamicDataManager.runtimedata["testFlowSuite"][testCaseIDkey]['iterDictTestFlow'][itDictkey]:
                            (DynamicDataManager.runtimedata["testFlowSuite"][testCaseIDkey]['iterDictTestFlow'][itDictkey]).remove(tf)
                            break
            finally:
                if config.browserClose:
                    self.teardown()
