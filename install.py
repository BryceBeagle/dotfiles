#!/usr/bin/env python

import locale
import os
import shutil
import subprocess
import sys

import boot
import config
import egpu
import fstab
import kernel_modules
import pacman
import util


def select_target():
    util.lslbk()
    target = input("Input the name of the partition to install to: /dev/")
    return "/dev/" + target.strip()


def format_target(target):
    if input(f"Target '{target}' will be wiped. "
             "Are you sure you want to continue? [y/N] ").lower() != 'y':
        sys.exit("Canceling operation")

    label = input("Label for new file system: ").strip()

    print(f"Making ext4 filesystem on target '{target}' with label '{label}'")
    util.run(["mkfs.ext4", target, "-L", label])

    return label


def mount_target(target):
    print(f"Mounting target '{target}' at /mnt/")
    if not os.path.ismount("/mnt"):
        util.mount(target, "/mnt/")


def select_mirrors():
    # try:
    #     util.run(["pacman", "-Qi", "reflector"])
    # except subprocess.CalledProcessError:
    #     util.run(["pacman", "-S", "--noconfirm", "reflector"])
    #
    # print("Ranking top 5 mirrors")
    # util.run(["reflector",
    #           "--country", "United States",
    #           "--protocol", "https",
    #           "--sort", "rate",
    #           "--save", "/etc/pacman.d/mirrorlist"])

    util.run(["curl -s 'https://www.archlinux.org/mirrorlist/?country=FR&country=GB&protocol=https&use_mirror_status=on' | sed -e 's/^#Server/Server/' -e '/^#/d' | rankmirrors -n 5 - > /etc/pacman.d/mirrorlist"])


def setup_localization():
    print("Setting time zone to America/Los_Angeles")
    util.symlink("/usr/share/zoneinfo/America/Los_Angeles", "/etc/localtime")

    print("Running hwclock to generate /etc/adjtime")
    util.run(["hwclock", "--systohc"])

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    print("Running locale-gen for en_US.UTF-8 UTF-8")
    util.file_sub("#en_US.UTF-8 UTF-8", "en_US.UTF-8 UTF-8", "/etc/locale.gen")
    util.run(["locale-gen"])

    print("Setting the locale")
    util.run(["localectl", "set-locale", "LANG=en_US.UTF-8"])


def setup_hostname(hostname):
    print(f"Creating /etc/hostname file for '{hostname}'")
    with open("/etc/hostname", "w", encoding="utf-8") as fi:
        fi.write(f"{hostname}\n")

    print("Adding matching entry to /etc/hosts")
    with open("/etc/hosts", "w", encoding="utf-8") as fi:
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

    target_drive = select_target()
    label = format_target(target_drive)
    mount_target(target_drive)
    select_mirrors()
    pacman.pacstrap()

    # Chroot into drive
    util.begin_chroot("/mnt/")

    setup_localization()
    setup_hostname(hostname)

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

    # Set up bootloader
    boot.setup(partition_label=label, conf_name="arch")
