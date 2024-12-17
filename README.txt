Owner : Pavithran
Development Phase Started: Sept 6th 2021
Features:
1) Reusability
2) Easy to arrange testflow repeated flow testing
3) Can create Multiple Packages example Venio_fr,Venio_en
4) TestFlow and TestData is with respect to package
5) Pandas module is used overall and whole framework works on Runtime data and testflow. Only during trigger runtime data from testdata and testflow will be retrived for the test cases which we want to execute for 
certain testcases enabled as Yes in ExecutionController
6) StaticData.prop is created for each package  (Venio_fr,Venio_en) Basically StatiData.prop file is used for validating error message
7) Config file feature
	-Different testsuites can be created for different packages. 
	-Browser teardown control
	-FunctionRepo control (requireS when add new methods in POM)
	-Browser control (Open and Close after each execution)
	-headless mode (ENABLE /dISABLE)
	-DynameRuntimeDatastorage
	-DynamicDataManager 
	-Explicit wait handlers implemented for Click,EnterText,isDisplayed,isElementPresent,ClickJS
8) Locators - Defining all element identifier accordingly. Dynamix Xpath Implementation using format
9) POM model for defining reusable methods
10) MethodDictionary repo is keyword framework


Yet to be done
-Exception handling as per requirement
-Logging
-InstanceWebElement.py few more selenium modified methods needs to be added
-Report generation (HTML report or Allure report) can be implemented to get Full Page screenshot when in headless mode
-Log Generation
-As of now built for chrome, further can be integrated to handle other browsers
-Parallel execution (multiprocessor module)
-According to requirement we can create dummy file for unstructured data import

