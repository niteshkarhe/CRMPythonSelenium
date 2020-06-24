'''
Created on Mar 25, 2020

@author: Nitesh
'''
from abc import ABC
from PyTestFramework.crmpro_automation.abstract_modules.header_adapter import HeaderAdapterClass

class HomePageAbs(ABC, HeaderAdapterClass):
    
    def click_export_button(self): pass
    def click_showfilters_button(self): pass