#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/16 15:07
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# 企业成员页面
class BusinessMemberPage(BasePage):
    __BTN__ADD_MEMBER = (By.XPATH, "//*[text()=' 添加成员 ']")
    __TEXT_TIPS = (By.XPATH, "//*[text()='成员添加成功!']")

    # 点击“添加成员”按钮
    def click_add_member(self):
        self.do_find(self.__BTN__ADD_MEMBER).click()

        from pages.add_members_page import AddMemberPage
        return AddMemberPage(self.driver)

    def get_tips(self):
        self.wait_visible(self.__TEXT_TIPS)
        tips_value = self.do_find(self.__TEXT_TIPS).text
        return tips_value
