import util


def setup(username):
    print(f"Symlinking .xinitrc to /home/{username}")
    util.symlink(".xinitrc", f"/home/{username}/")
