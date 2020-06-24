'''
Created on Jun 21, 2020

@author: Nitesh
'''
import xlrd
import xlwt
import traceback
import os
from PyTestFramework.crmpro_automation.filereader.searchfile import get_file
from PyTestFramework.crmpro_automation.utilities.general_custom_exceptions import *

class ExcelDataReader():
    __data_list=[]
    
    def __init__(self, file_name, sheet_name, testname):
        self.read_file_data(file_name, sheet_name, testname)
        
    def get_test_data(self):
        return self.__data_list
    
    def read_file_data(self, file_name, sheet_name, testname):
        cur_dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path=cur_dir_path.split(sep="\\filereader")[0]+"\\testdata"
        excel_file_path = str(get_file(dir_path, file_name)).replace("\\", "\\\\")
        wb = xlrd.open_workbook(excel_file_path)
        self.sheet = wb.sheet_by_name(sheet_name)
        self.__data_list=self.read_test_data(testname)
        del wb
        
    def read_test_data(self, test_case):
        row_num = self.get_data_rows_num(test_case)
        keyCount=0
        column_count=0
        for row in row_num:
            data={}
            for key in range(self.sheet.ncols):
                keyValue = self.read_row_cell(0, keyCount)
                actData=self.read_row_cell(row,column_count)
                if(keyValue=='TestCase'):
                    data[keyValue]=test_case
                elif(keyValue!=None):
                    data[keyValue]=actData
                keyCount+=1
                column_count+=1
            self.__data_list.append(data)
            keyCount=0
            column_count=0
        return self.__data_list
    
    def get_cell_row_num(self, test_case_name):
        row_flag=False
        try:
            count = 0
            testcase_row_num = 0
            for row in range(self.sheet.nrows):
                for col in self.sheet.row_values(row):
                    if isinstance(col, str):
                        if col.strip() != '':
                            if (col == test_case_name):
                                # print(row)
                                testcase_row_num = row
                                row_flag=True
                            count += 1
            if row_flag==False:
                raise TestCaseNotFoundInExcelSheet('Test case with name: '+test_case_name+" not present in excel sheet test data")
            return testcase_row_num
        except:
            #DriverSetup().log.error('#### Error: Row number is not obtained')
            print(traceback.print_exc())
        return None

    def get_cell_col_num(self, test_case_name):
        col_flag=False
        try:
            count=0
            testcase_col_num=0
            for col in range(self.sheet.ncols):
                for row in self.sheet.col_values(col):
                    if isinstance(row, str):
                        if row.strip() != '':
                            if(row==test_case_name):
                                testcase_col_num=col
                                col_flag=True
                            count +=1
            if col_flag==False:
                raise TestCaseNotFoundInExcelSheet('Test case with name: '+test_case_name+" not present in excel sheet test data")
            return testcase_col_num
        except:
            #DriverSetup().log.error('#### Error: Column number is not obtained')
            print(traceback.print_exc())
        return None
    
    def read_row_cell(self, rowx, colx):
        try:
            if colx !=None and rowx !=None:
                value=self.sheet.cell_value(rowx, colx)
                if isinstance(value, str):
                    if value.strip() != '':
                        return value
                elif isinstance(value, float):
                    if value==int(value):
                        return int(value)
                    else:
                        return value
                else:
                    return value
        except:
            #DriverSetup().log.error('#### Error: Excel value is not read')
            print(traceback.print_exc())
        return None
    
    def get_data_rows_num(self, test_case_name):
        row_flag=False
        row_index_lst=[]
        try:
            count = 0
            for row in range(self.sheet.nrows):
                for col in self.sheet.row_values(row):
                    if isinstance(col, str):
                        if col.strip() != '':
                            if (col == test_case_name):
                                #print(row)
                                row_index_lst.append(row)
                                row_flag=True
                            count += 1
            if row_flag==False:
                raise TestCaseNotFoundInExcelSheet('Test case with name: '+test_case_name+" not present in excel sheet test data")
            return row_index_lst
        except:
            #DriverSetup().log.error('#### Error: Row number is not obtained')
            print(traceback.print_exc())
        return None
    
    def add_sheet(self, wb, sheet_name):
        wb.
    
# o=ExcelDataReader('contact_pg_testdata', "Sheet2", 'Login Test')
# print(o.get_test_data())