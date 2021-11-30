import time

from selenium.common.exceptions import NoSuchElementException


class StockStatusManagementPage:
    lnkStockReceipt_id = "lnkStockReceipt"
    lnkGrMobile_css = "a[id='ContentPlaceHolder1_lnkGRMobile']"
    lnkWarehouseOperation_xpath = "//a[@id='ContentPlaceHolder_lnkBinToBin']/div"
    txtModuleName_xpath = "//a[@id='ContentPlaceHolder_lnkManageStockStatus']/div/div[2]/h4"
    gridMobile_xpath = "//a[@id='hdrToggle']"
    optionAdmin_xpath = "//a[@id='lnkAdmin']"
    lnkStockStatus_xpath = "//a[@id='ContentPlaceHolder_lnkManageStockStatus']/div"
    txtStockStatusPage_xpath = "//div[@id='divScrapMaterialListContent']/div[1]/h3"

    def __init__(self, driver):
        self.driver = driver

    def clickOnStockReceipt(self):
        self.driver.find_element_by_id(self.lnkStockReceipt_id).click()

    def clickOnGrMobile(self):
        self.driver.find_element_by_css_selector(self.lnkGrMobile_css).click()

    def clickOnWarehouseOperation(self):
        self.driver.find_element_by_xpath(self.lnkWarehouseOperation_xpath).click()

    def verifyPresenceOfModule(self):
        time.sleep(3)
        flag = False
        try:
            act_module = self.driver.find_element_by_xpath(self.txtModuleName_xpath).text
            exp_module = "Stock Status Management"
            if act_module == exp_module:
                flag = True
        except NoSuchElementException:
            self.driver.get_screenshot_as_file("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Stock_Status_Management"
                                               "\\Screenshots\\StockStatus.png")
            print("Stock status management module is not available under warehouse operation")
        return flag

    def clickOnMobileGrid(self):
        self.driver.find_element_by_xpath(self.gridMobile_xpath).click()

    def clickOnAdminOption(self):
        self.driver.find_element_by_xpath(self.optionAdmin_xpath).click()

    def clickOnStockStatusModule(self):
        self.driver.find_element_by_xpath(self.lnkStockStatus_xpath).click()

    def verifyStockStatusPage(self):
        act_page = self.driver.find_element_by_xpath(self.txtStockStatusPage_xpath).text
        exp_page = "List of stock status changed batches pending for bin location assignment"
        if act_page == exp_page:
            flag = True
        else:
            self.driver.get_screenshot_as_file("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Stock_Status_Management"
                                               "\\Screenshots\\StockStatusPage.png")
            flag = False
        return flag


