'''
Created on Mar 14, 2020

@author: Nitesh
'''

import configparser
import traceback

class ConfigReader:
    __property_file_path="configfiles//application_config.ini"
    __config = configparser.ConfigParser()
    
    def __init__(self, path):
        self.read_file_data(path)
    
    def read_file_data(self, path):
        try:
            self.__config.read(path)
        except:
            print(traceback.print_exc())
            
    def get_config(self):
        return  self.__config