import os
import subprocess
from typing import List, Union


def update():
    """Update packages"""
    subprocess.call(["pacman", "-Syu"])


def install(packages: Union[str, List[str]]):
    if isinstance(packages, List):
        packages = " ".join(packages)

    subprocess.call(["pacman", "-S", packages])


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
    subprocess.call(["git", "clone", git_url])

    # cd into cloned repo
    os.chdir("yay")

    # Install package
    subprocess.call(["makepkg", "-si"])

    # Restore original working directory
    os.chdir(working_dir)


def install_aur(packages: Union[str, List[str]]):

    # Install yay if we don't already have it
    try:
        subprocess.check_output(["pacman", "-Qi", "yay"])
    except subprocess.CalledProcessError:
        install_yay()

    if isinstance(packages, List):
        packages = " ".join(packages)

    subprocess.call(["yay", "-S", packages])


def enable_multilib():
    # Uncomment multilib section in /etc/pacman.conf
    conf_file = "/etc/pacman.conf"
    replace_str = "s/#[multilib]/[multilib]"
    subprocess.call(["sed", "-i", replace_str, conf_file])
