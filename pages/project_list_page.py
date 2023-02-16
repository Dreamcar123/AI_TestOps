#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/13 9:23
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# 项目列表页面
class ProjectListPage(BasePage):
    __BTN_ADD_PROJECT = (By.CSS_SELECTOR, ".el-button.el-button--primary.el-button--medium")
    __PROJECT_NAME = (By.CSS_SELECTOR, ".text")
    BTN_MORE = (By.CSS_SELECTOR, ".circleIcon")
    __BTN_DELETE = (By.XPATH, "//*[@x-placement='bottom-end']/li[3]/span")
    __BTN_CONFIRM = (By.CSS_SELECTOR, ".el-button.el-button--default.el-button--small.el-button--primary")
    __BTN_EDIT = (By.XPATH, "//*[@x-placement='bottom-end']/li[1]/span")
    __BTN_ADMIN_MANAGE = (By.XPATH, "//*[text()='管理']")

    # 点击“新建项目”按钮
    def click_add_project(self):
        self.wait_clickable(self.__BTN_ADD_PROJECT)
        self.do_find(self.__BTN_ADD_PROJECT).click()

        from pages.add_project_page import AddProjectPage
        return AddProjectPage(self.driver)

    # 点击“删除”按钮
    def click_delete(self):
        # 悬停
        ele_more = self.do_find(self.BTN_MORE)
        self.move_to_element(ele_more)
        # 点击”删除“按钮
        self.wait_clickable(self.__BTN_DELETE)
        self.do_find(self.__BTN_DELETE).click()
        self.do_find(self.__BTN_CONFIRM).click()

        return ProjectListPage(self.driver)

    # 点击“编辑”按钮
    def click_edit(self):
        # 悬停
        ele_more = self.do_find(self.BTN_MORE)
        self.move_to_element(ele_more)
        self.wait_clickable(self.__BTN_EDIT)
        self.do_find(self.__BTN_EDIT).click()

        from pages.edit_project_page import EditProject
        return EditProject(self.driver)

    # 获取项目列表名称
    def get_project_list(self):
        # 刷新
        self.do_refresh()
        # 获取元素列表
        ele_list = self.do_finds(self.__PROJECT_NAME)
        # 获取项目名称
        name_list = []
        for ele in ele_list:
            name_list.append(ele.text)
        return name_list

    # 点击“管理”按钮
    def click_admin_manage(self):
        self.do_find(self.__BTN_ADMIN_MANAGE).click()

        from pages.admin_manage_page import AdminManagePage
        return AdminManagePage(self.driver)

