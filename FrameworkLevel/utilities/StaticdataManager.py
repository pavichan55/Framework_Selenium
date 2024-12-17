import config
from jproperties import Properties
import json
from FrameworkLevel.utilities.DynamicDataManager import DynamicDataManager
from FrameworkLevel.utilities.DynameRuntimeDatastorage import DynameRuntimeDatastorage

class StaticdataManager:
    with open(config.dirname+"/"+"MethodDictionary.txt","r",encoding="utf-8") as repodata:
        if not config.functionTrue:
            REPO_DATA = json.loads(repodata.read())
        
    def __init__(self):
        self.local = config.local
        
    @staticmethod
    def getData(data):
        staticproperties = Properties()
        staticDataPath = f"./AutomationTestLevel/{config.local}/staticdata.prop"
        with open(staticDataPath,"rb") as staticdata:
            staticproperties.load(staticdata)
        return staticproperties.get(data).data
    
    @staticmethod
    def getKWDclassName(data):
        for clsnamerepokey,clsnamerepovalue in StaticdataManager.REPO_DATA.items():
            if data in clsnamerepovalue:
                return clsnamerepokey,data
            
    @staticmethod
    def getMethodLevelParamValue(data):
        iterDict = DynamicDataManager.runtimedata["testFlowSuite"][DynameRuntimeDatastorage.testCaseID]["iterDictTestFlow"]
        for iterDictKey, IterDictValue in iterDict.items():
            if DynameRuntimeDatastorage.testMethodName in IterDictValue:
                return DynamicDataManager.runtimedata["testFlowSuite"][DynameRuntimeDatastorage.testCaseID]["iterDictTestData"][iterDictKey][data]
        
        
        

