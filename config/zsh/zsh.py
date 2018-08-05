import util


def setup(username):
    print(f"Symlinking .zshrc to /home/{username}/")
    util.symlink(".zshrc", f"/home/{username}/")
