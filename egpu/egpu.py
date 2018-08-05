import os


def symlink(real, link):
    real = os.path.abspath(real)
    os.symlink(real, link)


def setup():

    # Symlink files
    symlink("display.egpu", "/etc/X11/xorg.conf.d/")
    symlink("display.internal", "/etc/X11/xorg.conf.d/")
    symlink("egpu-detect.service", "/etc/systemd/system/")
    symlink("egpu-detect.sh", "/etc/systemd/scripts")

    # Remove NVIDIA default xorg conf
    try:
        os.remove("/etc/X11/xorg.conf.d/20-nvidia.conf")
    except IOError:
        pass

