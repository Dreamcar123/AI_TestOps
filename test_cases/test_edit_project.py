#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/13 10:12
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
    @allure.title('编辑项目 - 正向用例')
    @pytest.mark.usefixtures('edit_project')
    @pytest.mark.run(order=2)
    def test_edit_project_name(self):
        project_list = self.browser.login() \
            .click_edit() \
            .edit_project_name() \
            .get_project_list()
        assert "test_芒果TV" in project_list
