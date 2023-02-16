#!/usr/bin/python
# encoding: utf-8
"""
@author: YeChen
@time: 2023/1/16 10:51
"""
import pytest
from utils.log_util import LoggerUtil


@pytest.fixture(name = 'add_project')
def add_project():
    lu = LoggerUtil()
    logger = lu.get_logger()
    logger.info("新建项目")
    lu.remove_handler()

@pytest.fixture(name = 'edit_project')
def edit_project():
    lu = LoggerUtil()
    logger = lu.get_logger()
    logger.info("编辑项目")
    lu.remove_handler()

@pytest.fixture(name = 'delete_project')
def delete_project():
    lu = LoggerUtil()
    logger = lu.get_logger()
    logger.info("删除项目")
    lu.remove_handler()

@pytest.fixture(name = 'add_member')
def add_member():
    lu = LoggerUtil()
    logger = lu.get_logger()
    logger.info("添加成员")
    lu.remove_handler()