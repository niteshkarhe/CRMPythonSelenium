'''
Created on Mar 25, 2020

@author: Nitesh
'''
import os, traceback, time
from PyTestFramework.crmpro_automation.pages.base_fixture import BaseFixture
from PyTestFramework.crmpro_automation.filereader.config_reader import ConfigReader
from PyTestFramework.crmpro_automation.utilities.wrapperactions import ClickActions, InputActions, SelectActions, ActionClass
from PyTestFramework.crmpro_automation.abstract_modules.createnewcontactspg_abs import CreateNewContactsPageAbs

class CreateNewContactPage(BaseFixture, CreateNewContactsPageAbs):
    
    def __init__(self):
        cur_dir_path=os.path.dirname(os.path.realpath(__file__))
        objectrepo_path=cur_dir_path.split(sep="\\pages")[0]+"\\objectrepository\\createnewcontacts_object.ini"
        config=ConfigReader(objectrepo_path).get_config()
        self.click_actions=ClickActions()
        self.input_actions=InputActions()
        self.select_actions=SelectActions()
        self.actions_obj=ActionClass()
        
        #Locators
        self.create_new_contacts_label_xpath=config['Locators']['create_new_contacts_label_xpath']
        self.save_btn_xpath=config['Locators']['save_btn_xpath']
        self.cancel_btn_xpath=config['Locators']['cancel_btn_xpath']
        self.firstname_name=config['Locators']['firstname_name']
        self.lastname_name=config['Locators']['lastname_name']
        self.middlename_name=config['Locators']['middlename_name']
        self.company_xpath=config['Locators']['company_xpath']
        self.tags_xpath=config['Locators']['tags_xpath']
        self.select_tag_xpath=config['Locators']['select_tag_xpath']
        self.email_label_xpath=config['Locators']['email_label_xpath']
        self.email_xpath=config['Locators']['email_xpath']
        self.category_dropdown_xpath=config['Locators']['category_dropdown_xpath']
        self.category_select_icon_xpath=config['Locators']['category_select_icon_xpath']
        self.category_label_xpath=config['Locators']['category_label_xpath']
        self.status_dropdown_xpath=config['Locators']['status_dropdown_xpath']
        self.status_select_icon_xpath=config['Locators']['status_select_icon_xpath']
        self.birthday_name=config['Locators']['birthday_name']
        self.birthmonth_dropdown_xpath=config['Locators']['birthmonth_dropdown_xpath']
        self.birthmonth_dropdown_icon_xpath=config['Locators']['birthmonth_dropdown_icon_xpath']
        self.birthyear_name=config['Locators']['birthyear_name']
        
        #data
        self.fname=self.testdata['FirstName']
        self.lname=self.testdata['LastName']
        self.middlename=self.testdata['MiddleName']
        self.company=self.testdata['Company']
        self.tags=self.testdata['Tags']
        self.email=self.testdata['Email']
        self.category=self.testdata['Category']
        self.status=self.testdata['Status']
        self.bdate=self.testdata['Bdate']
        self.bmonth=self.testdata['Bmonth']
        self.byear=self.testdata['Byear']
        
    def is_contact_new_page_displayed(self):
        self.is_page_ready('Create New Contacts Page')
        pg_display_flag=self.is_dom_loaded()
        flag=self.get_webelement('xpath', self.create_new_contacts_label_xpath).is_displayed()
        if flag==True and pg_display_flag==True:
            self.log.info("Create New Contacts is displayed")
        else:
            self.log.info("Create New Contacts is not displayed")
            
    def click_cancel_button(self):
        flag=self.click_actions.click_element('xpath', self.cancel_btn_xpath)
        if flag==True:
            self.log.info("Create New Contacts page Cancel button is clicked")
        elif flag==False:
            self.log.info("Create New Contacts page Cancel button is not clicked")
    
    def click_save_button(self):
        flag=self.click_actions.click_element('xpath', self.save_btn_xpath)
        if flag==True:
            self.log.info("Create New Contacts page Save button is clicked")
        elif flag==False:
            self.log.info("Create New Contacts page Save button is not clicked")
    
    def select_category(self, category_type):
        flag=True
        try:
            category_dropdown_lst=self.get_webelements('xpath', self.category_dropdown_xpath)
            for i in range(1, len(category_dropdown_lst)):
                category_div_xpath=self.category_dropdown_xpath+"["+str(i)+"]"
                category_text_xpath=category_div_xpath+"/span"
                category_text=self.get_webelement('xpath', category_text_xpath).text
                if category_text==category_type:
                    return self.click_actions.click_element('xpath', category_div_xpath)
                    break
        except Exception as e:
            flag=False
            self.log.error(e)
            print(traceback.print_exc())
        finally:
            return flag
        
    def select_tag(self, tag_type):
        flag=True
        try:
            self.input_actions.enter_text('xpath', self.tags_xpath, 'Persistent')
            time.sleep(3)
            self.actions_obj.move_and_click_same_element('xpath', self.select_tag_xpath)
            self.actions_obj.move_and_click_same_element('xpath', self.email_label_xpath)
            time.sleep(3)
        except Exception as e:
            flag=False
            self.log.error(e)
        return flag
    
    def select_status(self, status):
        flag=True
        try:
            status_dropdown_lst=self.get_webelements('xpath', self.status_dropdown_xpath)
            for i in range(1, len(status_dropdown_lst)):
                status_dropdown_xpath=self.status_dropdown_xpath+"["+str(i)+"]"
                status_text_xpath=status_dropdown_xpath+"/span"
                status_text=self.get_webelement('xpath', status_text_xpath).text
                if status_text==status:
                    return self.click_actions.click_element('xpath', status_dropdown_xpath)
                    break
        except Exception as e:
            flag=False
            self.log.error(e)
            print(traceback.print_exc())
        finally:
            return flag
        
    def select_birthmonth(self, birth_month):
        flag=True
        try:
            birth_dropdown_lst=self.get_webelements('xpath', self.birthmonth_dropdown_xpath)
            for i in range(1, len(birth_dropdown_lst)):
                birthmonth_dropdown_xpath=self.birthmonth_dropdown_xpath+"["+str(i)+"]"
                birthmonth_text_xpath=birthmonth_dropdown_xpath+"/span"
                birthmonth_text=self.get_webelement('xpath', birthmonth_text_xpath).text
                if birthmonth_text==birth_month:
                    return self.click_actions.click_element('xpath', birthmonth_dropdown_xpath)
                    break
        except Exception as e:
            flag=False
            self.log.error(e)
            print(traceback.print_exc())
        finally:
            return flag
            
    def fill_form(self):
        collective_flags={}
        self.key_lst=[]
        flag=True
        try:
            collective_flags['firstname_input']=self.input_actions.enter_text('name', self.firstname_name, self.fname)
            collective_flags['lastname_input']=self.input_actions.enter_text('name', self.lastname_name, self.lname)
            collective_flags['middlename_input']=self.input_actions.enter_text('name', self.middlename_name, self.middlename)
            collective_flags['company_input']=self.input_actions.enter_text('xpath', self.company_xpath, self.company)
            collective_flags['tags_input']=self.select_tag(self.tags)
            collective_flags['email_input']=self.input_actions.enter_text('xpath', self.email_xpath, self.email)
            self.actions_obj.move_and_click_same_element('xpath', self.category_select_icon_xpath)
            collective_flags['category_input']=self.select_category(self.category)
            self.actions_obj.move_and_click_same_element('xpath', self.status_select_icon_xpath)
            collective_flags['status_input']=self.select_status(self.status)
            collective_flags['birthday_input']=self.input_actions.enter_text_by_scrolling('name', self.birthday_name, self.bdate)
            self.actions_obj.move_and_click_same_element('xpath', self.birthmonth_dropdown_icon_xpath)
            collective_flags['birthmonth_input']=self.select_birthmonth(self.bmonth)
            collective_flags['birthyear_input']=self.input_actions.enter_text_by_scrolling('name', self.birthyear_name, self.byear)
            
            if False in collective_flags.values():
                flag=False
                for key in collective_flags.keys():
                    if collective_flags[key]==False:
                        self.key_lst.append(key)
                for item in self.key_lst:
                    self.log.error('Value is not entered/ selected for field: '+str(item))
                self.log.error('Form is not filled due to above issues')
                
            if flag==True:
                for key in collective_flags.keys():
                    if collective_flags[key]==True:
                        self.log.info('Value is entered/ selected for field: '+str(key))
                self.log.info('Form is filled completely')
        except:
            print(traceback.print_exc())