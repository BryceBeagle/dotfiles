import util


def setup():
    print("Symlinking conf files to /etc/X11/xorg.conf.d/")
    util.symlink("egpu/display.egpu", "/etc/X11/xorg.conf.d/", root_own=True)
    util.symlink("egpu/display.internal", "/etc/X11/xorg.conf.d/",
                 root_own=True)

    print("Symlinking conf switching service to /etc/systemd/system/")
    util.symlink("egpu/egpu-detect.service", "/etc/systemd/system/",
                 root_own=True)

    print("Symlinking helper script for service to /etc/systemd/scripts/")
    util.symlink("egpu/egpu-detect.sh", "/etc/systemd/scripts",
                 root_own=True)

    print("Removing NVIDIA default xorg conf from /etc/X11/xorg.conf.d/")
    util.remove("/etc/X11/xorg.conf.d/20-nvidia.conf")
