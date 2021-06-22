import os


def change_dir(path):
    if os.path.isdir(path):
        print("Current working directory: {0}".format(os.getcwd()))
        os.chdir(path)
        print("Current working directory after parse: {0}".format(os.getcwd()))
    else:
        print("Current working directory: {0}".format(os.getcwd()))
        os.makedirs(path)
        os.chdir(path)
        print("Current working directory after parse: {0}".format(os.getcwd()))
    pass


def get_files():
    getfileslist = os.listdir(os.getcwd())
    getfileslistinfo=[{}]
    for file in getfileslist:
        getfileslistinfo.append(get_file_data(file))

    print(getfileslistinfo)
    return getfileslistinfo


def read_file_content(filename):
    with open(filename, "r") as f:
        filecontent = f.read()
    return filecontent

def get_file_data(filename):
    fileinfo = {
        'name' : os.path.basename(filename),
        'content': read_file_content(filename),
        'create_date': os.path.getctime(filename),
        'edit_date': os.path.getmtime(filename),
        'size': os.path.getsize(filename)
               }
    return fileinfo

def create_file(filename, content=None):
    f=open(filename,"w")
    f.write(content+f.name)
    f.close()
    pass


def delete_file(filename):
    os.remove(filename)
    pass
