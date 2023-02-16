#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/16 14:43
"""
import allure
import pytest
from pages.login_page import LoginPage


class TestAddMember:
    def setup_class(self):
        self.browser = LoginPage()

    def teardown_class(self):
        self.browser.do_quit()

    @allure.story('管理模块 - 正常用例测试')
    @allure.title('添加成员 - 正向用例')
    @pytest.mark.usefixtures('add_member')
    @pytest.mark.run(order=1)
    def test_add_member(self):
        member_info_list = self.browser.login() \
            .click_admin_manage() \
            .click_business_member() \
            .click_add_member() \
            .fill_in_member_info()\
            .get_member_info()
        # assert "成员添加成功!" == value
        assert "15211111111" in member_info_list[0]
