#coding=utf-8
import inspect
import logging.config
from datetime import datetime
import os
import configparser
from os import path

class Logger:
    
    #current_time
    now=datetime.now()
    current_time=now.strftime("%d-%m-%Y %H-%M-%S")
    cur_dir_path=os.path.dirname(os.path.realpath(__file__))
    report_folder_path=None
    
    @classmethod
    def report(cls):
        #report folder
        folder_name="report-"+cls.current_time
        report_folder=cls.cur_dir_path.split(sep="\\utilities")[0]+"\\reports"
        cls.report_folder_path=os.path.join(report_folder, folder_name)
        cls.report_folder_path=cls.report_folder_path.replace("\\", "/")
        os.mkdir(cls.report_folder_path)
        return cls.report_folder_path
    
    def customLogger(self, report_folder_path, logLevel=logging.DEBUG):
        log_folder_path=report_folder_path
        file_name="automation-"+self.current_time+".log"
        file_path=os.path.join(log_folder_path, file_name)
        file_path=file_path.replace("\\", "/")
        
        #Write logging.conf file with log file path
        logconfig_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
        config = configparser.ConfigParser()
        config.read(logconfig_file_path)
        args_value="(\'"+file_path+"\','a\')"
        config.set('handler_fileHandler', 'args', args_value)
        with open(logconfig_file_path, 'w') as configfile:
            config.write(configfile)
            
        logging.config.fileConfig(logconfig_file_path)
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        return logger
    
# o=Logger()
# o.customLogger()