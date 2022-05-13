from selenium.webdriver.common.by import By
class SearchCustomer():

    txtEmail_id="SearchEmail"
    txtFirstName_id="SearchFirstName"
    txtLastName_id="SearchLastName"
    btnSearch_id="search-customers"

    table_id="customers-grid_wrapper"
    ddownmonth_id="SearchMonthOfBirth"
    ddownday_id="SearchDayOfBirth"
    txtCompany_id="SearchCompany"
    txtIPAddress_id="SearchIpAddress"

    def __init__(self,driver):
        self.driver=driver

    def enterEmail(self,email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def enterFirstName(self,fname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fname)

    def enterLastName(self,lname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def ClickOnSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()


