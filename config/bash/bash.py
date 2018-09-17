import util


def setup(username):
    print(f"Symlinking .bashrc to /home/{username}/")
    util.symlink("config/bash/.bashrc", f"/home/{username}/")
