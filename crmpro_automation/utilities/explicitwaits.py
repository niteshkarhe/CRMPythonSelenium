'''
Created on Mar 24, 2020

@author: Nitesh
'''
import traceback
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyTestFramework.crmpro_automation.pages.base_fixture import BaseFixture

class ExplicitWaits(BaseFixture):
    
    @staticmethod
    def visibility_of_element_located_by(locatortype, locator):
        try:
            wait = WebDriverWait(BaseFixture.driver, 10)
            wait.until(EC.visibility_of_element_located(BaseFixture.get_by_type(locatortype), locator))
            BaseFixture.log.info('Element with locator [' + locator + '] and locatortype [' + locatortype + '] is found.')
        except:
            BaseFixture.log.error('Element with locator [' + locator + '] and locatortype [' + locatortype + '] is not found.')
            print(traceback.print_exc())

    @staticmethod
    def presence_of_element(locatortype, locator):
        try:
            wait = WebDriverWait(BaseFixture.driver, 10)
            wait.until(EC.presence_of_element_located((BaseFixture.get_by_type(locatortype), locator)))
        except:
            print(traceback.print_exc())

    @staticmethod
    def element_to_be_clickable(locatortype, locator):
        try:
            wait = WebDriverWait(BaseFixture.driver, 10)
            wait.until(EC.element_to_be_clickable((BaseFixture.get_by_type(locatortype), locator)))
        except:
            print(traceback.print_exc())

    @staticmethod
    def element_selection_state_to_be(locatortype, locator):
        try:
            wait = WebDriverWait(BaseFixture.driver, 10)
            element = BaseFixture.get_webelement(locatortype, locator)
            wait.until(EC.element_selection_state_to_be(element, True))
        except:
            print(traceback.print_exc())

    @staticmethod
    def element_to_be_selected(locatortype, locator):
        try:
            wait = WebDriverWait(BaseFixture.driver, 10)
            element = BaseFixture.get_webelement(locatortype, locator)
            wait.until(EC.element_to_be_selected(element))
        except:
            print(traceback.print_exc())

    @staticmethod
    def title_is(titleValue):
        try:
            wait = WebDriverWait(BaseFixture.driver, 10)
            wait.until(EC.title_is(titleValue))
        except:
            print(traceback.print_exc())

    @staticmethod
    def text_to_be_present_element(locatortype, locator, text):
        try:
            wait = WebDriverWait(BaseFixture.driver, 30)
            wait.until(EC.presence_of_element_located((BaseFixture.get_by_type(locatortype), locator)))
            wait.until(EC.visibility_of_element_located((BaseFixture.get_by_type(locatortype), locator)))
            wait.until(EC.text_to_be_present_in_element((BaseFixture.get_by_type(locatortype), locator), text))
        except:
            print(traceback.print_exc())