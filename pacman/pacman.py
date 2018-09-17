import os
import subprocess
from typing import List, Union

import util
from pacman.packages import packages, Repo


def setup(username):
    print("Symlinking paccache hooks to /etc/pacman.d/")
    util.symlink("pacman/paccache-remove.hook", "/etc/pacman.d/hooks/",
                 root_own=True)
    util.symlink("pacman/paccache-upgrade.hook", "/etc/pacman.d/hooks/",
                 root_own=True)

    official_packages = [pkg for pkg, repo in packages if repo is Repo.official]
    aur_packages = [pkg for pkg, repo in packages if repo is Repo.aur]
    multilib_packages = [pkg for pkg, repo in packages if repo is Repo.multilib]

    print("Updating packages")
    update()

    print("Installing official repo packages")
    # install_packages(official_packages)

    print("Installing yay")
    install_yay(username)
    if aur_packages:
        print("Installing AUR packages")
        install_aur_packages(aur_packages, username)

    if multilib_packages:
        print("Enabling multilib")
        enable_multilib()

        print("Installing multilib packages")
        install_packages(multilib_packages)


def pacstrap():
    print("Running pacstrap")
    util.run(["pacstrap", "-i", "/mnt/", "base", "base-devel"])


def update():
    """Update packages"""
    util.run(["pacman", "-Syu"])


def install_packages(pkgs: Union[str, List[str]]):

    if isinstance(pkgs, str):
        pkgs = [packages]

    util.run(["pacman", "-Syu"])
    util.run(["pacman", "-S"] + pkgs)


def install_yay(username):

    # Dependencies for the command
    install_packages(["git", "go", "binutils"])

    working_dir = os.getcwd()

    # Change cwd to /tmp to clone the repositories
    os.chdir("/tmp")

    # Clone repository
    git_url = f"https://aur.archlinux.org/yay.git"
    util.run(["sudo", "-u", username, "git", "clone", git_url])

    # cd into cloned repo
    os.chdir("yay")

    # Install package
    util.run(["sudo", "-u", username, "makepkg", "-si"])

    # Restore original working directory
    os.chdir(working_dir)


def install_aur_packages(pkgs: Union[str, List[str]], username):
    # Install yay if we don't already have it
    try:
        util.run(["pacman", "-Qi", "yay"])
    except subprocess.CalledProcessError:
        install_yay(username)

    if isinstance(pkgs, str):
        pkgs = [packages]

    util.run(["su", "-u", username, "yay"])
    util.run(["yay", "-S"] + pkgs)


def enable_multilib():
    # Uncomment multilib section in /etc/pacman.conf
    conf_file = "/etc/pacman.conf"
    replace_str = "s/#[multilib]/[multilib]"
    util.run(["sed", "-i", replace_str, conf_file])
