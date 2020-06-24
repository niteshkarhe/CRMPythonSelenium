'''
Created on Mar 26, 2020

@author: Nitesh
'''

import unittest
from PyTestFramework.crmpro_automation.tests.login_test.login_test import TestLogin

class RunSuite(unittest.TestSuite):
        def suite(self):
            suite = unittest.TestSuite()
            suite.addTest(TestLogin('test_login'))
            #suite.addTest(TestLogin('test_one_login'))
            return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(RunSuite().suite())