import shutil

import util


def setup():

    shutil.move("/etc/fstab", "/etc/fstab.bak")
    util.symlink("fstab", "/etc", root_own=True)
