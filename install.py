import os
import shutil
import subprocess

import boot
import config
import egpu
import fstab
import kernel_modules
import pacman
import util


def init_drives(target_drive="arch", boot_drive="boot"):
    util.mount(target_drive, "/mnt/")
    os.mkdir("/mnt/boot/")
    util.mount(boot_drive, "/mnt/boot/")


def select_mirrors():
    mirrors = util.curl(
        "https://www.archlinux.org/mirrorlist/"
        "?country=FR&country=GB&protocol=https&use_mirror_status=on"
    )

    # Uncomment all servers
    mirrors = util.string_sub(r"^#Server", "Server", mirrors)

    # Delete lines with comments
    mirrors = util.string_sub(r"^#.", "", mirrors)

    util.pipe(["rankmirrors", "-n", "5", "-"], mirrors)


def setup_localization():
    # Set time zone
    util.symlink("/usr/share/zoneinfo/America/Los_Angeles", "/etc/localtime")

    # Run hwclock to generate /etc/adjtime
    subprocess.check_output(["hwclock", "--systohc"])

    # locale-gen
    util.file_sub("#en_US.UTF-8 UTF-8", "en_US.UTF-8 UTF-8", "/etc/locale.gen")
    subprocess.check_output(["locale-gen"])

    # Set the LANG variable in locale.conf
    with open("/etc/locale.conf", "w") as fi:
        fi.write("LANG=en_US.UTF-8\n")


def setup_hostname(hostname):
    # Create hostname file
    with open("/etc/hostname", "w") as fi:
        fi.write(f"{hostname}\n")

    # Add matching entries to hosts
    with open("/etc/hosts"):
        fi.write(f"127.0.0.1	localhost\n")
        fi.write(f"::1		    localhost\n")
        fi.write(f"127.0.1.1	{hostname}.localdomain	{hostname}\n")


def move_dotfiles(username):
    git_dir = f"~{username}/git/"

    # Create git dir if necessary
    if not os.path.exists(git_dir):
        os.mkdir(git_dir)

    # Move repo into dotfiles
    current_dotfiles_location = os.path.dirname(__file__)
    shutil.move(current_dotfiles_location, git_dir)

    new_dotfiles_location = os.path.join(git_dir, "dotfiles")

    # Change permissions so that user owns the files instead of root
    shutil.chown(new_dotfiles_location, username, username)
    os.chmod(new_dotfiles_location, 0o755)

    # cd into new dotfiles location
    os.chdir(new_dotfiles_location)


if __name__ == '__main__':
    # Set up installation environment
    init_drives(target_drive="arch-test")
    select_mirrors()
    pacman.pacstrap()

    # Chroot into drive
    util.begin_chroot("/mnt/")

    setup_localization()
    setup_hostname("griefcake")

    # Set up bootloader
    boot.setup(partition_label="arch", conf_name="arch")

    # Create user
    util.create_user("ignormies")
    util.set_password("root")
    util.set_password("ignormies")

    # Move dotfiles repo to user dir
    move_dotfiles("ignormies")

    # Set up environment
    pacman.setup()
    config.setup()
    fstab.setup()
    egpu.setup()
    kernel_modules.setup()
