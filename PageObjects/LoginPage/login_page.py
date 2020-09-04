from Locators.LoginLocators.login_locators import LoginLocator as loc
from Common.plugs.basepage import BasePage


class LoginPage(BasePage):

    # 登录
    def login(self, username, password):
        doc = '登录页面_登录功能'
        self.input_element(loc.user_locator, username, doc)
        self.input_element(loc.pwd_locator, password, doc)
        self.click_element(loc.btn_locator, doc)

    # 获取错误提示:请输入手机号
    def get_login_errMsg(self):
        doc = '登录页面_登录功能错误信息_请输入手机号'
        # self.wait_eleVisible(loc.error_msg_loc)
        return self.get_element_text(loc.prompt_user, doc)

    def get_login_errorMsg(self):
        doc = '登录页面_登录功能错误信息_请输入密码'
        return self.get_element_text(loc.prompt_pwd, doc)

    def get_login_toastMsg(self):
        doc = '登录页面_登录功能错误信息_获取toast'
        return  self.get_element_text(loc.invalid_info_toast, doc)
