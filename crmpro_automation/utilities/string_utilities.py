'''
Created on Mar 24, 2020

@author: Nitesh
'''
from PyTestFramework.crmpro_automation.pages.base_fixture import BaseFixture

class StringUtility(BaseFixture):
    
    def string_contains(self, string1, string2):
        return string2 in string1
    