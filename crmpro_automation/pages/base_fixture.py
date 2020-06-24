'''
Created on Mar 16, 2020

@author: Nitesh
'''
import traceback, os, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PyTestFramework.crmpro_automation.utilities.custom_logger import Logger
from PyTestFramework.crmpro_automation.configfiles.manage_report import ManageReport

class BaseFixture():
    
    report = Logger.report()
    report_path=report+"/report.html"
    asset_path=report+"/assets"
    #screenshot_dir=report
    
    log = Logger().customLogger(report)
    driver=None
    testdata={}
    
    @classmethod  
    def driver_setup(cls, driver):
        cls.driver=driver
    
    @classmethod
    def report_folder_file_path(cls):
        return (cls.report_path, cls.asset_path)
    
    @classmethod
    def testdata_setup(cls, testdata_dict):
        cls.testdata=testdata_dict
        
    def refresh_pg(self):
        self.driver.refresh()
        
    def get_title(self):
        return self.driver.title

    def clear_field(self, locatortype, locator):
        self.get_webelement(locatortype, locator).clear()

    def clear_element_field(self, element):
        element.clear()
        
    def get_current_url(self):
        return self.driver.current_url
     
    @classmethod
    def get_by_type(cls, locatorType):
        try:
            cls.locatortype=locatorType.lower()
            if cls.locatortype=='id':
                return By.ID
            elif cls.locatortype=='name':
                return By.NAME
            elif cls.locatortype=='xpath':
                return By.XPATH
            elif cls.locatortype=='css':
                return By.CSS_SELECTOR
            elif cls.locatortype=='classname':
                return By.CLASS_NAME
            elif cls.locatortype=='linktext':
                return By.LINK_TEXT
            elif cls.locatortype=='partiallinktext':
                return By.PARTIAL_LINK_TEXT
            elif cls.locatortype=='tagname':
                return By.TAG_NAME
            else:
                cls.log.info('Locator type',locatorType,'not correct/supported')
            return False
        except:
            print(traceback.format_exc())
            
    def screenshot(self, result, failureMsg):
        if result == False:
            file_name = failureMsg + '-' + str(round(time.time() * 1000)) + '.png'
            screenshot_dir = "../screenshots/"
            relativefilename = screenshot_dir + file_name
            current_dir = os.path.dirname(__file__)
            destination_filename = os.path.join(current_dir, relativefilename)
            destination_dir = os.path.join(current_dir, screenshot_dir)
        try:
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            self.driver.save_screenshot(destination_filename)
            self.log.info("Screenshot save to directory:"+destination_filename)
        except:
            self.log.error("### Exception occured in screenshot")
            print(traceback.format_exc())
     
    @classmethod       
    def get_webelement(cls,locatortype, locator):
        try:
            element=cls.driver.find_element(cls.get_by_type(locatortype), locator)
            return element
        except:
            cls.log.error('Element with locator ['+locator+'] and locatortype ['+locatortype+'] is not found. ')

    @classmethod
    def get_webelements(cls,locatortype, locator):
        try:
            elements=cls.driver.find_elements(cls.get_by_type(locatortype), locator)
            return elements
        except:
            cls.log.error('Element with locator ['+locator+'] and locatortype ['+locatortype+'] is not found. ')
            
    def is_page_ready(self, page_name):
        try:
            wait=WebDriverWait(self.driver, 30)
            wait.until(lambda driver: self.driver.execute_script('return document.readyState') == 'complete')
            self.log.info('Is '+page_name+' loaded?: '+self.driver.execute_script('return document.readyState'))
        except:
            print(traceback.print_exc())
            
    def is_dom_loaded(self):
        flag=True
        try:
            self.ui_ele_lst=self.get_webelements('xpath', '//body/div[@id="ui"]/div/div')
            while len(self.ui_ele_lst)<2:
                self.refresh_pg()
                time.sleep(1)
                self.ui_ele_lst=self.get_webelements('xpath', '//body/div[@id="ui"]/div/div')
                self.is_dom_loaded()
        except:
            flag=False
            print(traceback.print_exc())
        return flag