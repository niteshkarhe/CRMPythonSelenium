import traceback
from PyTestFramework.crmpro_automation.base.browserdriver import BrowserDriver
from PyTestFramework.crmpro_automation.base.chromedrivermanager import ChromeDriverManager
from PyTestFramework.crmpro_automation.base.firefoxdrivermanager import FirefoxDriverManager

class DriverManagerFactory:
    __chrome_driver=None
    __firefox_driver=None
    
    @classmethod
    def get_manager(cls, browser_type):
        if(browser_type==BrowserDriver.CHROME.name):
            if cls.__chrome_driver==None:
                cls.__chrome_driver=ChromeDriverManager()
                return cls.__chrome_driver
            else:
                return cls.__chrome_driver
        elif(browser_type==BrowserDriver.FIREFOX.name):
            if cls.__firefox_driver==None:
                cls.__firefox_driver=FirefoxDriverManager()
                return cls.__firefox_driver
            else:
                return cls.__firefox_driver
        else:
            print('Browser name is not correctly given in ExecutionConfig.xml. Note browsername should be in capital case.')
            raise 'Incorrect Browsername given in ExecutionConfig.xml'
        return None