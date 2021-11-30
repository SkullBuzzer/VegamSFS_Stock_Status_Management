import time

from selenium.webdriver import ActionChains
import re


class StockStatus_321_QI_UU:
    btnSelectStorageLoc_xpath = "//div[@id='divScrapMaterialListContent']/div[2]/div/div/div/button"
    btnStorageLocation_xpath = "//div[@id='divScrapMaterialListContent']/div[2]/div/div/div/div/ul/li[5]"
    iconSearch_xpath = "//div[@class='grid_1']/a"
    btnContinue_xpath = "//div[@class='pull-right grid_6']/a"
    txtBinLocation_xpath = "//input[@id='txtScanBinValue']"
    btnPick_xpath = "//a[@id='hypPick']"
    txtLabelScan_xpath = "//input[@id='txtScanLabel']"
    txtPickQty_id = "txtPickedQty"
    btnConfirm_xpath = "//button[@class='btn-success ui-btn ui-icon-printer ui-btn-icon-right ui-mini']"
    btnOK_xpath = "//a[text()='OK']"
    moduleWarehouse_xpath = "//a[@id='ContentPlaceHolder1_lnkWarehouseConfiguration']/div"
    moduleInventory_id = "ContentPlaceHolder1_lnkWarehouseStock"
    lnkDefSearch_xpath = "//div[@class='mr-3']"
    btnSearch_xpath = "//fieldset[@class='search-block position-relative']/div[2]/div/button"
    btnMoveStock_xpath = "//div[@class='ZebraDialog_Buttons']/a[2]"
    txtScanBin_id = "txtNewBin"
    btnConfPrint_id = "hypPrintLabelBtn"

    def __init__(self, driver):
        self.driver = driver

    def clickOnSelectStorageLocation(self):
        self.driver.find_element_by_xpath(self.btnSelectStorageLoc_xpath).click()

    def clickOnStorageLocation(self):
        self.driver.find_element_by_xpath(self.btnStorageLocation_xpath).click()

    def clickOnSearchIcon(self):
        self.driver.find_element_by_xpath(self.iconSearch_xpath).click()

    def getRows(self):
        return len(self.driver.find_elements_by_xpath("//tbody[@id='tbody_256']/tr"))

    def verifyDisplayedRecord(self):
        n = self.getRows()
        exp_stLoc = "CJ01"
        flag = False
        for r in range(1, n + 1):
            action = ActionChains(self.driver)
            element = self.driver.find_element_by_xpath("//tbody[@id='tbody_256']/tr[" + str(r) + "]/td[7]")
            action.move_to_element(element).perform()
            time.sleep(2)
            act_stLoc = self.driver.find_element_by_xpath("//tbody[@id='tbody_256']/tr[" + str(r) + "]/td[7]").text
            if act_stLoc == exp_stLoc:
                flag = True
            else:
                self.driver.get_screenshot_as_file("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Stock_Status_Management"
                                                   "\\Screenshots\\StockStatus_321.png")
        return flag

    def selectRecord_321(self):
        global act_mat, batch, qty
        n = self.getRows()
        exp_movt = "321"
        flag = False
        for r in range(1, n + 1):
            act_movt = self.driver.find_element_by_xpath("//tbody[@id='tbody_256']/tr[" + str(r) + "]/td[9]").text
            if act_movt == exp_movt:
                self.driver.find_element_by_xpath("//tbody[@id='tbody_256']/tr[" + str(r) + "]/td[1]").click()
                material = self.driver.find_element_by_xpath("//tbody[@id='tbody_256']/tr[" + str(r) + "]/td[2]").text
                l = material.split('/')
                act_mat = l[0]
                batch = self.driver.find_element_by_xpath("//tbody[@id='tbody_256']/tr[" + str(r) + "]/td[3]").text
                qty = self.driver.find_element_by_xpath("//tbody[@id='tbody_256']/tr[" + str(r) + "]/td[6]").text
                flag = True
                break
            else:
                self.driver.get_screenshot_as_file("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Stock_Status_Management"
                                                   "\\Screenshots\\StockStatus2_321.png")
        return flag, act_mat, batch, qty

    def clickOnContinue(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btnContinue_xpath).click()

    def getBinLocation(self, ReqQty):
        global bin_name, req_qty, avail_qty
        l = re.findall('\d*\.?\d+', ReqQty)
        req_qty = float(l[0])
        n = len(self.driver.find_elements_by_xpath("//table[@id='tableAvailableBins']/tbody/tr"))
        for r in range(1, n + 1):
            AvailQty = self.driver.find_element_by_xpath(
                "//table[@id='tableAvailableBins']/tbody/tr[" + str(r) + "]/td[5]").text
            l1 = re.findall('\d*\.?\d+', AvailQty)
            avail_qty = float(l1[0])
            if req_qty == avail_qty:
                bin_name = self.driver.find_element_by_xpath(
                    "//table[@id='tableAvailableBins']/tbody/tr[" + str(r) + "]/td[3]").text
            else:
                bin_name = self.driver.find_element_by_xpath(
                    "//table[@id='tableAvailableBins']/tbody/tr[" + str(r) + "]/td[3]").text
                break
        return bin_name, req_qty, avail_qty

    def scanBinLocation(self):
        return self.driver.find_element_by_xpath(self.txtBinLocation_xpath)

    def clickOnPickButton(self):
        self.driver.find_element_by_xpath(self.btnPick_xpath).click()
        time.sleep(5)

    def scanRmLabel(self):
        return self.driver.find_element_by_xpath(self.txtLabelScan_xpath)

    def enterQty(self, reqQty, availQty):
        time.sleep(3)
        if reqQty <= availQty:
            self.driver.find_element_by_id(self.txtPickQty_id).send_keys(str(reqQty))
        else:
            self.driver.find_element_by_id(self.txtPickQty_id).send_keys(str(availQty))

    def clickOnConfirm(self):
        self.driver.find_element_by_xpath(self.btnConfirm_xpath).click()
        time.sleep(5)

    def verifyMessage(self):
        act_msg = self.driver.find_element_by_xpath("//div[text()='Successfully updated stock status']").text
        exp_msg = "Successfully updated stock status"
        flag = False
        if act_msg == exp_msg:
            flag = True
        else:
            self.driver.get_screenshot_as_file("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Stock_Status_Management"
                                               "\\Screenshots\\StockStatus_pick_321.png")
        return flag

    def clickOnOK(self):
        self.driver.find_element_by_xpath(self.btnOK_xpath).click()
        time.sleep(5)

    def clickOnWMConfiguration(self):
        self.driver.find_element_by_xpath(self.moduleWarehouse_xpath).click()
        time.sleep(3)

    def clickOnManageInventory(self):
        self.driver.find_element_by_id(self.moduleInventory_id).click()
        time.sleep(5)

    def clickOnDefineSearchCriteria(self):
        self.driver.find_element_by_xpath(self.lnkDefSearch_xpath).click()
        time.sleep(1)

    def setMaterialCode(self):
        return self.driver.find_element_by_xpath("//input[@id='txt_3791']")

    def setBatchNo(self):
        return self.driver.find_element_by_xpath("//input[@id='txt_3794']")

    def setBinLocation(self):
        return self.driver.find_element_by_xpath("//input[@id='txt_3795']")

    def clickOnSearchButton(self):
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()
        time.sleep(5)

    def verifyStockStatus(self):
        act_stockStatus = self.driver.find_element_by_xpath(
            "//table[@class='table table-bordered table-striped']/tbody/tr/td[8]").text
        flag = False
        if act_stockStatus != 'Q':
            flag = True
        else:
            self.driver.get_screenshot_as_file("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Stock_Status_Management"
                                               "\\Screenshots\\StockStatus_inventory_321.png")
        return flag

    def clickOnMoveStock(self):
        self.driver.find_element_by_xpath(self.btnMoveStock_xpath).click()
        time.sleep(5)

    def getProposedBin(self):
        element = self.driver.find_element_by_xpath("//input[@id='txtProposedBin']")
        self.driver.execute_script("arguments[0].removeAttribute('disabled')", element)
        proposed_bin = self.driver.find_element_by_xpath("//input[@id='txtProposedBin']").get_attribute("value")
        return proposed_bin

    def scanProposedBin(self):
        return self.driver.find_element_by_id(self.txtScanBin_id)

    def clickOnConfirmPint(self):
        self.driver.find_element_by_id(self.btnConfPrint_id).click()
        time.sleep(5)

    def verifyConfirmMessage(self):
        act_msg = self.driver.find_element_by_xpath("//div[text()='Movement is successful.']").text
        exp_msg = "Movement is successful."
        flag = False
        if act_msg == exp_msg:
            flag = True
        else:
            self.driver.get_screenshot_as_file("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Stock_Status_Management"
                                               "\\Screenshots\\StockStatus_partial_321.png")
        return flag

    def clickOnOkButton(self):
        self.driver.find_element_by_xpath("//a[@class='ZebraDialog_Button_0']").click()
        time.sleep(2)

    def clickOnBackButton(self):
        self.driver.find_element_by_id("hypBack").click()
        time.sleep(3)

