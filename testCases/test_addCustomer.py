import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen() #Logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("***** Test_003_AddCustomer ****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login Succeessful****")
        self.logger.info("***** starting add customer test*****")
        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuItem()
        self.addcust.ClickOnAddNew()
        self.logger.info("*****    providing customer info *****")
        self.email= random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("ggfgfg")
        self.addcust.setFirstName("asdas")
        self.addcust.setLastName("sfsf")
        self.addcust.setGender("Female")
        self.addcust.setDOB("15/4/1988")
        self.addcust.setCompanyName("Disha Pvt.Ltd")
        self.addcust.SelectTaxCHkBox()
        self.addcust.setCustomerRole("Guests")

def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return''.join(random.choice(chars) for x in range(size))
    driver.close()