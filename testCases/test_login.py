import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from selenium import webdriver
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("************ Test_001_Login  ***********")
        self.logger.info("************ Verifying Home Page Title  ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************ Home Page Title test is passed  ***********")
        else:
            self.driver.save_screenshot(self, "..\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("************ Home Page Title test is passed  ***********")
            assert False

    def test_login(self,setup):
        self.logger.info("************ Verifying login test  ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("************ Login test is passed  ***********")

        else:
            self.driver.save_screenshot(self, ".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False
            self.logger.info("************ Login test is failed ***********")
#this is a pyunit testcase.below is the syntax for parallel method execution.here -n=2 is for number of methods to be executed parallelly
# pytest -v -s -n=2 --html=Reports\report.html test_login.py --browser chrome
