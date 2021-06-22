import os


def print_current_work_dir():
    print("Current working directory: {0}".format(os.getcwd()))


def change_dir(path):
    if os.path.isdir(path):
        os.chdir(path)
    else:
        try:
            os.makedirs(path)
            os.chdir(path)
        except Exception as ex:
            print(ex)


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
    except Exception as ex:
        print(ex)
    return file_content


def get_file_data(filename):
    try:
        file_info = {
            'name': os.path.basename(filename),
            'content': read_file_content(filename),
            'create_date': os.path.getctime(filename),
            'edit_date': os.path.getmtime(filename),
            'size': os.path.getsize(filename)
        }
    except Exception as ex:
        print(ex)
    return file_info


def create_file(filename, content=None):
    try:
        f = open(filename, "w")
        f.write(content + f.name)
        f.close()
    except Exception as ex:
        print(ex)


def delete_file(filename):
    try:
        os.remove(filename)
    except Exception as ex:
        print(ex)


