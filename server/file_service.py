import os
import sys
import re
import platform


def print_current_work_dir():
    print("Current working directory: {0}".format(os.getcwd()))


def validate_path(path):
    if platform.system() == "Windows":
        validator = bool(re.match(r"[a-zA-Z]:\\((?:.*?\\)*).*", path))
    if platform.system() == "Linux":
        validator = bool(re.match(r"^[a-zA-Z0-9]?(/[^/ ]*)+/?$", path))
    return validator


def change_dir(path, auto_create=False):
    if validate_path(path):
        pass
    else:
        raise ValueError("Cant validate linux or windows path")
    if os.path.isdir(path) and not auto_create:
        os.chdir(path)
    elif not os.path.isdir(path) and auto_create:
        os.makedirs(path)
        os.chdir(path)
    elif not auto_create and not os.path.isdir(path):
        raise ValueError("add flag auto_create or create dir")
    elif os.getcwd() == path:
        print('already in this directory')
    else:
        raise ValueError('cant create dir or something wrong')


def get_files():
    get_files_list = os.listdir(os.getcwd())
    get_files_list_info = [{}]
    for file in get_files_list:
        get_files_list_info.append(get_file_data(file))

    print(get_files_list_info)
    return get_files_list_info


def read_file_content(filename):
    try:
        with open(filename, "r") as f:
            file_content = f.read()
    except OSError as ex:
        print(ex)
    return file_content


def get_file_data(filename):
    if os.path.isfile(filename):
        file_info = {
            'name': os.path.basename(filename),
            'content': read_file_content(filename),
            'create_date': os.path.getctime(filename),
            'edit_date': os.path.getmtime(filename),
            'size': os.path.getsize(filename)}
    else:
        print("File doesn't exist")
    return file_info


def create_file(filename, content=None):
    try:
        f = open(filename, "w")
        if content is not None:
            f.write(content + f.name)
        else:
            f.write(content)
        f.close()
    except Exception as ex:
        print(ex)


def delete_file(filename):
    try:
        os.remove(filename)
    except Exception as ex:
        print(ex)
