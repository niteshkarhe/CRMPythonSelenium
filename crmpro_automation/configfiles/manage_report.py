'''
Created on Mar 27, 2020

@author: Nitesh
'''
import os
from PyTestFramework.crmpro_automation.filereader.config_reader import ConfigReader

class ManageReport():
    dest_report_path=None
    dest_asset_path=None
    
    def cut_report_to_folder(self):
        cur_dir_name=os.path.dirname(os.path.realpath(__file__))
        report_folder_file=cur_dir_name.split(sep="\\configfiles")[0]+"\\reports\\report.html"
        asset_folder_path=cur_dir_name.split(sep="\\configfiles")[0]+"\\reports\\assets"
        appli_config_path=cur_dir_name+"\\application_config.ini"
        config=ConfigReader(appli_config_path).get_config()
        report_resoure_path=config['Report Resources']['report_notepad_path']
        with open(report_resoure_path) as report:
            self.dest_report_path=report.readline().rstrip()
            self.dest_asset_path=report.readline()
            print('Report resource file is read!')
        os.rename(report_folder_file, self.dest_report_path)
        os.rename(asset_folder_path, self.dest_asset_path)
        print('report.html and assets folder are cut and pasted into mentioned paths in report_resources.txt file')
    
    def write_report_path(self, report_path_details):
        cur_dir_name=os.path.dirname(os.path.realpath(__file__))
        appli_config_path=cur_dir_name+"\\application_config.ini"
        config=ConfigReader(appli_config_path).get_config()
        report_resoure_path=config['Report Resources']['report_notepad_path']
        report_path=report_path_details[0]
        report_asset_path="\n"+report_path_details[1]
        print(report_resoure_path)
        with open(report_resoure_path, "w+") as report:
            report.write(report_path)
            report.write(report_asset_path)
            print("Resource Report File is updated!")
        
#o=ManageReport()
#tup=("D:\\NK\\Python\\PyTestFramework\\crmpro_automation\\reports\\report-28-03-2020 14-31-48\\report.html", "D:\\NK\\Python\\PyTestFramework\\crmpro_automation\\reports\\report-28-03-2020 14-31-48\\assets")
#o.write_report_path(tup)
#o.cut_report_to_folder()

if __name__ == '__main__':
    ManageReport().cut_report_to_folder()