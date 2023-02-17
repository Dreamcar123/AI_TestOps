#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/13 9:21
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """与浏览器driver交互"""
    _BASE_URL = "https://test.dragontesting.net/login"

    # 构造方法
    def __init__(self, base_driver=None):
        if base_driver:
            self.driver = base_driver
        else:
            "实例化"
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)

        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL)

    def do_refresh(self):
        """刷新"""
        self.driver.refresh()

    def do_find(self, by, locator=None):
        """获取单个元素"""
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def do_finds(self, by, locator=None):
        """获取多个元素"""
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, value, by, locator=None):
        """输入文本"""
        ele = self.do_find(by, locator)
        ele.clear()
        ele.send_keys(value)

    def do_quit(self):
        self.driver.quit()

    def wait_presence(self, locator: tuple):
        """
        显示等待
        判断某个元素是否被加到了dom树里，并不代表该元素一定可见
        """
        return WebDriverWait(self.driver, 30, 0.5).until(expected_conditions.presence_of_element_located(locator), "没找到元素")

    def wait_visible(self, locator:tuple):
        """
        显示等待
        判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
        """
        return WebDriverWait(self.driver, 30, 0.5).until(expected_conditions.visibility_of_element_located(locator))

    def wait_clickable(self, locator:tuple):
        """
        显示等待
        判断某个元素中是否可见并且是可以点击，如果是的就返回这个元素，否则返回False
        """
        return WebDriverWait(self.driver, 30, 0.5).until(expected_conditions.element_to_be_clickable(locator))

    def move_to_element(self, locator: tuple):
        """悬停"""
        return ActionChains(self.driver).move_to_element(locator).perform()


