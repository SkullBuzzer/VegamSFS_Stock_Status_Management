import pytest

from PageObjects.LoginPage import LoginPage
from PageObjects.StockStatusManagementPage import StockStatusManagementPage
from PageObjects.StockStatus_321_QI_To_UU import StockStatus_321_QI_UU
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_002_StockStatus_321(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getuserName()
    password = ReadConfig.getPassword()
    log = LogGen.getLogger()

    @pytest.mark.skip
    def test_stockStatusChange_321(self):
        self.driver.implicitly_wait(10)
        self.log.info("************* Test_002_StockStatus_321 ***************")
        self.log.info("******** test stock status change_321 started ********")
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("***************** Login Successful *******************")
        ssmp = StockStatusManagementPage(self.driver)
        ssmp.clickOnStockReceipt()
        ssmp.clickOnGrMobile()
        ssmp.clickOnWarehouseOperation()
        ssmp.clickOnStockStatusModule()
        self.log.info("******* Accessed Stock status management page ********")
        ss_321 = StockStatus_321_QI_UU(self.driver)
        ss_321.clickOnSelectStorageLocation()
        ss_321.clickOnStorageLocation()
        ss_321.clickOnSearchIcon()
        status = ss_321.verifyDisplayedRecord()
        assert status == True
        status, material, batch, qty = ss_321.selectRecord_321()
        assert status == True
        ss_321.clickOnContinue()
        bin_location, req_qty, avail_qty = ss_321.getBinLocation(qty)
        ss_321.scanBinLocation().send_keys(bin_location)
        ss_321.clickOnPickButton()
        ss_321.scanRmLabel().send_keys("COAA006787")
        ss_321.enterQty(req_qty, avail_qty)
        ss_321.clickOnConfirm()
        status = ss_321.verifyMessage()
        assert status == True
        self.log.info("****** Updated the stock status for the scanned bin ******")
        ss_321.clickOnOK()
        ssmp.clickOnMobileGrid()
        ssmp.clickOnAdminOption()
        ss_321.clickOnWMConfiguration()
        ss_321.clickOnManageInventory()
        self.log.info("************* Accessed WM inventory module **************")
        ss_321.clickOnDefineSearchCriteria()
        ss_321.setMaterialCode().send_keys(material)
        ss_321.setBatchNo().send_keys(batch)
        ss_321.setBinLocation().send_keys(bin_location)
        ss_321.clickOnSearchButton()
        status = ss_321.verifyStockStatus()
        assert status == True
        self.log.info("*********** Stock status updated from QI to UU **************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()
        self.log.info("*********** test stock status change_321 passed **************")

    def test_stockStatus_321_partially(self):
        self.driver.implicitly_wait(10)
        self.log.info("************* Test_002_StockStatus_321 ***************")
        self.log.info("******** test stock status change_321 started ********")
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("***************** Login Successful *******************")
        ssmp = StockStatusManagementPage(self.driver)
        ssmp.clickOnStockReceipt()
        ssmp.clickOnGrMobile()
        ssmp.clickOnWarehouseOperation()
        ssmp.clickOnStockStatusModule()
        self.log.info("******* Accessed Stock status management page ********")
        ss_321 = StockStatus_321_QI_UU(self.driver)
        ss_321.clickOnSelectStorageLocation()
        ss_321.clickOnStorageLocation()
        ss_321.clickOnSearchIcon()
        status = ss_321.verifyDisplayedRecord()
        assert status == True
        status, material, batch, qty = ss_321.selectRecord_321()
        assert status == True
        ss_321.clickOnContinue()
        bin_location, req_qty, avail_qty = ss_321.getBinLocation(qty)
        ss_321.scanBinLocation().send_keys(bin_location)
        ss_321.clickOnPickButton()
        ss_321.scanRmLabel().send_keys("COAA006787")
        ss_321.enterQty(req_qty, avail_qty)
        ss_321.clickOnMoveStock()
        proposedBin = ss_321.getProposedBin()
        ss_321.scanProposedBin().send_keys(proposedBin)
        ss_321.clickOnConfirmPint()
        status = ss_321.verifyConfirmMessage()
        assert status == True
        self.log.info("*** Successfully transferred req qty different bin ***")
        ss_321.clickOnOkButton()
        ss_321.clickOnBackButton()
        ss_321.scanBinLocation().send_keys(bin_location)
        ss_321.clickOnPickButton()
        ss_321.scanRmLabel().send_keys("COAA006787")
        ss_321.enterQty(req_qty, avail_qty)
        ss_321.clickOnConfirm()
        status = ss_321.verifyMessage()
        assert status == True
        self.log.info("****** Updated the stock status for the scanned bin ******")
        ss_321.clickOnOK()
        ssmp.clickOnMobileGrid()
        ssmp.clickOnAdminOption()
        ss_321.clickOnWMConfiguration()
        ss_321.clickOnManageInventory()
        self.log.info("************* Accessed WM inventory module **************")
        ss_321.clickOnDefineSearchCriteria()
        ss_321.setMaterialCode().send_keys(material)
        ss_321.setBatchNo().send_keys(batch)
        ss_321.setBinLocation().send_keys(bin_location)
        ss_321.clickOnSearchButton()
        status = ss_321.verifyStockStatus()
        assert status == True
        self.log.info("*********** Stock status updated from QI to UU **************")
        lp.clickOnSignOut()
        self.log.info("********** test_stockStatus_321_partially passed ***********")














