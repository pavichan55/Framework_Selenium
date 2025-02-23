import subprocess

import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.ie.service import Service
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
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
            # '''    Docker Configuration   '''
            # SELENIUM_GRID_URL = "http://localhost:4444/wd/hub"
            # capabilities = DesiredCapabilities.CHROME.copy()
            # driver = webdriver.Remote(
            #     command_executor=SELENIUM_GRID_URL,
            #     desired_capabilities=capabilities
            # )
            driver.maximize_window()
            Common.driver =driver
            return driver
        else:
            if config.execution_mode == "docker":
                try:

                    result = subprocess.run("docker ps | grep selenium-hub", shell=True, capture_output=True, text=True)

                    if "selenium-hub" not in result.stdout:
                        print("Starting Selenium Grid using Docker Compose")
                        subprocess.run("docker-compose up -d", shell=True, check=True)
                        time.sleep(5)
                    else:
                        print("Selenium Grid is already running.")

                    driver = webdriver.Remote(command_executor=config.docker_port,
                                              options=webdriver.ChromeOptions())

                except Exception as e:
                    print(f"Error starting Selenium Grid: {e}")


            elif config.execution_mode == "local":
                # driver = webdriver.Chrome(Common.PATH_DRIVER_LOCATION+"/chromedriver.exe")
                service = Service(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=service)


            driver.maximize_window()
            Common.driver =driver
            return driver
