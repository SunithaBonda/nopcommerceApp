import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#https://admin-demo.nopcommerce.com/
class AddCustomer():
    #add customer page
   linkCustomers_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"  #//a[@href='#']//span[contains(text(),'Customers')]"
   linkCustomers_menuitem_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"  #"//span[@class='menu-item-title'][contains9text90,'Customers'0]""
   btnAddnew_xpath="//a[@class='btn btn-primary']"
   txtEmail_xpath="//input[@id='Email']"  #"Email"
   txtPassword_xpath="//input[@id='Password']"
   txtFirstName_xpath="//input[@id='FirstName']"
   txtLastName_xpath = "//input[@id='LastName']"
   rbMale_Gender_id="Gender_Male"
   rbFemale_Gender_id="Gender_Female"
   txtDOB_id="DateOfBirth"
   txtCOMName_Name="Company"
   chkbx_tax_name="IsTaxExempt"
   txt_Customerrole_xpath="//div[@class='k-widget k-multiselect k-multiselect-clearable']"
   txt_administrators_span_txt="Administrators"
   txt_forummoderators_span_txt="Forum Moderators"
   txt_Guests_span_txt="Guests"
   txt_Registered_xpath="//div[@span='Registered']"
   txt_Vendors_span_txt="Vendors"

   def __init__(self,driver):
     self.driver=driver

   def ClickOnCustomersMenu(self):
     self.driver.find_element(By.XPATH, self.linkCustomers_menu_xpath).click()

   def ClickOnCustomersMenuItem(self):
     self.driver.find_element(By.XPATH, self.linkCustomers_menuitem_xpath).click()

   def ClickOnAddNew(self):
     self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

   def setEmail(self, email):
     self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

   def setPassword(self, password):
     self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

   def setFirstName(self,fname):
      self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

   def setLastName(self, lname):
      self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

   def setGender(self, gender):
       if gender=='Male':
           self.driver.find_element(By.ID, self.rbMale_Gender_id).click()
       elif gender=='Female':
           self.driver.find_element(By.ID, self.rbFemale_Gender_id).click()
       else:
           self.driver.find_element(By.ID, self.rbMale_Gender_id).click()

   def setDOB(self, DOB):
       self.driver.find_element(By.ID, self.txtDOB_id).send_keys(DOB)
   def setCompanyName(self, ComName):
       self.driver.find_element(By.NAME, self.txtCOMName_Name).send_keys(ComName)

   def SelectTaxCHkBox(self):
       self.driver.find_element(By.NAME, self.chkbx_tax_name).click()

   def setCustomerRole(self,role):
       self.driver.find_element(By.ID, self.txt_Customerrole_xpath).click()
       time.sleep(3)
       if role=="Administrators":
           self.listitem=self.driver.find_element(By.TAG_NAME, self.txt_adminstrator_span_txt)
       elif role=="Forum Moderators":
           self.listitem=self.driver.find_element(By.TAG_NAME, self.txt_forummoderators_span_txt)
       elif role=="Registered":
           self.listitem=self.driver.find_element(By.TAG_NAME, self.txt_registered_span_txt)
       elif role=="Guests":
           time.sleep(3)
           self.driver.find_element(By.CLASS_NAME, "//*[@id='customer-info']").click()
            #here we have to clear the text box .because we have to select either registered or guests.both cannot be selected
           self.listitem=self.driver.find_element(By.TAG_NAME, self.txt_guests_span_txt)