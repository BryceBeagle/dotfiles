import os
import subprocess
from typing import List, Union

import util
from pacman.packages import packages, Repo


def setup():
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
    install(official_packages)

    print("Installing yay")
    install_yay()
    if aur_packages:
        print("Installing AUR packages")
        install_aur(aur_packages)

    if multilib_packages:
        print("Enabling multilib")
        enable_multilib()

        print("Installing multilib packages")
        install(multilib_packages)


def pacstrap():
    print("Running pacstrap")
    util.run(["pacstrap", "-i", "/mnt/"])


def update():
    """Update packages"""
    util.run(["pacman", "-Syu"])


def install(pkgs: Union[str, List[str]]):
    if isinstance(pkgs, List):
        pkgs = " ".join(pkgs)

        util.run(["pacman", "-S"].extend(pkgs))


def install_yay():
    # Should be installed by nature of having this file, but just in case
    try:
        util.run(["pacman", "-Qi", "git"])
    except subprocess.CalledProcessError:
        install("git")

    working_dir = os.getcwd()

    # Change cwd to /tmp to clone the repositories
    os.chdir("/tmp")

    # Clone repository
    git_url = f"https://aur.archlinux.org/yay.git"
    util.run(["git", "clone", git_url])

    # cd into cloned repo
    os.chdir("yay")

    # Install package
    util.run(["makepkg", "-si"])

    # Restore original working directory
    os.chdir(working_dir)


def install_aur(pkgs: Union[str, List[str]]):
    # Install yay if we don't already have it
    try:
        util.run(["pacman", "-Qi", "yay"])
    except subprocess.CalledProcessError:
        install_yay()

    if isinstance(pkgs, List):
        pkgs = " ".join(pkgs)

        util.run(["yay", "-S"].extend(pkgs))


def enable_multilib():
    # Uncomment multilib section in /etc/pacman.conf
    conf_file = "/etc/pacman.conf"
    replace_str = "s/#[multilib]/[multilib]"
    util.run(["sed", "-i", replace_str, conf_file])
