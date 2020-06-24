'''
Created on Mar 16, 2020

@author: Nitesh
'''
import os
from PyTestFramework.crmpro_automation.pages.base_fixture import BaseFixture
from PyTestFramework.crmpro_automation.filereader.config_reader import ConfigReader
from PyTestFramework.crmpro_automation.utilities.string_utilities import StringUtility
from PyTestFramework.crmpro_automation.utilities.wrapperactions import ClickActions, InputActions, SelectActions
from PyTestFramework.crmpro_automation.common_functionalities.homepage_functions import HomePageFunctions
from PyTestFramework.crmpro_automation.pages.contacts_page import ContactsPage

class HomePage(BaseFixture):
    
    def __init__(self):
        cur_dir_path=os.path.dirname(os.path.realpath(__file__))
        objectrepo_path=cur_dir_path.split(sep="\\pages")[0]+"\\objectrepository\\homepage_object.ini"
        config=ConfigReader(objectrepo_path).get_config()
        self.click_actions = ClickActions()
        self.input_actions = InputActions()
        self.string_utility = StringUtility()
        self.homepg_func = HomePageFunctions(config)
        
        #Locators
        self.contact_activity_stream_label_xpath=config["Locators"]["contact_activity_stream_label_xpath"]
        self.home_menu_css=config['Locators']['home_menu_css']
        self.contact_css=config['Locators']['contact_menu_css']
        
        #Data
        self.home_url=config['Data']['url_string']
        
    def is_homepage_displayed(self):
        self.is_page_ready('Home Page')
        flag=self.get_webelement('xpath', self.contact_activity_stream_label_xpath).is_displayed()
        if flag==True:
            self.log.info("Home page is displayed")
            
    def goto_contacts_page(self):
        flag=self.click_actions.click_element('css', self.contact_css)
        if flag==True:
            self.log.info('Contact menu link is clicked')
        return ContactsPage()