# -*- coding:utf-8 -*-

from argparse import ArgumentParser
import glob
import os
import shutil


class MassCopier:
    def __init__(self, args):
        self.args = args
        self.args.filter = self.args.filter.lower()
        self.filters = self.args.filter.split(",")

    def get_file_ext(self, filename):
        return filename.lower().split(".")[-1]

    def copy_dir(self, directory):
        i_dir = glob.iglob(os.path.join(directory, "*"))
        for i_item in i_dir:
            if os.path.isdir(i_item):
                print("Entering {}".format(os.path.basename(i_item)))
                self.copy_dir(i_item)
            elif os.path.isfile(i_item):
                print("Testing {}".format(i_item))
                _ext = self.get_file_ext(i_item)
                if _ext in self.filters:
                    print("Copying {}".format(os.path.basename(i_item)))
                    shutil.copy2(i_item, os.path.join(self.args.target, os.path.basename(i_item)))

    def start(self):
        print("== Mass Copier ==")
        self.copy_dir(self.args.source)


if __name__ == "__main__":
    parser = ArgumentParser(description="Mass Copier")
    parser.add_argument("source", type=str, help="Source directory")
    parser.add_argument("--filter", type=str, help="File filter")
    parser.add_argument("target", type=str, help="Target directory")
    args = parser.parse_args()

    copier = MassCopier(args)
    copier.start()
