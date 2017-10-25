import ConfigParser
import os
import sys
from telnetlib import EC
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from FunctionLibrary.CommonFunctions.Commonfunctions import CommonFunctions


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


Config = ConfigParser.ConfigParser()
Root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root+ "/../ObjectLibrary/LoginpageObjects.ini")
Config.read(Root+ "/../DataBank/Datavalue.ini")
Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root + "/../ObjectLibrary/AupPreferencesObject.ini")
Config.read(Root +  "/../ObjectLibrary/AupSchedulerObject.ini")

class AupPreferences():
    global commonObject
    commonObject = CommonFunctions()

    url=Config.get('LoginpageObjects', 'URL')
    userName=Config.get('LoginpageObjects', 'username')
    passWord=Config.get('LoginpageObjects', 'passsword')
    usname_Value=Config.get('Datavalue', 'usname_value')
    password_Value=Config.get('Datavalue', 'pssword_value')
    firstSiteName = Config.get('AupPreferencesObject', 'td_preferences_id')
    siteDeleteBtn = Config.get('AupPreferencesObject', 'btn_preferences_id')
    siteConfirmDeleteBtn = Config.get('AupPreferencesObject', 'btn_preferences_confirm')
    siteSearchText = Config.get('AupPreferencesObject', 'txt_preferences_gsearch')
    actualMessage = Config.get('AupPreferencesObject', 'lbl_prefernces_actual')
    expectedMessage = Config.get('AupPreferencesObject', 'Expected_message')
    logout=Config.get('AupPreferencesObject', 'lnk_preferences_logout')
    check_button=Config.get('AupPreferencesObject', 'Check_new_aup')
    confirm_button=Config.get('AupPreferencesObject', 'Check_new_add')
    site_count=Config.get('AupPreferencesObject','count_site')
    expectedMessage_addsite=Config.get('AupPreferencesObject','Expected_site_message')
    home_lnk=Config.get('HomepageObjects', 'img_home_schedulerLink')
    aup_shd_lnk=Config.get('AupSchedulerObject', 'lnk_scheduler_PreferenceMenuLink')
  
    def CustomTestFunctions(self,driver):

        #         print func_name
        """This function will create the object for AUP preferences view controller and triggers the required
         UI test cases via the class methods"""
        try:
#             print os.path.abspath(os.curdir)  
            commonObject.loginToCrux(self.url,self.userName,self.passWord,self.usname_Value,self.password_Value,driver)
#             commonObject.timeDelay(self.home_lnk,driver)
            
#             element = WebDriverWait(driver, 60).until((EC.visibility_of_element_located(By.XPATH, self.home_lnk)))
            # Navigate to AUP preferences page from Home page.
            self.gotoPreferencesview(commonObject,self.home_lnk,self.aup_shd_lnk,driver)
	    #driver.get("https://kalaiselvan-ramu.hmsdev.lan/sitesnap/aup_preferences")
            Actual_mesg =self.deletePreference(commonObject,self.firstSiteName,self.siteDeleteBtn,self.siteConfirmDeleteBtn,
                                               self.siteSearchText,self.actualMessage,self.expectedMessage,Root,driver) 
            ## Logout from CRUX and kill the browser object
            assert Actual_mesg==self.expectedMessage
# 	    print self.expectedMessage
            commonObject.logoutFromCrux(self.logout,driver)
            return True

        except AssertionError :
            print (" Tese Case Failed ")
            raise AssertionError
            return False



    def gotoPreferencesview(self,commonObject, schedulerLink, preferenceLink,driver):
        """This function opens the AUP Preferences view"""
        print "On Home page, Clicking on Scheduler Link"
        # You are now on home page. Search scheduler link and click
        commonObject.gotoPage(schedulerLink,driver)

        print "On Schedueler page, Clicking on AUP Preferences Link"
        # You are on AUP Scheduler main view. find Preference link and Click
        commonObject.gotoPage(preferenceLink,driver)
        driver.set_page_load_timeout(10)

    def deletePreference(self,commonObject, firstSiteName, delete, confirm_del, search_txt, meassage, Expected_message, root,driver):
        """Delete the table Content"""
        
        print "Get the first site name"
        
        sitename = commonObject.is_ElementPresent(By.XPATH,firstSiteName,driver).text
        
        # Click on Delete button
        print "site name is :" +sitename

        print "Click on Delete button"
        delButton =commonObject.is_ElementPresent(By.XPATH, delete,driver)
        delButton.click()
        # Confirm the delete operation
        print "Confirm the delete operation"
        commonObject.is_ElementPresent(By.XPATH, confirm_del, driver).click()
        driver.set_page_load_timeout(10)
        # Searching for the deleted site
        print "searching for the deleted site"
        
        
        commonObject.is_ElementPresent(By.XPATH,search_txt,driver).send_keys(sitename)
#         commonObject.is_ElementPresent(By.XPATH,meassage,driver).text
        
        Actual_message = commonObject.is_ElementPresent(By.XPATH,meassage,driver).text
        
        
        return Actual_message
    
    def addPreference (self,driver,commonObject):
        """Add the table Content"""
     
        try:
      
            #login to Crux
            commonObject.loginToCrux(self.url,self.userName,self.passWord,self.usname_Value,self.password_Value,driver)
            commonObject.timeDelay(self.home_lnk)
            # Navigate to AUP preferences page from Home page.
            self.gotoPreferencesview(commonObject,self.home_lnk,self.aup_shd_lnk,driver)
            commonObject.is_ElementPresent(By.ID, self.check_button, driver).click()
            commonObject.is_ElementPresent(By.XPATH, self.confirm_button, driver).click()
            Actual_mesg=commonObject.is_ElementPresent(By.ID,self.site_count,driver).text
                   
#             asserts.assert_equal(Actual_mesg,expectedMessage)
            assert Actual_mesg==self.expectedMessage_addsite
             
          #  commonObject.logoutFromCrux(self.logout,driver)
            return True
	    commonObject.logoutFromCrux(self.logout,driver) 

        except AssertionError :
            print (" Tese Case Failed ")
            raise AssertionError
            return False
