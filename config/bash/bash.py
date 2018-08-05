import util


def setup(username):
    print(f"Symlinking .bashrc to /home/{username}/")
    util.symlink(".bashrc", f"/home/{username}/")
