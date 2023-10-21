from PyTestFramework.crmpro_automation.base.drivermanager import DriverManager

import os
import traceback
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from PyTestFramework.crmpro_automation.utilities.ScreenshotListener import EventListener
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PyTestFramework.crmpro_automation.filereader.qe_environment import QEEnvironment

class ChromeDriverManager(DriverManager):
    __chservice=None
    
    def launch_browser(self):
        chrome_option = Options()
        chrome_option.add_argument("--disable-infobars")
        chrome_option.add_argument("--start-maximized")
        chrome_option.add_argument("--disable-popup-blocking")
        cur_dir_path = os.path.dirname(os.path.realpath(__file__))
        chromedriver = cur_dir_path.split(sep='\\base')[0]+QEEnvironment.get_environment_dict().get('BrowserPath')
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chromedriver, options = chrome_option)
        driver.get('https://ui.cogmento.com/')
    
    def start_service(self):
        try:
            if self.__chservice==None:
                cur_dir_path = os.path.dirname(os.path.realpath(__file__))
                driver_path=cur_dir_path.split(sep='\\base')[0]+QEEnvironment.get_environment_dict().get('BrowserPath')
                self.__chservice=Service(driver_path)
                self.__chservice.start()
                print('Service is started')
        except:
            print(traceback.print_exc())
    
    def stop_service(self):
        if self.__chservice!=None and self.__chservice.is_connectable():
            print('Stop service')
            self.__chservice.stop()
    
    def create_driver(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--disable-infobars")
        chrome_option.add_argument("--start-maximized")
        chrome_option.add_argument("--disable-popup-blocking")
        #capabilities = DesiredCapabilities.CHROME.copy()
        #capabilities['browser']='chrome'
        #capabilities=chrome_option.to_capabilities()
        self.driver=webdriver.Chrome(options = chrome_option)
        self.edriver = EventFiringWebDriver(self.driver, EventListener())
        self.edriver.implicitly_wait(QEEnvironment.get_environment_dict().get('ImplicitWait'))
        self.edriver.get(QEEnvironment.get_environment_dict().get('URL'))
        
#o=ChromeDriverManager()
# o.start_service()
# o.create_driver()
# o.stop_service()
#o.get_driver()
#o.stop_service()
