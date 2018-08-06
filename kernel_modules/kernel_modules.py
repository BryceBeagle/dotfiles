import os
import subprocess

import util


def setup():
    print("Symlinking no-psmouse.conf to /etc/modprobe.d/")
    util.symlink("no-psmouse.conf", "/etc/modprobe.d/", root_own=True)

    if not os.path.ismount("/boot"):
        util.run(["mount", "-a"])
    assert os.path.ismount("/boot"), \
        "Error: Could not rebuild initramfs after loading kernel modules: " \
        "/boot is not mounted"

    # mkinitcpio is run in boot.setup() afterwards
