import util


def setup(username):
    print(f"Symlinking .xinitrc to /home/{username}/")
    util.symlink("config/x/.xinitrc", f"/home/{username}/")
