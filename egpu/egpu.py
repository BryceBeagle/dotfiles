import os
import util


def setup():

    # Symlink files
    util.symlink("display.egpu", "/etc/X11/xorg.conf.d/")
    util.symlink("display.internal", "/etc/X11/xorg.conf.d/")
    util.symlink("egpu-detect.service", "/etc/systemd/system/")
    util.symlink("egpu-detect.sh", "/etc/systemd/scripts")

    # Remove NVIDIA default xorg conf
    try:
        os.remove("/etc/X11/xorg.conf.d/20-nvidia.conf")
    except IOError:
        pass

