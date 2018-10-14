# https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832
# https://github.com/yeraydiazdiaz/wtmock
# Author: Yeray Diaz

import os

def work_on():
    path = os.getcwd()
    print(f'Working on {path}')
    return path


class Helper:

    def __init__(self, path):
        self.path = path

    def get_path(self):
        base_path = os.getcwd()
        return os.path.join(base_path, self.path)


class Worker:

    def __init__(self):
        self.helper = Helper('db')

    def work(self):
        path = self.helper.get_path()
        print(f'Working on {path}')
        return path
