import util


def setup():
    print(f"Symlinking .bashrc to ~/")
    util.symlink("config/bash/.bashrc", "~/")
