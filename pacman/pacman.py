import os
import subprocess
from typing import List, Union

import util
from boot import boot
from pacman.packages import packages, Package, Repo


def setup():
    print("Symlinking paccache hooks to /etc/pacman.d/")
    util.symlink("pacman/paccache-remove.hook", "/etc/pacman.d/hooks/",
                 root_own=True)
    util.symlink("pacman/paccache-upgrade.hook", "/etc/pacman.d/hooks/",
                 root_own=True)


def setup_environment(official=True, aur=False):
    official_packages = [pkg for pkg in packages if pkg.repo is Repo.official]
    aur_packages = [pkg for pkg in packages if pkg.repo is Repo.aur]
    multilib_packages = [pkg for pkg in packages if pkg.repo is Repo.multilib]

    print("Ensuring boot mounted")
    boot.ensure_boot_mounted()

    print("Updating packages")
    update()

    if official:
        print("Installing official repo packages")
        install_packages(official_packages)

    if aur:
        print("Installing yay")
        install_yay()

        if aur_packages:
            print("Installing AUR packages")
            install_aur_packages(aur_packages)

    if multilib_packages:
        print("Enabling multilib")
        enable_multilib()

        print("Installing multilib packages")
        install_packages(multilib_packages)


def pacstrap():
    print("Running pacstrap")
    util.run(["pacstrap", "/mnt/", "base", "base-devel"])


def update():
    """Update packages"""
    util.run(util.add_root(["pacman", "-Syu"]))


def install_packages(pkgs: List[Union[str, Package]]):
    if isinstance(pkgs, str):
        pkgs = [pkgs]
    if isinstance(pkgs, list):
        pkgs = [pkg.name if isinstance(pkg, Package) else pkg for pkg in pkgs]

    util.run(util.add_root(["pacman", "-S", "--noconfirm", "--needed"]) + pkgs)


def install_yay():
    # Dependencies for the command
    install_packages(["git", "binutils"])

    working_dir = os.getcwd()

    # Change cwd to /tmp to clone the repositories
    os.chdir("/tmp")

    # Clone repository
    git_url = f"https://aur.archlinux.org/yay.git"
    util.run(["git", "clone", git_url])

    # cd into cloned repo
    os.chdir("yay")

    # Install package
    util.run(["makepkg", "-si", "--noconfirm"])

    # Restore original working directory
    os.chdir(working_dir)


def install_aur_packages(pkgs: List[Union[str, Package]], username):
    # Install yay if we don't already have it
    try:
        util.run(["pacman", "-Qi", "yay"])
    except subprocess.CalledProcessError:
        install_yay()

    print("Installing gpg keys if necessary")
    for pkg in pkgs:
        if isinstance(pkg, Package):
            if pkg.gpg_keys:
                print(f"Receiving key={pkg.gpg_keys}")
                util.recv_gpg_keys(username, pkg.gpg_keys)

    if isinstance(pkgs, str):
        pkgs = [pkgs]
    if isinstance(pkgs, list):
        pkgs = [pkg.name if isinstance(pkg, Package) else pkg for pkg in pkgs]

    util.run(["yay",
              "--pgpfetch", "--sudoloop", "--noconfirm",
              "--answerclean", "N",
              "--answerdiff", "N",
              "--answerupgrade", "N",
              "-S"] + pkgs)


def enable_multilib():
    # Uncomment multilib section in /etc/pacman.conf
    conf_file = "/etc/pacman.conf"
    replace_str = "s/#[multilib]/[multilib]"
    util.run(util.add_root(["sed", "-i", replace_str, conf_file]))
