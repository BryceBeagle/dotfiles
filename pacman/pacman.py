import os
import subprocess
from typing import List, Union

from pacman.packages import packages, Repo
import util


def setup():

    util.symlink("paccache-remove.hook", "/etc/pacman.d/hooks/")
    util.symlink("paccache-upgrade.hook", "/etc/pacman.d/hooks/")

    official_packages = [pkg for pkg, repo in packages if repo is Repo.official]
    aur_packages      = [pkg for pkg, repo in packages if repo is Repo.aur]
    multilib_packages = [pkg for pkg, repo in packages if repo is Repo.multilib]

    # Update packages
    update()

    # Install packages
    install(official_packages)

    install_yay()
    if aur_packages:
        install_aur(aur_packages)

    if multilib_packages:
        enable_multilib()
        install(multilib_packages)


def update():
    """Update packages"""
    subprocess.check_output(["pacman", "-Syu"])


def install(pkgs: Union[str, List[str]]):
    if isinstance(pkgs, List):
        pkgs = " ".join(pkgs)

    subprocess.check_output(["pacman", "-S", pkgs])


def install_yay():

    # Should be installed by nature of having this file, but just in case
    try:
        subprocess.check_output(["pacman", "-Qi", "git"])
    except subprocess.CalledProcessError:
        install("git")

    working_dir = os.getcwd()

    # Change cwd to /tmp to clone the repositories
    os.chdir("/tmp")

    # Clone repository
    git_url = f"https://aur.archlinux.org/yay.git"
    subprocess.check_output(["git", "clone", git_url])

    # cd into cloned repo
    os.chdir("yay")

    # Install package
    subprocess.check_output(["makepkg", "-si"])

    # Restore original working directory
    os.chdir(working_dir)


def install_aur(pkgs: Union[str, List[str]]):

    # Install yay if we don't already have it
    try:
        subprocess.check_output(["pacman", "-Qi", "yay"])
    except subprocess.CalledProcessError:
        install_yay()

    if isinstance(pkgs, List):
        pkgs = " ".join(pkgs)

    subprocess.check_output(["yay", "-S", pkgs])


def enable_multilib():
    # Uncomment multilib section in /etc/pacman.conf
    conf_file = "/etc/pacman.conf"
    replace_str = "s/#[multilib]/[multilib]"
    subprocess.check_output(["sed", "-i", replace_str, conf_file])
