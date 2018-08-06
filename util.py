import os
import re
import shutil
import subprocess
from typing import List


def run(command):
    subprocess.run(command, check=True)


def remove(path):
    try:
        os.remove(path)
    except IOError:
        pass


def symlink(real, link, root_own=False):
    # Add name of real file to link if link is merely a directory
    if os.path.isdir(link):
        link = os.path.join(link, os.path.basename(real))

    # Expand potentially relative path to be absolute
    real = os.path.abspath(real)

    # Create directory link will reside in if it does not exist
    link_dir = os.path.dirname(link)
    if not os.path.exists(link_dir):
        os.mkdir(link_dir)

    # Delete target if it exists
    remove(link)

    # Change the owner to root if desired
    if root_own:
        shutil.chown(real, "root", "root")

    # Create symlink
    os.symlink(real, link)


def begin_chroot(path):
    run(["arch-chroot", path])


def mount(name, location):
    run(["mount", name, location])


def curl(address, quiet=True):
    quiet_flag = "-s" if quiet else ""
    return subprocess.check_output(["curl", quiet_flag, address]).decode()


def string_sub(pattern, replacement, string):
    return re.sub(pattern, replacement, string, flags=re.MULTILINE)


def file_sub(pattern, replacement, filename):
    with open(filename, "r+") as fi:
        for line in fi:
            line = string_sub(pattern, replacement, line)
            fi.write(line)


def pipe(command: List[str], string: str):
    subprocess.run(command, input=string.encode(), check=True)


def create_user(username, sudoer=True):
    run(["useradd", "-m",
         "-s", "/usr/bin/zsh",
         "-G", "sudo",
         username])

    if sudoer:
        run(["groupadd", "sudo"])
        run(["gpasswd", "-a", username])


def set_password(username):
    run(["passwd", username])


def recursive_chown(path, username):
    for root, dirs, files in os.walk(path):

        for dir_file in dirs + files:
            shutil.chown(os.path.join(root, dir_file), username, username)


def recursive_chmod(path, mode, ignore_git=True):
    for root, dirs, files in os.walk(path):

        if ignore_git:
            dirs[:] = [dir_ for dir_ in dirs if ".git" not in dir_]

        for dir_file in dirs + files:
            os.chmod(os.path.join(root, dir_file), mode)


def lslbk():

    run(["lsblk", "-o", "name,label,size,mountpoint"])
