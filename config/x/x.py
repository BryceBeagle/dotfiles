import util


def setup():
    print(f"Symlinking .xinitrc to ~/")
    util.symlink("config/x/.xinitrc", "~/")
