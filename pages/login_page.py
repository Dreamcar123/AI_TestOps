#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/13 9:23
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# 登录页面
class LoginPage(BasePage):
    ACCOUNT = (By.CSS_SELECTOR, ".el-input__inner")
    PASSWORD = (By.CSS_SELECTOR, "[type='password']")
    __BTN_LOGIN = (By.CSS_SELECTOR, ".el-button.submit-btn.el-button--default.el-button--medium")


    def login(self, account="15261074486", password="yechen123"):
        self.do_find(self.ACCOUNT).click()
        self.do_send_keys(account, self.ACCOUNT)
        self.do_find(self.PASSWORD).click()
        self.do_send_keys(password, self.PASSWORD)
        self.do_find(self.__BTN_LOGIN).click()

        from pages.project_list_page import ProjectListPage
        return ProjectListPage(self.driver)