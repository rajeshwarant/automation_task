import xml.etree.ElementTree as ET
from datetime import datetime
from datetime import timedelta
import os

curr_dir  = os.getcwd()
def xml_update(x,y):
    if str(x).strip().isdigit() and str(y).strip().isdigit():
        mytree = ET.parse(curr_dir +"/test_payload1.xml")
        myroot = mytree.getroot()
        for depart in myroot.iter('DEPART'):
            updated_x = datetime.now() + timedelta(days = x)
            depart.text = updated_x.strftime("%Y%m%d")
        for r in myroot.iter('RETURN'):
            updated_y = datetime.now() + timedelta(days = y)
            r.text = updated_y.strftime("%Y%m%d")
        mytree.write(curr_dir +"/modified.xml")
        print (" Modified xml file created successfully in this path {}".format(curr_dir+"/modified.xml"))

    else:
        print("please provide the correct number")

xml_update(10,15)
