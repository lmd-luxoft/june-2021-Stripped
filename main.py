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
    fileService.change_dir()
    pass


def command_get_files():
    fileService.get_files()
    pass


def command_get_file_data():
    fileService.get_file_data()
    pass


def command_create_file():
    fileService.create_file()
    pass


def command_delete_file():
    fileService.delete_file()
    pass


def main():
    """Entry point of app.

    Get and parse command line parameters and configure web app.

    Command line options:
    -f --folder - working directory (absolute or relative path, default: current app folder).
    -h --help - help.
    """

    pass


if __name__ == '__main__':
    main()
