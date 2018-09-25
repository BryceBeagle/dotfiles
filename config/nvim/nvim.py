import util


def setup():
    print(f"Symlinking init.vim to ~/.config/nvim/")
    util.symlink("config/nvim/init.vim", "~/.config/nvim/")
