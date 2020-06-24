'''
Created on Mar 25, 2020

@author: Nitesh
'''
from abc import ABC, abstractmethod
from PyTestFramework.crmpro_automation.abstract_modules.header_adapter import HeaderAdapterClass

class ContactPageAbs(ABC, HeaderAdapterClass):
    
    @abstractmethod
    def click_export_button(self):
        '''Not implemented. To be implemented in respective abstract class'''
        raise NotImplementedError
     
    @abstractmethod   
    def click_showfilters_button(self):
        '''Not implemented. To be implemented in respective abstract class'''
        raise NotImplementedError
