#!/usr/bin/env python2
import argparse
import server.file_service as file_service
import utilities.config_manager as config_manager


def commandline_parser():
    parser = argparse.ArgumentParser(description='Process parameters for application')
    parser.add_argument('-p', '--port', type=int, help='parameter for setting port to fileserver')
    parser.add_argument('-d', '--directory', type=str, help='parameter for setting working directory')

    args = parser.parse_args()
    return args


def command_change_dir():
    change_dir = raw_input("Please enter path to dir: ")
    file_service.change_dir(change_dir)


def command_get_files():
    return file_service.get_files()


def command_get_file_data():
    filename = raw_input("Enter path with file name: ")
    return file_service.get_file_data(filename)


def command_create_file():
    filename = raw_input("Enter path with file name: ")
    content = raw_input("Enter file content")
    return file_service.create_file(filename, content)


def command_delete_file():
    filename = raw_input("Enter path with file name: ")
    return file_service.delete_file(filename)


def main():
    args = commandline_parser()
    file_service.change_dir(config_manager.config_load()['workdir'])


    try:
        file_service.change_dir(args.directory)
    except:
        print("Console param is None")

    while True:
        print("""
        Available operations:
        1-Change work dir
        2-Get files in work dir
        3-Get file data
        4-Create file
        5-Delete file
        6-Print Current workdir
        7-Exit app
        """)
        cmd = raw_input('Enter a command'+'\n')
        if cmd == '1':
            command_change_dir()
        elif cmd == '2':
            command_get_files()
        elif cmd == '3':
            print(command_get_file_data())
        elif cmd == '4':
            command_create_file()
        elif cmd == '5':
            command_delete_file()
        elif cmd == '6':
            file_service.print_current_work_dir()
        elif cmd == '7':
            break
        else:
            print "Invalid command."


if __name__ == '__main__':
    main()
