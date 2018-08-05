import os
import subprocess

import util


def setup():
    util.symlink("no-psmouse.conf", "/etc/modprobe.d/", root_own=True)

    if not os.path.ismount("/boot"):
        subprocess.check_output(["mount", "-a"])
    assert (os.path.ismount("/boot"),
            "Error: Could not rebuild initramfs after loading kernel modules: "
            "/boot is not mounted")

    subprocess.check_output(["mkinitcpio", "-p", "linux"])
