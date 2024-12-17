from FrameworkLevel.utilities.StaticdataManager import StaticdataManager
from FrameworkLevel.utilities.InstanceWebElement import InstanceWebElement
from FrameworkLevel.utilities.Common import Common
from AutomationTestLevel.locators.UIDashboardPage import UIDashboardPage
import time

class DashboardPage:
    
    def __init__(self):
        self.driver = Common.driver
        
    # def loc_ele_searchresult(self,data):
    #     UIDashboardPage.loc_ele_searchresult[-1]=UIDashboardPage.loc_ele_searchresult[-1].format(data)
    #     self.loc_ele_searchresult=InstanceWebElement(self.driver,UIDashboardPage.loc_ele_searchresult)
    #     return self.loc_ele_searchresult
        
    # def loc_ele_inputsearch(self):
    #     self.loc_ele_inputsearch=InstanceWebElement(self.driver,UIDashboardPage.loc_ele_inputsearch)
    #     return self.loc_ele_inputsearch
    