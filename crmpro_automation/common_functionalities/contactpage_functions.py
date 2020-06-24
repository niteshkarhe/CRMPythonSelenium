'''
Created on Mar 25, 2020

@author: Nitesh
'''
import time
from PyTestFramework.crmpro_automation.abstract_modules.contactpage_abs import ContactPageAbs
from PyTestFramework.crmpro_automation.pages.base_fixture import BaseFixture
from PyTestFramework.crmpro_automation.utilities.wrapperactions import ClickActions, InputActions, SelectActions
from PyTestFramework.crmpro_automation.utilities.jsexecutor import JsExecutorMethods
from PyTestFramework.crmpro_automation.pages.createnewcontacts_page import CreateNewContactPage

class ContactPageFunctions(BaseFixture, ContactPageAbs):
    
    def __init__(self, config):
        #Locators
        self.contactspg_label_xpath=config['Locators']['contactspg_label_xpath']
        self.showfilters_btn_xpath=config['Locators']['showfilters_btn_xpath']
        self.export_btn_xpath=config['Locators']['export_btn_xpath']
        self.click_actions=ClickActions()
        self.input_actions=InputActions()
        self.select_actions=SelectActions()
        

    def click_contactpg_new_button(self):
        flag=self.click_new_button()
        if flag==True:
            self.log.info('New Button is clicked')
        elif flag==False:
            self.log.info('New Button is not clicked')
        time.sleep(2)
        return CreateNewContactPage()
        
    def click_export_button(self):
        flag=self.click_actions.click_element('xpath', self.export_btn_xpath)
        if flag==True:
            self.log.info('Export Button is clicked')
        elif flag==False:
            self.log.info('Export Button is not clicked')
            
    def click_showfilters_button(self):
        flag=self.click_actions.click_element('xpath', self.showfilters_btn_xpath)
        if flag==True:
            self.log.info('Show filters Button is clicked')
        elif flag==False:
            self.log.info('Show filters Button is not clicked')