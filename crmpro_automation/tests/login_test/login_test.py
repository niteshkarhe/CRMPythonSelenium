'''
Created on Mar 14, 2020
@author: Nitesh
'''
import pytest
import unittest
from PyTestFramework.crmpro_automation.filereader.qe_environment import QEEnvironment
from PyTestFramework.crmpro_automation.pages.base_fixture import BaseFixture
from PyTestFramework.crmpro_automation.pages.login_page import LoginPage
from PyTestFramework.crmpro_automation.filereader.excel_reader import ExcelReader
from PyTestFramework.crmpro_automation.filereader.excel_datareader import ExcelDataReader
from parameterized import parameterized

@pytest.mark.usefixtures("setUp")
class TestLogin():
    __driver=None
    __environment_dict={}

    def get_excel_data(testname):
        return ExcelReader('contact_pg_testdata', "Sheet2", testname).get_test_data()

    @pytest.fixture(autouse=True)
    def login(self, setUp):
        #print('This is login method')
        QEEnvironment.set_environment_dict(self.environment)
        #self.__driver=self.driver.get_driver()
        BaseFixture.driver_setup(self.driver.get_driver())

    @pytest.mark.parametrize("row", ExcelReader('contact_pg_testdata', "Sheet2", 'Verify User is able to login and save Contact Info').get_test_data())
    def test_login(self, row):
        BaseFixture.log.info('#### Verify User is able to login and save Contact Info ####')
        #BaseFixture.testdata_setup(ExcelReader('contact_pg_testdata', "Sheet1", 'Verify User is able to login and save Contact Info').get_test_data())
        BaseFixture.testdata_setup(row)

        login=LoginPage()
        home_page=login.login()
        home_page.is_homepage_displayed()
        contact_page=home_page.goto_contacts_page()
        createnewcontact_page=contact_page.click_contactpg_new_button()
        createnewcontact_page.is_contact_new_page_displayed()
        createnewcontact_page.fill_form()
        createnewcontact_page.click_save_button()

    @pytest.mark.skip(reason="Temporay disabled") 
    def test_one_login(self):
        BaseFixture.log.info('#### This Test case assert fail ####')
        login=LoginPage()
        login.login()
        assert 1==1
    
    @pytest.mark.skip(reason="Temporay disabled") 
    def test_two_login(self):
        BaseFixture.log.info('#### This Test case will fail due to missing toolsqa page ####')
        login=LoginPage()
        login.toolsqa()
        assert 1==1