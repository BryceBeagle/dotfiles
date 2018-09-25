import util


def setup():

    print("Symlink all qtile files")
    util.symlink("config/qtile/config.py", "~/.config/qtile/")
    util.symlink("config/qtile/bindings.py", "~/.config/qtile/")
    util.symlink("config/qtile/groups.py", "~/.config/qtile/")
    util.symlink("config/qtile/helpers.py", "~/.config/qtile/")
    util.symlink("config/qtile/layouts.py", "~/.config/qtile/")
    util.symlink("config/qtile/settings.py", "~/.config/qtile/")
    util.symlink("config/qtile/widgets.py", "~/.config/qtile/")
