#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/13 9:22
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# 编辑项目页面
class EditProject(BasePage):
    __PROJECT_NAME = (By.XPATH, "//*/div[2]//form/div[1]/div[1]/div/input")
    __BTN_SAVE = (By.XPATH, "//*[text()='保存']")

    def edit_project_name(self, project_name="test_芒果TV"):
        # 修改项目名称
        self.wait_clickable(self.__PROJECT_NAME)
        self.do_find(self.__PROJECT_NAME).clear()
        self.do_send_keys(project_name, self.__PROJECT_NAME)
        # 点击“保存”按钮
        self.do_find(self.__BTN_SAVE).click()

        from pages.project_list_page import ProjectListPage
        return ProjectListPage(self.driver)