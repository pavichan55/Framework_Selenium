from FrameworkLevel.utilities.StaticdataManager import StaticdataManager
from FrameworkLevel.utilities.InstanceWebElement import InstanceWebElement
from FrameworkLevel.utilities.Common import Common
from AutomationTestLevel.locators.UIMasterPage import UIMasterPage
import time
from selenium.webdriver.common.action_chains import ActionChains

class MasterPage:
    
    def __init__(self):
        self.driver = Common.driver

    # def loc_ele_btnSignin(self):
    #     self.loc_ele_btnSignin=InstanceWebElement(self.driver,UIMasterPage.loc_ele_btnSignin)
    #     return self.loc_ele_btnSignin
    def btnDoodle(self):
        self.btnDoodle = InstanceWebElement(self.driver,UIMasterPage.btnDoodle)
        return self.btnDoodle

    def btnGoogleLens(self):
        self.btnGoogleLens = InstanceWebElement(self.btnGoogleLens,UIMasterPage.btnGoogleLens)
        return self.btnGoogleLens
    
    # def loc_ele_profileIconUser(self,data):
    #     UILoginPage.loc_ele_profileIconUser[-1]=UILoginPage.loc_ele_profileIconUser[-1].format(data)
    #     self.loc_ele_profileIconUser=InstanceWebElement(self.driver,UILoginPage.loc_ele_profileIconUser)
    #     return self.loc_ele_profileIconUser

    def openApp(self):
        url = StaticdataManager.getData("url")
        self.driver.get(url)
        time.sleep(5)
        actualtitle = self.driver.title
        expectedTitle = StaticdataManager.getMethodLevelParamValue("Title")
        actions = ActionChains(self.driver)
        element = self.driver.find_element('xpath', "//div[@class='nDcEnd']")
        actions.move_to_element(element).perform()
        self.btnDoodle().ClickJS()
        self.driver.save_screenshot(str(int(time.time())) + ".png")

        if expectedTitle == actualtitle:
            print("Pass")
        else:
            print("Fail")

    def openBS(self):
        url = 'https://bstackdemo.com/'
        self.driver.get(url)
        time.sleep(5)
        