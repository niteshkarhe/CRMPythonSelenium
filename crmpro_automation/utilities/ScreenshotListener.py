'''
Created on Jun 21, 2020

@author: Nitesh
'''

from selenium.webdriver.support.events import AbstractEventListener
from PyTestFramework.crmpro_automation.pages.base_fixture import BaseFixture

class EventListener(AbstractEventListener):
    pass
#     def on_exception(self, exception, driver):
#         BaseFixture().screenshot(False, "This is failure")
