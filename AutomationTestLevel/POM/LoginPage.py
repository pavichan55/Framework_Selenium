from FrameworkLevel.utilities.StaticdataManager import StaticdataManager
from FrameworkLevel.utilities.InstanceWebElement import InstanceWebElement
from FrameworkLevel.utilities.Common import Common
from AutomationTestLevel.locators.UIMasterPage import UIMasterPage
from AutomationTestLevel.locators.UILoginPage import UILoginPage
import time
class LoginPage:
    def __init__(self):
        self.driver = Common.driver 
    # def loc_ele_btnLogin(self):
    #     self.loc_ele_btnLogin = InstanceWebElement(self.driver,UIMasterPage.loc_ele_btnLogin)
    #     return self.loc_ele_btnLogin
    #
    # def loc_ele_profileIconUser(self,data):
    #     UILoginPage.loc_ele_profileIconUser[-1]=UILoginPage.loc_ele_profileIconUser[-1].format(data)
    #     self.loc_ele_profileIconUser=InstanceWebElement(self.driver,UILoginPage.loc_ele_profileIconUser)
    #     return self.loc_ele_profileIconUser

        
