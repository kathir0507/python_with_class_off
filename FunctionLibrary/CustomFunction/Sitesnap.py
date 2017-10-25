import ConfigParser
from cgitb import strong
from multiprocessing.util import is_exiting
import os
import sys

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


class Sitesnap():
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
            Expected_sitename=sitetab.text
            commonObject.pageloadtime(10,driver)    
            print "Expected site"
            print Expected_sitename
            commonObject.is_ElementPresent(By.XPATH,self.site_li,driver).click()
            commonObject.pageloadtime(10,driver)      
            Actual_sitename=commonObject.is_ElementPresent(By.TAG_NAME,self.Actual_site_name,driver).text
            commonObject.pageloadtime(10,driver)    
            print "Actual site"
            print Actual_sitename
            commonObject.pageloadtime(10,driver)
            if((Expected_sitename==Actual_sitename) and 
            (commonObject.is_exists(By.XPATH,self.statsnap_value,driver) or commonObject.is_exists(By.XPATH,self.create_value,driver))):
                return True
                commonObject.logoutFromCrux(self.logout,driver)
        except AssertionError :
            print (" Tese Case Failed ")
            raise AssertionError
            return False
      
