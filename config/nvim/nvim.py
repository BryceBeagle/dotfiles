import util


def setup(username):
    print(f"Symlinking init.vim to /home/{username}/.config/nvim/")
    util.symlink("init.vim", f"/home/{username}/.config/nvim/")
