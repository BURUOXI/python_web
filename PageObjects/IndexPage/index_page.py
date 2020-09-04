from selenium.webdriver.support.wait import WebDriverWait
from Common.plugs.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from Locators.IndexLocators.index_locators import IndexLocator as loc


class IndexPage(BasePage):
    # 继承了BasePage的类方法
    # def __init__(self, driver):
    #     self.driver = driver

    # 判断当前元素是否存在 存在返回True 否则返回false
    def isExist_logout_ele(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.logout_loc))
            return True
        except:
            return False

    def createpage_company(self):
        doc = '过渡页面_创建新公司'
        self.click_element(loc.create_company, doc)

    def applypage_company(self):
        doc = '过渡页面_申请加入公司'
        self.click_element(loc.apply_company, doc)

    def enterpage_personal(self):
        doc = '过渡页面_申请加入公司'
        self.click_element(loc.login_personal, doc)

    def enterpage_company(self):
        doc = '过渡页面_申请加入公司'
        self.click_element(loc.login_company, doc)


