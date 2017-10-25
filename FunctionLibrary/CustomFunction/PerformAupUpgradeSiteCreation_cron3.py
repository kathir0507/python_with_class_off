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
Config.read(Root +  "/../ObjectLibrary/PerformAupUpgradeSiteCreationObject.ini")
Config.read(Root +  "/../ObjectLibrary/time.ini")

class PerformAupUpgradeSiteCreation_cron3():
    global commonObject
    commonObject = CommonFunctions()

    url=Config.get('LoginpageObjects', 'URL')
    userName=Config.get('LoginpageObjects', 'username')
    passWord=Config.get('LoginpageObjects', 'passsword')
    usname_Value=Config.get('Datavalue', 'usname_value')
    password_Value=Config.get('Datavalue', 'pssword_value')
    aup_shd_lnk=Config.get('PerformAupUpgradeSiteCreation', 'menu_id')
    home_lnk=Config.get('HomepageObjects', 'img_home_schedulerLink')
    check_box=Config.get('PerformAupUpgradeSiteCreation', 'check_box')
    change_button=Config.get('PerformAupUpgradeSiteCreation', 'change_date_button')
    site_forecast_date=Config.get('PerformAupUpgradeSiteCreation','site_forecast_date')
    change_button_submit=Config.get('PerformAupUpgradeSiteCreation','change_button_submit')
    home_lnk_page=Config.get('PerformAupUpgradeSiteCreation', 'home_lnk_page')
    Admin_lnk=Config.get('PerformAupUpgradeSiteCreation', 'Admin_lnk')
    view_lnk=Config.get('PerformAupUpgradeSiteCreation', 'view_lnk')
    cron3_lnk=Config.get('PerformAupUpgradeSiteCreation', 'cron3_lnk')
    run=Config.get('PerformAupUpgradeSiteCreation', 'run')

    def CustomTestFunctions(self,driver):
        try:
           
            commonObject.loginToCrux(self.url,self.userName,self.passWord,self.usname_Value,self.password_Value,driver)
            self.gotoPreferencesview(commonObject,self.home_lnk,self.aup_shd_lnk,driver)
            
            alert_mes=self.cronjob3_run(commonObject,driver,self.home_lnk_page,self.Admin_lnk,self.cron3_lnk,self.view_lnk,self.run)
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
    
 
        
    def cronjob3_run(self,commonObject,driver,home_lnk_page,Admin_lnk,cron2_lnk,view_lnk,run):
        print "Returning Home page"
        commonObject.gotoPage(home_lnk_page,driver)
        commonObject.pageloadtime(10,driver)
        print "Clicking on Admin page"
        commonObject.gotoPage(Admin_lnk,driver)
        commonObject.pageloadtime(10,driver)
        print "Clicking on View page"
        commonObject.gotoPage(view_lnk,driver)
        commonObject.pageloadtime(10,driver)
        print "Clicking on Cron3 Tab"
        commonObject.gotoPage(cron2_lnk,driver)   
        print "Running Cron"
        job_id=int(commonObject.is_ElementPresent(By.XPATH,"//tr[1]/td[1]",driver).text)
        commonObject.gotoPage(run,driver)
        commonObject.pageloadtime(10,driver)
        alert_msg=commonObject.alert_present(driver)
        print "New JoB Id has been created"
        job_id_new=job_id+1
        print "After Running cron looks for the text"
        cron3_txt=commonObject.is_ElementPresent(By.XPATH,"//tr[1]/td[2]",driver).text
        
        print "After CronRun looks for the message"
        afterrun_message_txt=commonObject.is_ElementPresent(By.XPATH,"//tr[1]/td[5]",driver).text
        
        if(job_id!=job_id_new and cron3_txt=="AUP Upgrade Site Creation ('Job 3')" and "Total Sites forecasted on" in afterrun_message_txt):
            return "Finished"
        
        else:
            return "Failed"
        
 