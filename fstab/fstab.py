import shutil

import util


def setup():
    print("Making a copy of old fstab at /etc/fstab.bak")
    shutil.move("/etc/fstab", "/etc/fstab.bak")

    print("Symlinking fstab to /etc/fstab")
    util.symlink("fstab/fstab", "/etc", root_own=True)
