import subprocess
import time
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.ie.service import Service
import config
import ctypes


class Common():
    driver = ""
    appium_service = AppiumService()


    @classmethod
    def getDriver(cls):
        if config.execution_mode == 'android':
            # Start Appium service if not running

            if not cls.appium_service.is_running:
                cls.appium_service.start(args=['--address', '127.0.0.1', '--port', '4723'])

            if config.browser == 'AndroidChrome':
                desired_cap = {
                    "deviceName": "emulator-5554",
                    "browserName": "Chrome",
                    "platformName": "Android",
                    "automationName": "UiAutomator2",
                    "chromeOptions": {"w3c": True}
                }
                capabilities = UiAutomator2Options().load_capabilities(desired_cap)
                driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=capabilities)

            else:
                options = AppiumOptions()
                options.load_capabilities({
                    "appium:app": "C:\\Users\\ADMIN\\PycharmProjects\\Appium\\General-Store.apk",
                    "appium:automationName": "UiAutomator2",
                    "platformName": "Android",
                    "appium:deviceName": "emulator-5554",
                    "appium:appPackage": "com.androidsample.generalstore",
                    "appium:appActivity": "com.androidsample.generalstore.SplashActivity",
                    "appium:autoGrantPermissions": True,
                    "appium:noReset": True
                })
                driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

        elif config.execution_mode == "docker":
            try:
                result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
                if "selenium-hub" not in result.stdout:
                    print("Starting Selenium Grid using Docker Compose")
                    subprocess.run(["docker-compose", "up", "-d"], check=True)
                    time.sleep(5)
                driver = webdriver.Remote(command_executor=config.docker_port,
                                          options=webdriver.ChromeOptions())
            except Exception as e:
                print(f"Error starting Selenium Grid: {e}")

        elif config.execution_mode == "local":
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)

        Common.driver = driver
        return driver
