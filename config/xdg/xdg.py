import util


def setup():
    print(f"Symlinking user-dirs.dirs to ~/.config/")
    util.symlink("config/xdg/user-dirs.dirs", "~/.config/")
