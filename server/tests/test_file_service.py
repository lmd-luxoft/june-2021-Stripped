# coding=utf-8
import os
import random
import string
import platform

import pytest

from server import file_service


class Test_change_dir:

    def test_incorrect_type1(self):
        with pytest.raises(TypeError):
            file_service.change_dir(None)

    def test_incorrect_type2(self):
        with pytest.raises(TypeError):
            file_service.change_dir(int)

    def test_dot_dir(self):
        with pytest.raises(ValueError):
            file_service.change_dir(".")

    def test_incorrect_value2(self):
        with pytest.raises(ValueError):
            file_service.change_dir("..")

    def test_incorrect_value3(self):
        with pytest.raises(ValueError):
            file_service.change_dir('../something')

    def test_existing_dir_no_create(self):
        default_dir = os.getcwd()
        file_service.change_dir(os.getcwd(), auto_create=False)
        print(os.getcwd())
        assert os.getcwd() == default_dir

    def test_existing_dir_create(self):
        default_dir = os.getcwd()
        file_service.change_dir(os.getcwd(), auto_create=True)
        print(os.getcwd())
        assert os.getcwd() == default_dir

    def test_non_existing_dir_no_create(self):
        n = random.randint(0, 5000)
        work_path = os.getcwd()
        print(platform.system())
        if platform.system() == "Linux":
            path = string.join(work_path, '/', str(n))
            file_service.change_dir(path, True)
        elif platform.system() == "Windows":
            path = string.join(work_path, '\\', str(n))
            file_service.change_dir(path, False)
        else:
            print ("Unknown Operation System")
        assert os.getcwd() == work_path

    def test_non_existing_dir_create(self):
        n = random.randint(0, 5000)
        work_path = os.getcwd()
        if platform.system() == "Linux":
            path = string.join(work_path, '/' + str(n))
            file_service.change_dir(path, True)
        elif platform.system() == "Windows":
            path = string.join(work_path, '\\'+str(n))
            file_service.change_dir(path, True)
        else:
            print ("Unknown Operation System")
        assert os.getcwd() == path
