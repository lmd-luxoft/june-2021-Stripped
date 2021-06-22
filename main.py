#!/usr/bin/env python2
import argparse
import server.FileService as fileService


def commandline_parser():
    parser = argparse.ArgumentParser(description='Process parameters for application')
    parser.add_argument('-p', '--port', type=int, help='parameter for setting port to fileserver')
    parser.add_argument('-d', '--directory', type=str, help='parameter for setting working directory')

    args = parser.parse_args()
    return args


def command_change_dir():
    change_dir = raw_input("Please enter path to dir: ")
    fileService.change_dir(change_dir)
    pass


def command_get_files():
    return fileService.get_files()


def command_get_file_data():
    filename = raw_input("Enter path with file name: ")
    return fileService.get_file_data(filename)


def command_create_file():
    filename = raw_input("Enter path with file name: ")
    content = raw_input("Enter file content")
    return fileService.create_file(filename, content)


def command_delete_file():
    filename = raw_input("Enter path with file name: ")
    return fileService.delete_file(filename)


def main():
    args = commandline_parser()

    try:
        fileService.change_dir(args.directory)
    except:
        print("Console param is None")

    while True:
        print('\n'
                  'Available operations:' + '\n'
                  '1-Change work dir' + '\n'
                  '2-Get files in work dir' + '\n'
                  '3-Get file data' + '\n'
                  '4-Create file' + '\n'
                  '5-Delete file' + '\n'
                  '6-Exit app' + '\n')
        cmd = raw_input('Enter a command')
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
            break
        else:
            print "Invalid command."
    """Entry point of app.

    Get and parse command line parameters and configure web app.

    Command line options:
    -f --folder - working directory (absolute or relative path, default: current app folder).
    -h --help - help.
    """

    pass


if __name__ == '__main__':
    main()
