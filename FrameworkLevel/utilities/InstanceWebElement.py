from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InstanceWebElement:
    __locatorelement = None
    
    def __init__(self,driverInstance,elementIdentifier,*argue):
        self.__driver = driverInstance
        self.__locator = elementIdentifier
        
    def Click(self):
        try:
            clickvariable  = WebDriverWait(self.__driver,17).until(EC.element_to_be_clickable(self.__locator))
            clickvariable.click()
        except Exception as e:
            print("Element is not clickable ",e)
            
    def EnterText(self,arguText):
        try:
            entertextvariable = WebDriverWait(self.__driver,17).until(EC.presence_of_element_located(self.__locator))
            entertextvariable.clear()
            entertextvariable.send_keys(arguText)
        except Exception as e:
            print("Input Field is not present",e)
            
    def isDisplayed(self):
        isDisplayedvariable=False
        try:
            isDisplayedvariable = WebDriverWait(self.__driver,17).until(EC.visibility_of_element_located(self.__locator),"False")
        except Exception as e:
            print("Element is not displayed",e)
        if isDisplayedvariable == "False":
            return False
        return isDisplayedvariable
            
    def isElementPresent(self):
        isElementPresentVariable=False
        try:
            isElementPresentVariable=WebDriverWait(self.__driver,17).until(EC.presence_of_element_located(self.__locator),"False")
        except Exception as e:
            print("Element Not Present",e)
        if isElementPresentVariable=="False":
            return False
        return True
    
    def ClickJS(self):
        try:
            isclickjsvariable = WebDriverWait(self.__driver,17).until(EC.element_to_be_clickable(self.__locator))
            self.__driver.execute_script("arguments[0].click()",isclickjsvariable)
        except Exception as e:
            print("Element is not clickable",e)
            