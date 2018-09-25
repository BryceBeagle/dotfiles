import util


def setup():

    # Symlink all qtile files
    util.symlink("qtile/config.py", "~/.config/qtile/")
    util.symlink("qtile/bindings.py", "~/.config/qtile/")
    util.symlink("qtile/groups.py", "~/.config/qtile/")
    util.symlink("qtile/helpers.py", "~/.config/qtile/")
    util.symlink("qtile/layouts.py", "~/.config/qtile/")
    util.symlink("qtile/settings.py", "~/.config/qtile/")
    util.symlink("qtile/widgets.py", "~/.config/qtile/")
