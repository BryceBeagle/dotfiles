import subprocess

from notes.packages import packages, Repo
import pacman


official_packages = [pkg for pkg, repo in packages if repo is Repo.official]
aur_packages      = [pkg for pkg, repo in packages if repo is Repo.aur]
multilib_packages = [pkg for pkg, repo in packages if repo is Repo.multilib]

# Update packages
pacman.update()

# Install packages
pacman.install(official_packages)

pacman.install_yay()
pacman.install_aur(aur_packages)

if multilib_packages:
    pacman.enable_multilib()
    pacman.install(multilib_packages)
