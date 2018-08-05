import util


def setup():

    # Symlink files
    util.symlink("display.egpu", "/etc/X11/xorg.conf.d/", root_own=True)
    util.symlink("display.internal", "/etc/X11/xorg.conf.d/", root_own=True)
    util.symlink("egpu-detect.service", "/etc/systemd/system/", root_own=True)
    util.symlink("egpu-detect.sh", "/etc/systemd/scripts", root_own=True)

    # Remove NVIDIA default xorg conf
    util.remove("/etc/X11/xorg.conf.d/20-nvidia.conf")

