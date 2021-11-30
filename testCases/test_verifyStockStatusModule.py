import pytest

from PageObjects.LoginPage import LoginPage
from PageObjects.StockStatusManagementPage import StockStatusManagementPage
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_002_Verify_Stock_Status_Module(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getuserName()
    password = ReadConfig.getPassword()
    log = LogGen.getLogger()

    def test_verifyStockStatusModule(self):
        self.driver.implicitly_wait(10)
        self.log.info("*********** Test_002_Verify_Stock_Status_Module *************")
        self.log.info("*********** test verify stock status module started *********")
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("*************** Login Successful ****************")
        ssmp = StockStatusManagementPage(self.driver)
        ssmp.clickOnStockReceipt()
        ssmp.clickOnGrMobile()
        ssmp.clickOnWarehouseOperation()
        status = ssmp.verifyPresenceOfModule()
        assert status == True
        self.log.info("*********** test verify stock status module passed *********")
        ssmp.clickOnMobileGrid()
        ssmp.clickOnAdminOption()
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    def test_verifyStockStatusPage(self):
        self.driver.implicitly_wait(10)
        self.log.info("*********** test verify stock status page started *********")
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("*************** Login Successful ****************")
        ssmp = StockStatusManagementPage(self.driver)
        ssmp.clickOnStockReceipt()
        ssmp.clickOnGrMobile()
        ssmp.clickOnWarehouseOperation()
        ssmp.clickOnStockStatusModule()
        status = ssmp.verifyStockStatusPage()
        assert status == True
        self.log.info("*********** test verify stock status page passed *********")
        ssmp.clickOnMobileGrid()
        ssmp.clickOnAdminOption()
        lp.clickOnSignOut()
