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
from string import lstrip


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


Config = ConfigParser.ConfigParser()
Root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root+ "/../ObjectLibrary/LoginpageObjects.ini")
Config.read(Root+ "/../DataBank/Datavalue.ini")
Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root + "/../ObjectLibrary/ProductreleaseinfoObject.ini")
Config.read(Root +  "/../ObjectLibrary/AupSchedulerObject.ini")
Config.read(Root +  "/../ObjectLibrary/AupPreferencesObject.ini")
Config.read(Root +  "/../ObjectLibrary/time.ini")

class Populatedate_cron2():
    global commonObject
    commonObject = CommonFunctions()

    url=Config.get('LoginpageObjects', 'URL')
    userName=Config.get('LoginpageObjects', 'username')
    passWord=Config.get('LoginpageObjects', 'passsword')
    usname_Value=Config.get('Datavalue', 'usname_value')
    password_Value=Config.get('Datavalue', 'pssword_value')
    home_lnk=Config.get('HomepageObjects', 'img_home_schedulerLink')
    product_release_info=Config.get('ProductreleaseinfoObject', 'menu_product_release_id')
    product_release_Addnew=Config.get('ProductreleaseinfoObject', 'new_product_release_info_id')
    dropdown=Config.get('ProductreleaseinfoObject','dropdown')
    prod_release_date=Config.get('ProductreleaseinfoObject','prod_release_date')
    patch_date=Config.get('ProductreleaseinfoObject','patch_date')
    addbutton=Config.get('ProductreleaseinfoObject','Addbutton')
    siteSearchText = Config.get('ProductreleaseinfoObject', 'txt_preferences_gsearch')
    home_lnk_page=Config.get('ProductreleaseinfoObject', 'home_lnk_page')
    Admin_lnk=Config.get('ProductreleaseinfoObject', 'Admin_lnk')
    view_lnk=Config.get('ProductreleaseinfoObject', 'view_lnk')
    cron2_lnk=Config.get('ProductreleaseinfoObject', 'cron2_lnk')
    run=Config.get('ProductreleaseinfoObject', 'run')
  
    def CustomTestFunctions(self,driver):
        """To Run the Cron2 Job"""
      
        try:
            commonObject.loginToCrux(self.url,self.userName,self.passWord,self.usname_Value,self.password_Value,driver)
