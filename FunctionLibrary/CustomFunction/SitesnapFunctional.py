import ConfigParser
from cgitb import strong
from multiprocessing.util import is_exiting
import os
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from FunctionLibrary.CommonFunctions.Commonfunctions import CommonFunctions


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


Config = ConfigParser.ConfigParser()
Root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root+ "/../ObjectLibrary/LoginpageObjects.ini")
Config.read(Root+ "/../DataBank/Datavalue.ini")
Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root + "/../ObjectLibrary/SitesnapObject.ini")


class SitesnapFunctioanl():
    global commonObject
    commonObject = CommonFunctions()

    url=Config.get('LoginpageObjects', 'URL')
    userName=Config.get('LoginpageObjects', 'username')
    passWord=Config.get('LoginpageObjects', 'passsword')
    usname_Value=Config.get('Datavalue', 'usname_value')
    password_Value=Config.get('Datavalue', 'pssword_value')
    home_lnk=Config.get('HomepageObjects', 'img_home_sitesnaplink')
    site_snap=Config.get('SitesnapObject','search_site_id')
    sitename=Config.get('SitesnapObject','sitename')
    site_li=Config.get('SitesnapObject','site_li_text')
    statsnap_value=Config.get('SitesnapObject','statsnap_value')
    create_value=Config.get('SitesnapObject','create_value')
    Actual_site_name=Config.get('SitesnapObject','Actual_sitename')
    Sitesnap_content=Config.get('SitesnapObject','sitesnap_content')
    qualified_text=Config.get('SitesnapObject','qualified')
    enroll_text=Config.get('SitesnapObject','enroll')
   
    def CustomTestFunctions(self,driver):
        
        #         print func_name
        """This function will create the object for AUP preferences view controller and triggers the required
         UI test cases via the class methods"""
        try:
            
            commonObject.loginToCrux(self.url,self.userName,self.passWord,self.usname_Value,self.password_Value,driver)
            # Navigate to Sitesnap page.
            print "Sitesnap Loaded "
            commonObject.gotoPage(self.home_lnk,driver);
            print "Verify search textbox present or not"
            commonObject.is_exists(By.ID,self.site_snap,driver);
            print "Enter sitename in the textbox"
            commonObject.is_ElementPresent(By.ID,self.site_snap,driver).send_keys(self.sitename)
            print "Pressing tab"
            sitetab=commonObject.is_ElementPresent(By.XPATH,self.site_li,driver)
            print "Expected site"
            Expected_sitename=sitetab.text
            print "Waiting"
            commonObject.pageloadtime(10,driver)    
            print "Clicking on the site"
            commonObject.is_ElementPresent(By.XPATH,self.site_li,driver).click()
            print "Waiting"
            commonObject.pageloadtime(10,driver)
            commonObject.is_ElementPresent(By.XPATH,self.statsnap_value,driver).click() 
            print "Completing the process"
            time.sleep(20)
            print "Extracting Datas"
            qualification_text=commonObject.is_ElementPresent(By.XPATH,self.qualified_text,driver).text
            print "Spliting the date String "
            Actual_data=commonObject.string_split(self.Sitesnap_content,"\n",driver);
            print "Getting Actual site"
            Actual_sitename=commonObject.is_ElementPresent(By.TAG_NAME,self.Actual_site_name,driver).text
            commonObject.pageloadtime(10,driver)    
            print "Actual site"
            print Actual_sitename
            print "Getting Enrollment Status"
            commonObject.pageloadtime(10,driver)
            enrollment_text=commonObject.is_ElementPresent(By.XPATH,self.enroll_text,driver).text
            commonObject.pageloadtime(10,driver)
            print "Getting current date and time"
            date_time=commonObject.timestamp()
            """Comparing all the extracted data Against to the site"""
            
            if((Expected_sitename==Actual_sitename) and 
            (qualification_text=="NOT QUALIFIED" or qualification_text=="QUALIFIED" ) and 
            (enrollment_text=="normal" or enrollment_text=="automatic") and (date_time in Actual_data[3])):
                return True
                commonObject.logoutFromCrux(self.logout,driver)           
            
            
        except AssertionError :
            print (" Tese Case Failed ")
            raise AssertionError
            return False
      
