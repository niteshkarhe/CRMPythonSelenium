'''
Created on Mar 26, 2020

@author: Nitesh
'''
import unittest
from PyTestFramework.crmpro_automation.tests.login_test.login_test import TestLogin

#to get all tests from TestLogin class

login_tests=unittest.TestLoader().loadTestsFromTestCase(TestLogin)

#create a test suites
smoke_test=unittest.TestSuite([login_tests])

unittest.TextTestRunner(verbosity=2).run(smoke_test)