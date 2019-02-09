import util


def setup():
    print(f"Symlinking kitty.conf to ~/.config/kitty/")
    util.symlink("config/kitty/kitty.conf", "~/.config/kitty/kitty.conf")
