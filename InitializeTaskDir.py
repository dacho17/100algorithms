#######################################################################
##
##  Author: David Dosenovic
##  This script creates a new task directory.
##  Terminal run format: python InitializeTaskDir.py <new_folder_name>
##  Example of the script run: python InitializeTaskDir.py 999NewTask
##
#######################################################################

import os
import sys

class DirInitializer(object):
    def __init__(self):
        self.template_dir = "000TaskTemplate/"
        self.notes = "notes.txt"
        self.test_suite = "TestSuite.py"
        self.main = "_main.py"

    def create_dir(self, dir_name):
        cur_dir = os.path.abspath(os.getcwd())
        new_dir = cur_dir + "/" + dir_name

        if not os.path.exists(new_dir):
            os.makedirs(new_dir)    # create a directory
        return
    
    def get_contents(self):
        files_to_visit = [self.notes, self.test_suite, self.main]

        res = []
        for cur in files_to_visit:
            with open(self.template_dir + cur) as cur_file:
                lines = cur_file.readlines()
                lines = [line.rstrip() for line in lines]
            res.append(lines)

        return res[0], res[1], res[2]

    def create_notes(self, dir_name, lines):    # create notes.txt file with the content
        f = open(dir_name + "/" + self.notes, "w+")
        f.writelines(line + '\n' for line in lines)
        f.close()

    def create_suite(self, dir_name, lines):    # create <taskName>TestSuite.py with the content
        f = open(dir_name + "/" + dir_name[3:] + self.test_suite, "w+")
        f.writelines(line + '\n' for line in lines)
        f.close()

    def create_main(self, dir_name, lines):     # create a copy of _main.py
        f = open(dir_name + "/" + self.main, "w+")
        f.writelines(line + '\n' for line in lines)
        f.close()

    def create_task(self, dir_name):    # create <taskName>.py empty file
        f = open(dir_name + "/" + dir_name[3:] + ".py", "w+")
        f.writelines("")
        f.close()


def initialize_task():
    dir_name = sys.argv[1]
    initializer = DirInitializer()
    initializer.create_dir(dir_name)
    notes_cont, t_suite_cont, main_cont = initializer.get_contents()
    initializer.create_notes(dir_name, notes_cont)
    initializer.create_suite(dir_name, t_suite_cont)
    initializer.create_main(dir_name, main_cont)
    initializer.create_task(dir_name)


initialize_task()
