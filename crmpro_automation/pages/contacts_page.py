'''
Created on Mar 25, 2020

@author: Nitesh
'''
import os
from PyTestFramework.crmpro_automation.pages.base_fixture import BaseFixture
from PyTestFramework.crmpro_automation.filereader.config_reader import ConfigReader
from PyTestFramework.crmpro_automation.utilities.string_utilities import StringUtility
from PyTestFramework.crmpro_automation.utilities.wrapperactions import ClickActions, InputActions, SelectActions
from PyTestFramework.crmpro_automation.common_functionalities.contactpage_functions import ContactPageFunctions

class ContactsPage(ContactPageFunctions):
    
    def __init__(self):
        cur_dir_path=os.path.dirname(os.path.realpath(__file__))
        objectrepo_path=cur_dir_path.split(sep="\\pages")[0]+"\\objectrepository\\contactspage_object.ini"
        config=ConfigReader(objectrepo_path).get_config()
        super().__init__(config)
        #Locators
        
        #Data
        
    def is_contactspage_displayed(self):
        self.is_page_ready('Contacts Page')
        flag=self.get_webelement('xpath', self.contact_activity_stream_label_xpath).is_displayed()
        if flag==True:
            self.log.info("Contacts page is displayed")