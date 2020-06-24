'''
Created on Mar 25, 2020

@author: Nitesh
'''
from abc import ABC, abstractmethod
from PyTestFramework.crmpro_automation.abstract_modules.header_adapter import HeaderAdapterClass

class CreateNewContactsPageAbs(ABC, HeaderAdapterClass):
    
    @abstractmethod
    def click_save_button(self):
        '''Not implemented. To be implemented in respective abstract class'''
        raise NotImplementedError
    
    
    @abstractmethod
    def click_cancel_button(self):
        '''Not implemented. To be implemented in respective abstract class'''
        raise NotImplementedError
