import util

def setup():
    print("Symlinking usb wake disabling service to /etc/systemd/system/")
    util.symlink("fixes/disable-usb-wakeup.service", "/etc/systemd/system/",
                 root_own=True)

    print("Symlinking helper script for service to /etc/systemd/scripts/")
    util.symlink("fixes/disable-usb-wakeup.sh", "/etc/systemd/scripts",
                 root_own=True)

    util.run(["systemctl", "enable", "--now", "disable-usb-wakeup"])

