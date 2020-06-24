'''
Created on Apr 12, 2020

@author: Nitesh
'''

import os
import traceback
from PyTestFramework.crmpro_automation.utilities.general_custom_exceptions import FileDoesNotExistsInGivenDir

def get_file(dir_path, file_name):
    file_flag=False
    try:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(".xlsx"):
                    if file_name in file:
                        file_flag=True
                        return root+'\\'+str(file)
            if file_flag==False:
                raise FileDoesNotExistsInGivenDir("File: "+file_name+" does not exists")
    except:
        print(traceback.print_exc())
    return None

# cur_dir_path = os.path.dirname(os.path.realpath(__file__))
# dir_path=cur_dir_path.split(sep="\\filereader")[0]+"\\testdata"
# 
# get_file(dir_path, 'contact_pg_testdata')
