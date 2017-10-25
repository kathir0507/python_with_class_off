import ConfigParser
from datetime import date, timedelta
import datetime
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
Config.read(Root +  "/../ObjectLibrary/PerformCruxCxRestIntegrationObject.ini")
Config.read(Root +  "/../ObjectLibrary/time.ini")

class PerformCruxCxRestIntegration_cron4():
    global commonObject
    commonObject = CommonFunctions()

    url=Config.get('LoginpageObjects', 'URL')
    userName=Config.get('LoginpageObjects', 'username')
    passWord=Config.get('LoginpageObjects', 'passsword')
    usname_Value=Config.get('Datavalue', 'usname_value')
    password_Value=Config.get('Datavalue', 'pssword_value')
    aup_shd_lnk=Config.get('PerformCruxCxRestIntegration', 'menu_id')
    home_lnk=Config.get('HomepageObjects', 'img_home_schedulerLink')
    check_box=Config.get('PerformCruxCxRestIntegration', 'check_box')
    change_button=Config.get('PerformCruxCxRestIntegration', 'change_date_button')
    site_forecast_date=Config.get('PerformCruxCxRestIntegration','site_forecast_date')
    change_button_submit=Config.get('PerformCruxCxRestIntegration','change_button_submit')
    home_lnk_page=Config.get('PerformCruxCxRestIntegration', 'home_lnk_page')
    Admin_lnk=Config.get('PerformCruxCxRestIntegration', 'Admin_lnk')
    view_lnk=Config.get('PerformCruxCxRestIntegration', 'view_lnk')
    cron4_lnk=Config.get('PerformCruxCxRestIntegration', 'cron4_lnk')
    run=Config.get('PerformCruxCxRestIntegration', 'run')
  
    def CustomTestFunctions(self,driver):
        try:
            commonObject.loginToCrux(self.url,self.userName,self.passWord,self.usname_Value,self.password_Value,driver)
#             self.gotoPreferencesview(commonObject,self.home_lnk,self.aup_shd_lnk,driver)
            
            alert_mes=self.cronjob4_run(commonObject,driver,self.home_lnk_page,self.Admin_lnk,self.cron4_lnk,self.view_lnk,self.run)
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
    
 
        
    def cronjob4_run(self,commonObject,driver,home_lnk_page,Admin_lnk,cron4_lnk,view_lnk,run):

        print "Clicking on Admin page"
        commonObject.gotoPage(Admin_lnk,driver)
        commonObject.pageloadtime(10,driver)
        print "Clicking on View page"
        commonObject.gotoPage(view_lnk,driver)
        commonObject.pageloadtime(10,driver)
        print "Clicking on Cron4 Tab"
        commonObject.gotoPage(cron4_lnk,driver)   
        print "Running Cron"
        job_id=int(commonObject.is_ElementPresent(By.XPATH,"//tr[1]/td[1]",driver).text)
        commonObject.gotoPage(run,driver)
        commonObject.pageloadtime(10,driver)
        alert_msg=commonObject.alert_present(driver)
        print "New JoB Id has been created"
        job_id_new=job_id+1
        print job_id
        print "After Running cron looks for the text"
        
        cron4_txt=commonObject.is_ElementPresent(By.XPATH,"//tr[1]/td[2]",driver).text
        print job_id_new
        print "After CronRun looks for the message"
        afterrun_message_txt=commonObject.is_ElementPresent(By.XPATH,"//tr[1]/td[5]",driver).text
        print afterrun_message_txt
        if(job_id!=job_id_new and cron4_txt=="Crux CX Rest Integration ('Job 4')" and afterrun_message_txt== "There were no forecast dates to be synched to CX" ):
            return "Finished"
        
        else:
            return "Failed"
        
 