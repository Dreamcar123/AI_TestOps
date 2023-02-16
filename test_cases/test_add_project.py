#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/13 9:38
"""
import allure
import pytest

from pages.login_page import LoginPage



class TestAddProject:
    def setup_class(self):
        # 打开登录页
        self.browser = LoginPage()

    def teardown_class(self):
        self.browser.do_quit()

    @allure.story('项目模块 - 正常用例测试')
    @allure.title('新建项目 - 正向用例')
    @pytest.mark.usefixtures('add_project')
    @pytest.mark.run(order=1)
    def test_add_project(self, add_project):
        # self.logger = add_project
        project_list = self.browser.login() \
                            .click_add_project() \
                            .fill_in_info()\
                            .get_project_list()

        assert "test_Auto" in project_list
