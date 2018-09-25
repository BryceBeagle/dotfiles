import util


def setup():
    print(f"Symlinking 10-emoji.conf to ~/.config/fontconfig/conf.d/")
    util.symlink("config/fonts/10-emoji.conf", "~/.config/fontconfig/conf.d/")
