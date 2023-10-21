'''
Created on Mar 14, 2020

@author: Nitesh
'''

import os
import traceback

from PyTestFramework.crmpro_automation.filereader.xml_reader import XmlReader

class EnvironmentReader():
    
    __env_dict={}
    
    def __init__(self):
        self.read_file_data()
    
    def get_environment_dict(self):
        return self.__env_dict
    
    def read_file_data(self):
        cur_dir_path = os.path.dirname(os.path.realpath(__file__))
        xml_path=cur_dir_path.split(sep="\\filereader")[0]+"\\configfiles\\ExecutionConfig.xml"
        tree=XmlReader.parse_xml(xml_path)
        self.__env_dict=self.get_environment_list(tree)
    
    def get_environment_list(self, tree):
        env_dict={}
        try:
            root=tree.getroot()
            for node in root.findall('QAEnvironment'):
                if node.attrib.get('testingExecutionStatus')=='True':
                    env_dict['value']=node.attrib.get('value')
                    for child in node:
                        if child.tag=='BrowserName':
                            env_dict['BrowserName']=child.text
                        elif child.tag=='BrowserPath':
                            env_dict['BrowserPath']=child.text
                        elif child.tag=='ImplicitWait':
                            env_dict['ImplicitWait']=int(child.text)
                        elif child.tag=='URL':
                            env_dict['URL']=child.text
            return env_dict        
        except:
            print(traceback.format_exc())
            
# o=EnvironmentReader()
# print(o.get_environment_dict())
# print(QEEnvironment.get_browserpath())
# print(QEEnvironment.get_browsername())
# print(QEEnvironment.get_environment())
# print(QEEnvironment.get_implecitwait())
# print(QEEnvironment.get_url())        