#             self.gotoPreferencesview(commonObject,self.home_lnk,self.product_release_info,driver)
            print "Clicking scheduler menu in the home page "
            commonObject.gotoPage(self.home_lnk,driver)
            commonObject.pageloadtime(10,driver)
            print "Clicking Product Release Information menu Scheduler Page "
            commonObject.gotoPage(self.product_release_info,driver)
            print "Deleting entire Product release Details"
            bool_Delete=commonObject.delete_table(driver)
            print"If the Forecast date exists Delete "
            if(bool_Delete):
                form_string=self.Add_details(driver, self.product_release_Addnew)
                bool_value=commonObject.select_by_text(driver,self.dropdown,form_string)
                commonObject.pageloadtime(10, driver)
                if(bool_value):
                    actual_info=self.prodcut_release_info(driver,commonObject,self.prod_release_date,self.patch_date,self.addbutton,self.siteSearchText,form_string)
                    alert_mes=self.cronjob2_run(commonObject,driver,self.home_lnk_page,self.Admin_lnk,self.cron2_lnk,self.view_lnk,self.run)
                    assert alert_mes=="Finished"
                    return True
             
            else:
                print"If Forecast date Not exists Create New one" 
                form_string=self.Add_details(driver, self.product_release_Addnew)
                commonObject.pageloadtime(10, driver)
                bool_value=commonObject.select_by_text(driver,self.dropdown,form_string)
                self.prodcut_release_info(driver,commonObject,self.prod_release_date,self.patch_date,self.addbutton,self.siteSearchText,form_string)
                alert_mes=self.cronjob2_run(commonObject,driver,self.home_lnk_page,self.Admin_lnk,self.cron2_lnk,self.view_lnk,self.run)
                assert alert_mes=="Finished"
                return True
            
        except AssertionError :
            print (" Tese Case Failed ")
            raise AssertionError
            return False

        
    def Add_details(self,driver,product_addnew):
        """To Add details in the Site"""
        commonObject.gotoPage(product_addnew,driver)
        commonObject.pageloadtime(10,driver)
        print "Current month"      
        currentmonth=commonObject.timestampmonth()
        print currentmonth  
        print "Current Year"    
        currentyear=commonObject.timestampyear()
          
        print "Release date"
        release=self.datecalculation(driver,commonObject,currentmonth)
        print release  
        print"Form String"
        form_string=self.formstring(driver,release,currentyear)
        print form_string
        return form_string

    
    def datecalculation(self,driver,commonObject,curmonth):
        """To Caculate the date"""
        first_term_release=['February','March','April']
        second_term_release=['May','June','July']
        third_term_release=['August','September','October']
        fourth_term_release=['November','December','January']
        
        if curmonth in first_term_release:
            return "February"
        elif curmonth in second_term_release:
            return "May"
        elif curmonth in third_term_release:
            return "August"
        else:
            return "November" 
        
    def cronjob2_run(self,commonObject,driver,home_lnk_page,Admin_lnk,cron2_lnk,view_lnk,run):
        
        print "Returning Home page"
        commonObject.gotoPage(home_lnk_page,driver)
        commonObject.pageloadtime(10,driver)
        print "Clicking on Admin page"
        commonObject.gotoPage(Admin_lnk,driver)
        commonObject.pageloadtime(10,driver)
        print "Clicking on View page"
        commonObject.gotoPage(view_lnk,driver)
        commonObject.pageloadtime(10,driver)
        print "Clicking on Cron2 Tab"
        commonObject.gotoPage(cron2_lnk,driver)   
        time.sleep(10)

        print "Running Cron"
        job_id=int(commonObject.is_ElementPresent(By.XPATH,"//tr[1]/td[1]",driver).text)
        commonObject.gotoPage(run,driver)
        time.sleep(10)
        alert_msg=commonObject.alert_present(driver)
        time.sleep(10)
        print "JoB Id"
        job_id_new=job_id+1
        time.sleep(10)
        print job_id_new
        print "After Running cron looks for the text"
        time.sleep(10)
        cron2_txt=commonObject.is_ElementPresent(By.XPATH,"//tr[1]/td[2]",driver).text
        print cron2_txt
        print "After CronRun looks for the message"
        afterrun_message_txt=commonObject.is_ElementPresent(By.XPATH,"//tr[1]/td[5]",driver).text
        time.sleep(10)
        
        if(job_id!=job_id_new and cron2_txt=="AUP Forecast Date Generation('Job 2')" and "Forecast Date generated for sites:" in afterrun_message_txt):
            return "Finished"
        
        else:
            return "Failed"
        
        
    def prodcut_release_info(self,driver,commonObject,prod_release_date,patch_date,addbutton,siteSearchText,form_string):
        print "Select Current Date"
        cdate=commonObject.currentdate()
        time.sleep(10)
        print cdate
        commonObject.is_ElementPresent(By.XPATH,prod_release_date, driver).send_keys(cdate)
        commonObject.pageloadtime(10, driver)
        commonObject.is_ElementPresent(By.XPATH,prod_release_date, driver).send_keys(Keys.ENTER)
        time.sleep(10)
        print "Select Next Date"
        patchdate=commonObject.nextdate()
        time.sleep(10)
        print patchdate

        commonObject.pageloadtime(10, driver)
        commonObject.is_ElementPresent(By.XPATH,patch_date, driver).send_keys(patchdate)
#         commonObject.is_ElementPresent(By.XPATH,patch_date, driver).send_keys(Keys.ENTER)
        commonObject.pageloadtime(10, driver)
        print "Clicking on the Add Date"
        commonObject.is_ElementPresent(By.XPATH,addbutton,driver).click()
        print "searching for the Product release Version"
        commonObject.is_ElementPresent(By.XPATH,siteSearchText,driver).send_keys(form_string)
        commonObject.is_ElementPresent(By.XPATH,siteSearchText, driver).send_keys(Keys.ENTER)
        text_td="//td[text()='"+form_string+"']"
        Actual_prod=commonObject.is_ElementPresent(By.XPATH,text_td,driver).text
        
        return Actual_prod
        
    def formstring(self,driver,release,year):
        str="Oracle Service Cloud "+release+" "+year
        return str