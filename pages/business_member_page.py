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
    __TEXT_MOBILE = (By.CSS_SELECTOR, ".el-table__row.el-table__row--striped:nth-child(2)")


    # 点击“添加成员”按钮
    def click_add_member(self):
        self.do_find(self.__BTN__ADD_MEMBER).click()

        from pages.add_members_page import AddMemberPage
        return AddMemberPage(self.driver)

    # 添加成功提示
    def get_tips(self):
        self.wait_visible(self.__TEXT_TIPS)
        tips_value = self.do_find(self.__TEXT_TIPS).text
        return tips_value

    # 获取成员列表信息
    def get_member_info(self):
        # 刷新页面
        self.do_refresh()

        ele_list = self.do_finds(self.__TEXT_MOBILE)
        member_info_list = []
        # 遍历元素列表，通过元素的text属性，提取文本数据信息
        for ele in ele_list:
            member_info_list.append(ele.text)
        # print(member_info_list)
        return member_info_list

