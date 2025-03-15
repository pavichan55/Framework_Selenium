from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

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

    # def drpdwCountry(self):
    #     self.drpdwCountry = InstanceWebElement(self.driver,UIDashboardPage.drpdwCountry)
    #     return self.drpdwCountry
    # def txtName(self):
    #     self.txtName = InstanceWebElement(self.driver,UIDashboardPage.txtName)
    #     return self.txtName


    def launchApp(self):

        # self.driver.find_element(By.ID, "android:id/text1").Click()
        self.driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='android:id/text1']").click()
        # self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Angola")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("India"))').click()


        self.driver.find_element(By.XPATH,
                            "//android.widget.EditText[@resource-id='com.androidsample.generalstore:id/nameField']").send_keys(
            'AppiumAutomation')
        # Lets shop element
        # self.driver.find_element(By.XPATH,"//android.widget.Button[@resource-id='com.androidsample.generalstore:id/btnLetsShop']").click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().resourceId("com.androidsample.generalstore:id/btnLetsShop")').click()
        # text = self.driver.find_element(By.XPATH,'(//android.widget.Toast)[1]').get_attribute('text')
        # print(text)
        # self.driver.execute_script("mobile:scrollGesture", {"direction": "down", "percent": 1.0 })

        self.driver.execute_script("mobile: scrollGesture", {
            "left": 100,  # X-coordinate of scroll area
            "top": 500,  # Y-coordinate of scroll area
            "width": 300,  # Width of scroll area
            "height": 600,  # Height of scroll area
            "direction": "down",
            "percent": 1.0
        })

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Jordan 6 Rings"))')

        # products = self.driver.find_elements(By.ID, "com.androidsample.generalstore:id/productName")


        # for name in products:
        #     if name.get_attribute('text') == 'Jordan 6 Rings':
        #         self.driver.find_element(By.XPATH,
        #                             '(//android.widget.TextView[@resource-id="com.androidsample.generalstore:id/productAddCart"])[2]').click()
        #
        # self.driver.find_element(By.XPATH,
        #                     '//android.widget.ImageButton[@resource-id="com.androidsample.generalstore:id/appbar_btn_cart"]').click()


    