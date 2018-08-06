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


def init_drives(target_drive="arch", boot_drive="BOOT"):
    print(f"Mounting target drive '{target_drive}' at /mnt/")
    if not os.path.ismount("/mnt"):
        util.mount(target_drive, "/mnt/")

    print("Creating /mnt/boot/")
    if not os.path.exists("/mnt/boot/"):
        os.mkdir("/mnt/boot/")

    print(f"Mounting boot_drive '{boot_drive}' at /mnt/boot/")
    if not os.path.ismount("/mnt/boot"):
        util.mount(boot_drive, "/mnt/boot/")


def select_mirrors():
    try:
        subprocess.check_output(["pacman", "-Qi", "reflector"])
    except subprocess.CalledProcessError:
        subprocess.check_output(["pacman", "-S", "reflector"])

    print("Ranking top 5 mirrors")
    subprocess.check_output(["reflector",
                             "--country", "United States",
                             "--protocol", "https",
                             "--sort", "rate",
                             "--save", "/etc/pacman.d/mirrorlist"])


def setup_localization():
    print("Setting time zone to America/Los_Angeles")
    util.symlink("/usr/share/zoneinfo/America/Los_Angeles", "/etc/localtime")

    print("Running hwclock to generate /etc/adjtime")
    subprocess.check_output(["hwclock", "--systohc"])

    print("Running locale-gen for en_US.UTF-8 UTF-8")
    util.file_sub("#en_US.UTF-8 UTF-8", "en_US.UTF-8 UTF-8", "/etc/locale.gen")
    subprocess.check_output(["locale-gen"])

    print("Setting the LANG variable in /etc/locale.conf")
    with open("/etc/locale.conf", "w") as fi:
        fi.write("LANG=en_US.UTF-8\n")


def setup_hostname(hostname):
    print(f"Creating /etc/hostname file for '{hostname}'")
    with open("/etc/hostname", "w") as fi:
        fi.write(f"{hostname}\n")

    print("Addding matching entry to /etc/hosts")
    with open("/etc/hosts"):
        fi.write(f"127.0.0.1	localhost\n")
        fi.write(f"::1		    localhost\n")
        fi.write(f"127.0.1.1	{hostname}.localdomain	{hostname}\n")


def move_dotfiles(username):
    git_dir = f"~{username}/git/"

    # Create git dir if necessary
    if not os.path.exists(git_dir):
        print(f"Creating git dir at '{git_dir}'")
        os.mkdir(git_dir)
    else:
        print("Git dir already exists. Continuing")

    current_dotfiles_location = os.path.dirname(__file__)
    print(f"Moving dotfiles clone from {current_dotfiles_location} "
          f"to '{git_dir}'")
    shutil.move(current_dotfiles_location, git_dir)

    new_dotfiles_location = os.path.join(git_dir, "dotfiles")

    print(f"Changing owner of {new_dotfiles_location} to user '{username}'")
    util.recursive_chown(new_dotfiles_location, username)

    print(f"Recursively changing permissions of {new_dotfiles_location} "
          "to 0o755")
    util.recursive_chmod(new_dotfiles_location, 0o755)

    print(f"cd-ing to {new_dotfiles_location}")
    os.chdir(new_dotfiles_location)


if __name__ == '__main__':
    hostname = "griefcake"
    username = "ignormies"

    init_drives(target_drive="arch-test")
    select_mirrors()
    pacman.pacstrap()

    # Chroot into drive
    util.begin_chroot("/mnt/")

    setup_localization()
    setup_hostname(hostname)

    # Set up bootloader
    boot.setup(partition_label="arch", conf_name="arch")

    # Create user
    util.create_user(username)
    util.set_password("root")
    util.set_password(username)

    # Move dotfiles repo to user dir
    move_dotfiles(username)

    # Set up environment
    pacman.setup()
    config.setup(username)
    fstab.setup()
    egpu.setup()
    kernel_modules.setup()
