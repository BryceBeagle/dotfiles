import util


def setup(username):
    print(f"Symlinking ssh config to /home/{username}/.ssh/")
    util.symlink("config/ssh/config", f"/home/{username}/.ssh/")
