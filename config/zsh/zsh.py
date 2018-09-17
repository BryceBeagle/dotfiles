import util


def setup(username):
    print(f"Symlinking .zshrc to /home/{username}/")
    util.symlink("config/zsh/.zshrc", f"/home/{username}/")
