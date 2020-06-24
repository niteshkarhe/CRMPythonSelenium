'''
Created on Mar 14, 2020

@author: Nitesh
'''

class QEEnvironment():
    
    __env_dict={}
    
    @classmethod
    def set_environment_dict(cls, env_dict):
        cls.__env_dict=env_dict
    
    @classmethod
    def get_environment_dict(cls):
        return cls.__env_dict
