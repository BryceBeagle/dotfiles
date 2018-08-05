import os
import shutil
import subprocess


def setup():

    if not os.path.ismount("/boot"):
        subprocess.check_output(["mount", "-a"])
    assert (os.path.ismount("/boot"),
            "Error: Could not copy systemd-boot configuration: "
            "/boot is not mounted")

    shutil.copy2("loader.conf", "/boot/loader/")
    shutil.copy2("arch.conf", "/boot/loader/entries/")
