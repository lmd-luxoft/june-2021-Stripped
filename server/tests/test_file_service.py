# coding=utf-8
from __future__ import print_function
import os
import random
import platform
import logging

import pytest

from server import file_service
from utilities import config_manager


class Test_change_dir:

    logging.basicConfig(filename='tests.log', encoding='utf-8')
    logger = logging.getLogger('tests')
    logger.setLevel(config_manager.config_load()['loggers']['tests'])

    def test_incorrect_type1(self):
        with pytest.raises(TypeError):
            file_service.change_dir(None)
        self.logger.info('End test')

    def test_incorrect_type2(self):
        with pytest.raises(TypeError):
            file_service.change_dir(int)

    def test_dot_dir(self):
        with pytest.raises(ValueError):
            file_service.change_dir(".")

    def test_incorrect_value2(self):
        with pytest.raises(ValueError):
            file_service.change_dir("..")
        logging.info('End test')

    def test_incorrect_value3(self):
        with pytest.raises(ValueError):
            file_service.change_dir('../something')
        logging.info('End test')

    def test_existing_dir_no_create(self):
        default_dir = os.getcwd()
        logging.info("before func: "+os.getcwd())
        file_service.change_dir(os.getcwd(), auto_create=False)
        logging.info("after func: "+os.getcwd())
        assert os.getcwd() == default_dir

    def test_existing_dir_create(self):
        default_dir = os.getcwd()
        logging.info("before func: "+os.getcwd())
        file_service.change_dir(os.getcwd(), auto_create=True)
        logging.info("after func: "+os.getcwd())
        assert os.getcwd() == default_dir

    def test_non_existing_dir_no_create(self):
        with pytest.raises(ValueError):
            n = random.randint(0, 5000)
            work_path = os.getcwd()
            print(platform.system())
            if platform.system() == "Linux":
                path = os.path.join(work_path, str(n))
                file_service.change_dir(path, False)
            elif platform.system() == "Windows":
                path = os.path.join(work_path, str(n))
                file_service.change_dir(path, False)
            else:
                logging.error("Unknown Operation System")
                raise OSError("Unknown Operation System")

    def test_non_existing_dir_create(self):
        n = random.randint(0, 5000)
        work_path = os.getcwd()
        if platform.system() == "Linux":
            path = os.path.join(work_path, str(n))
            file_service.change_dir(path, True)
        elif platform.system() == "Windows":
            path = os.path.join(work_path, str(n))
            file_service.change_dir(path, True)
        else:
            logging.error("Unknown Operation System")
            raise OSError("Unknown Operation System")
        assert os.getcwd() == path
