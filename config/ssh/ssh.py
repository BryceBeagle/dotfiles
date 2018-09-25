import util


def setup():
    print(f"Symlinking ssh config to ~/.ssh/")
    util.symlink("config/ssh/config", "~/.ssh/")
