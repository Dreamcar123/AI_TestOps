#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/13 9:22
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# 新建项目页面
class AddProjectPage(BasePage):
    __INPUT_PROJECT_NAME = (By.CSS_SELECTOR, "[placeholder='请输入项目名称']")
    __BTN_PROJECT_TYPE = (By.CSS_SELECTOR, "[placeholder='请选择项目类型']")
    __INPUT_APPLICATION_TYPE = (By.XPATH, "//*/div[9]/div[1]/div[1]/ul/li[1]")
    __INPUT_WEB_URL = (By.CSS_SELECTOR, "[placeholder='请输入URL']")
    __INPUT_SOFTWARE_VERSION = (By.CSS_SELECTOR, "[placeholder='请输入软件版本']")
    __BTN_CONFIRM = (By.XPATH, "//*[text()='确定']")

    def fill_in_info(self, project_name="test_Auto", url="https://www.baidu.com/", software_version="2023"):
        self.do_send_keys(project_name, self.__INPUT_PROJECT_NAME)
        self.do_find(self.__BTN_PROJECT_TYPE).click()
        self.do_find(self.__INPUT_APPLICATION_TYPE).click()#/html/body/div[9]/div[1]/div[1]/ul/li[1]
        self.do_send_keys(url, self.__INPUT_WEB_URL)
        self.do_send_keys(software_version, self.__INPUT_SOFTWARE_VERSION)
        self.do_find(self.__BTN_CONFIRM).click()

        from pages.project_list_page import ProjectListPage
        return ProjectListPage(self.driver)
