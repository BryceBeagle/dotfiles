import util


def setup(username):
    print(
        f"Symlinking 10-emoji.conf to "
        f"/home/{username}/.config/fontconfig/conf.d/")
    util.symlink(
        "config/fonts/10-emoji.conf",
        f"/home/{username}/.config/fontconfig/conf.d/")
