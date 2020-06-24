'''
Created on Jun 22, 2020

@author: Nitesh
'''

import xlwt
import xlrd
from xlutils.copy import copy
import os
import traceback

class ExcelReader():
    __data_dict={}
    
    def __init__(self, file_name, sheet_name, testname):
        self.read_file_data(file_name, sheet_name, testname)
        
    def write_file_data(self, file_name, sheet_name, testname):
        cur_dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path=cur_dir_path.split(sep="\\filereader")[0]+"\\testdata"
        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet(sheet_name, cell_overwrite_ok=True)
        
    def write_data_in_cell(self, ws, rowx, colx, value):
        try:
            ws.write(rowx, colx, value)
        except:
            print(traceback.print_exc())
    
    def write_data_in_column_range(self, ws, rowx, col_range, value_list):
        try:
            for colnum in col_range:
                ws.write(rowx, colnum, value_list[colnum])
        except:
            print(traceback.print_exc())
            
    def write_data_according_to_colname(self, ws, col_names, value_dict):
        try:
            for colnum in len(col_names):
                for colname in value_dict.keys():
                    if(col_names[colnum]==colname):
                        