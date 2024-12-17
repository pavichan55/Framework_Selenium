from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
import os
import time

from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import config
import ctypes


class Common():
    PATH_DRIVER_LOCATION = os.path.abspath(".//FrameworkLevel//ApplicationData")
    
    driver = ""
    @classmethod
    def getDriver(cls):
        if config.headlessmode:
            resolution = ctypes.windll.user32
            screensize = resolution.GetSystemMetrics(0),resolution.GetSystemMetrics(1)
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument(f"--window-size={screensize[0]}x{screensize[1]}")
            # driver = webdriver.Chrome(Common.PATH_DRIVER_LOCATION+"/chromedriver.exe",chrome_options=chrome_options)
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
            driver.maximize_window()
            Common.driver =driver

            return driver
        else:
            # driver = webdriver.Chrome(Common.PATH_DRIVER_LOCATION+"/chromedriver.exe")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
            driver.maximize_window()
            Common.driver =driver
            return driver
