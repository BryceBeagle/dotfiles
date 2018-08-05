import os
import re
import shutil
import subprocess
from typing import List


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
    subprocess.call(["arch-chroot", path])


def lsblk():
    subprocess.check_output(["lsblk"])


def mount(label, location):
    # https://stackoverflow.com/a/29156997
    subprocess.check_output(["mount", "-L", label, location])


def curl(address, quiet=True):
    quiet_flag = "-s" if quiet else ""
    return subprocess.check_output(["curl", quiet_flag, address])


def string_sub(pattern, replacement, string):
    return re.sub(pattern, replacement, string, flags=re.MULTILINE)


def file_sub(pattern, replacement, filename):
    with open(filename, "r+") as fi:
        for line in fi:
            line = string_sub(pattern, replacement, line)
            fi.write(line)


def pipe(command: List[str], string: str):
    process = subprocess.Popen(command, stdin=subprocess.PIPE)

    process.communicate(input=string)


def create_user(username, sudoer=True):
    subprocess.check_output(["useradd", "-m",
                             "-s", "/usr/bin/zsh",
                             "-G", "sudo",
                             username])

    if sudoer:
        subprocess.check_output(["groupadd", "sudo"])
        subprocess.check_output(["gpasswd", "-a", username])


def set_password(username):
    subprocess.check_output(["passwd", username])


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
