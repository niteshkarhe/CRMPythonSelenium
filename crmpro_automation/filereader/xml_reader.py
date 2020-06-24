'''
Created on Mar 14, 2020

@author: Nitesh
'''

import xml.etree.ElementTree as ET

class XmlReader():
    
    @classmethod
    def parse_xml(cls, xml_path):
        # create element tree object 
        return ET.parse(xml_path)
        
        # get root element 
        #root = tree.getroot()  
        
#         print(root.tag)
#         print(root[0].tag)
#         print(root[0].attrib)
#         
#         for x in root[0]:
#             print(x.tag, x.attrib)
#             
#         for x in root[0]:
#             print(x.text)  
#         for x in root.findall('QAEnvironment'):
#             browsername=x.find('BrowserName').text
#             print(browsername)
#             print(x.attrib.get('value'))
#             
#             try:
#                 if x.attrib.get('value')==environment:
#                     pass
#             except:
#                 pass    
        
# cur_dir_path = os.path.dirname(os.path.realpath(__file__))
# xml_path=cur_dir_path.split(sep="\\filereader")[0]+"\\configfiles\\ExecutionConfig.xml"
# o=XmlReader()
# o.parse_xml(xml_path)