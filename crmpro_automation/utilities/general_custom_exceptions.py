#coding=UTF-8
'''
Created on Mar 14, 2020

@author: Nitesh
'''

class DriverNotSetException(Exception):
    '''When driver is not set for a defined path then this exception is raised'''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'DriverNotSetException, {0} '.format(self.message)
        else:
            return 'DriverNotSetException has been raised'
        
class BrowserNameDoesNotExistException(Exception):
    '''When browser name is present in browserdriver.py enum class then this exception is raised'''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'BrowserNameDoesNotExistException, {0} '.format(self.message)
        else:
            return 'BrowserNameDoesNotExistException has been raised'

class NodeAttributeDoesNotExist(Exception):
    '''In ExecutionConfig.xml if attribute of a given node does not exist then this exception is raised'''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'NodeAttributeDoesNotExist, {0} '.format(self.message)
        else:
            return 'NodeAttributeDoesNotExist has been raised'
        
class NodeTagDoesNotExist(Exception):
    '''In ExecutionConfig.xml if tag of a given node does not exist then this exception is raised'''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'NodeTagDoesNotExist, {0} '.format(self.message)
        else:
            return 'NodeTagDoesNotExist has been raised'
        
class FileDoesNotExistsInGivenDir(Exception):
    '''It is raised when File is not present in given directory'''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'FileDoesNotExistsInGivenDir, {0} '.format(self.message)
        else:
            return 'FileDoesNotExistsInGivenDir has been raised'

class TestCaseNotFoundInExcelSheet(Exception):
    '''It is raised when testcase is not present in given excel sheet test data'''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'TestCaseNotFoundInExcelSheet, {0} '.format(self.message)
        else:
            return 'TestCaseNotFoundInExcelSheet has been raised'