'''
Created on Mar 16, 2020

@author: Nitesh
'''
import os
from PyTestFramework.crmpro_automation.pages.base_fixture import BaseFixture
from PyTestFramework.crmpro_automation.filereader.config_reader import ConfigReader
from PyTestFramework.crmpro_automation.utilities.wrapperactions import ClickActions, InputActions, SelectActions, HandleIFrame
from PyTestFramework.crmpro_automation.pages.home_page import HomePage

class LoginPage(BaseFixture):
    
    def __init__(self):
        #print('driver in LoginPage: ', driver)
        cur_dir_path=os.path.dirname(os.path.realpath(__file__))
        objectrepo_path=cur_dir_path.split(sep="\\pages")[0]+"\\objectrepository\\loginpage_object.ini"
        config=ConfigReader(objectrepo_path).get_config()
        self.click_actions = ClickActions()
        self.input_actions = InputActions()
        self.handle_frame = HandleIFrame()
        
        #Locators
        self.email_name=config['Locators']['email_inpbox_name']
        self.pwd_name=config['Locators']['pwd_inpbox_name']
        self.login_btn_xpath=config['Locators']['login_btn_xpath']
        self.classic_crm_label_xpath=config['Locators']['classic_crm_label_xpath']
        
        #Data
        self.username=config['Data']['invalid_uname']
        self.password=config['Data']['invalid_pwd']
        
     
    def print_locators(self):
        print(self.email_name, self.pwd_name, self.login_btn_xpath)
        
    def is_loginpage_displayed(self):
        self.is_page_ready('Login Page')
        flag=self.get_webelement('xpath', self.classic_crm_label_xpath).is_displayed()
        if flag==True:
            self.log.info("Login page is displayed")
            
    def enter_username(self):
        flag=self.input_actions.enter_text('name', self.email_name, self.username)
        if flag==True:
            self.log.info('Username is entered')
        elif flag==False:
            self.log.error('Username is not entered due to error in finding username field')
            
    def enter_password(self):
        flag=self.input_actions.enter_text('name', self.pwd_name, self.password)
        if flag==True:
            self.log.info('Password is entered')
        elif flag==False:
            self.log.error('Password is not entered due to error in finding password field')
            
    def click_login_btn(self):
        flag=self.click_actions.click_element('xpath', self.login_btn_xpath)
        if flag==True:
            self.log.info('Login button is clicked')
        elif flag==False:
            self.log.error('Login button is not clicked due to issue in finding login button element')
        
    def login(self):
        self.is_loginpage_displayed()
        self.enter_username()
        self.enter_password()
        self.click_login_btn()
        return HomePage()
    
    def toolsqa(self):
        self.log.info('Tools QA Frame page opened')
        self.handle_frame.switch_to_frame_id('IF1')
        title_text=self.get_webelement('id', 'site-description').text   
        print(title_text)
        self.log.info('title_text: '+title_text)
                  
# o=LoginPage("driver")
# o.print_locators()