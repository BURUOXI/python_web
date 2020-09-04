from time import sleep

from Locators.createcompany.createCompany import CreatCompany as loc
from Common.plugs.basepage import BasePage


class CreatePage(BasePage):

    def create_licence(self, file_path):
        doc = '创建新企业_新增营业执照'
        self.upload_file(loc.upload_licence, file_path)


    def get_create_result_msg(self):
        doc = '创建新企业_新增营业执照_新增营业执照名称_获取新增营业执照名称'
        # self.wait_eleVisible(loc.user_add_dialog_msg, doc)
        sleep(2)
        return self.get_element_text(loc.licence_name, doc)


