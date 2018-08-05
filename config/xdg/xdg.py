import util


def setup(username):
    print(f"Symlinking user-dirs.dirs to /home/{username}/.config/")
    util.symlink("user-dirs.dirs", f"/home/{username}/.config/")
