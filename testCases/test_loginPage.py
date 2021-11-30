from PageObjects.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from Utilities import XLUtils


class Test_001_DDt_Login(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    log = LogGen.getLogger()
    path = "C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Stock_Status_Management\\TestData\\LoginData.xlsx"

    def test_login_DDT(self):
        self.log.info("********** Test_001_DDT_Login **********")
        self.log.info("********** test_login ddt started ***********")
        self.driver.get(self.baseURL)
        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        lp = LoginPage(self.driver)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            lp.setUserName().send_keys(self.username)
            lp.setPassword().send_keys(self.password)
            lp.clickOnLogin()
            act_title = self.driver.title
            exp_title = "iPAS-CC"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.log.info("***Passed")
                    lp.clickOnSignOut()
                    lp.clickOnLoginAgain()
                    lst_status.append("Pass")
                    XLUtils.writeData(self.path, "Sheet1", r, 4, "test passed")
                elif self.exp == "Fail":
                    self.log.info("***Failed")
                    lp.clickOnSignOut()
                    lp.clickOnLoginAgain()
                    lst_status.append("Fail")
                    XLUtils.writeData(self.path, "Sheet1", r, 4, "test failed")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.log.info("***Failed")
                    lst_status.append("Fail")
                    XLUtils.writeData(self.path, "Sheet1", r, 4, "test failed")
                elif self.exp == "Fail":
                    self.log.info("***Passed")
                    lst_status.append("Pass")
                    XLUtils.writeData(self.path, "Sheet1", r, 4, "test passed")

        if "Fail" not in lst_status:
            self.log.info("******* Login DDt test passed *********")
            assert True
        else:
            self.log.info("****** Login DDT test failed ********")
            assert False

