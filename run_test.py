#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/16 10:57
"""
import os
import pytest

if __name__ == '__main__':
    pytest.main(['-vs', './test_cases', '--alluredir=./result'])
    os.system('allure generate ./result -o ./report --clean')
