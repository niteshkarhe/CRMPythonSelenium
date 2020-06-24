'''
Created on Mar 25, 2020

@author: Nitesh
'''
import traceback, time
from abc import ABC, ABCMeta, abstractmethod
from PyTestFramework.crmpro_automation.utilities.jsexecutor import JsExecutorMethods
from PyTestFramework.crmpro_automation.utilities.wrapperactions import ClickActions

class HeaderInterface(metaclass=ABCMeta):
    
    def click_new_button(self):
        flag=True
        try:
            self.new_btn_xpath="//button[text()='New']"
            ClickActions().click_element('xpath', self.new_btn_xpath)
            #JsExecutorMethods.js_click('xpath', self.new_btn_xpath)
        except:
            flag=False
            self.log.error('Element with locator ['+self.new_btn_xpath+'] and locatortype [xpath] is not clicked.')
            print(traceback.format_exc())
        return flag
    
    @abstractmethod
    def click_export_button(self):
        '''Not implemented. To be implemented in respective abstract class'''
        raise NotImplementedError
        
    @abstractmethod
    def click_showfilters_button(self):
        '''Not implemented. To be implemented in respective abstract class'''
        raise NotImplementedError
    
    @abstractmethod
    def click_cancel_button(self):
        '''Not implemented. To be implemented in respective abstract class'''
        raise NotImplementedError
    
    @abstractmethod
    def click_save_button(self):
        '''Not implemented. To be implemented in respective abstract class'''
        raise NotImplementedError