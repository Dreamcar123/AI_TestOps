#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/16 15:15
"""
from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddMemberPage(BasePage):
    __INPUT_MOBILE = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")
    __SELECT_MEMBER_ROLE = (By.CSS_SELECTOR, "[placeholder='请选择角色']")
    __SELECT_DOMESTIC_CONSUMER = (By.XPATH, "//*/div[9]/div[1]/div[1]/ul/li[3]")  # 普通用户
    __JOIN_PROJECT = (By.CSS_SELECTOR, ".el-select__input.is-medium")
    __SELECT_PROJECT = (By.XPATH, "//*[text()='Windows应用+安卓']")
    __BTN_CONFIRM = (By.XPATH, "//*[text()=' 确 认 ']")
    __BTN_CONFIRM_1 = (By.CSS_SELECTOR, ".el-button.el-button--default.el-button--small.el-button--primary ") # 确定

    # 填写成员信息
    def fill_in_member_info(self, mobile="15211111111"):
        self.do_send_keys(mobile, self.__INPUT_MOBILE)
        self.do_find(self.__SELECT_MEMBER_ROLE).click()
        self.wait_presence(self.__SELECT_DOMESTIC_CONSUMER)
        self.do_find(self.__SELECT_DOMESTIC_CONSUMER).click() # 选择普通用户
        self.do_find(self.__JOIN_PROJECT).click()
        self.do_find(self.__SELECT_PROJECT).click()
        self.do_find(self.__BTN_CONFIRM).click()
        # 确认添加成员
        self.do_find(self.__BTN_CONFIRM_1).click()

        from pages.business_member_page import BusinessMemberPage
        return BusinessMemberPage(self.driver)
