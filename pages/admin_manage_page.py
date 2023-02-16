#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/16 14:20
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# 管理页面
class AdminManagePage(BasePage):
    __BTN_BUSINESS_MEMBER = (By.XPATH, "//*[text()=' 企业成员 ']")

    # 点击“企业成员”按钮
    def click_business_member(self):
        self.do_find(self.__BTN_BUSINESS_MEMBER).click()

        from pages.business_member_page import BusinessMemberPage
        return BusinessMemberPage(self.driver)