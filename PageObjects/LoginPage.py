import time


class LoginPage:
    txt_username_xpath = "//input[@id='ContentPlaceHolder_userNameTextBox']"
    txt_password_xpath = "//input[@id='ContentPlaceHolder_passwordTextbox']"
    btnLogin_id = "ContentPlaceHolder_loginButton"
    lnkUserProfile_xpath = "//a[@id='userPropfile']"
    btnSignOut_xpath = "//a[@id='signOut']"
    lnkLoginAgain_xpath = "//a[@id='ContentPlaceHolder_lnkLoginAgain']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self):
        self.driver.find_element_by_xpath(self.txt_username_xpath).clear()
        return self.driver.find_element_by_xpath(self.txt_username_xpath)

    def setPassword(self):
        self.driver.find_element_by_xpath(self.txt_password_xpath).clear()
        return self.driver.find_element_by_xpath(self.txt_password_xpath)

    def clickOnLogin(self):
        self.driver.find_element_by_id(self.btnLogin_id).click()
        time.sleep(5)

    def clickOnSignOut(self):
        self.driver.find_element_by_xpath(self.lnkUserProfile_xpath).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.btnSignOut_xpath).click()

    def clickOnLoginAgain(self):
        self.driver.find_element_by_xpath(self.lnkLoginAgain_xpath).click()

