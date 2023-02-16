#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/13 10:14
"""
import allure
import pytest
from pages.login_page import LoginPage


class TestDeleteProject:
    def setup_class(self):
        # 打开登录页
        self.browser = LoginPage()

    def teardown(self):
        self.browser.do_quit()

    @allure.story('项目模块 - 正常用例测试')
    @allure.title('删除项目 - 正向用例')
    @pytest.mark.usefixtures('delete_project')
    @pytest.mark.run(order=3)
    def test_delete_project(self):
        project_list = self.browser.login() \
            .click_delete() \
            .get_project_list()
        assert "test_Auto" not in project_list
