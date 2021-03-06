import os
import re
import shutil
import subprocess
from typing import List


def run(command, repeat=False):
    # If repeat is True, keep trying. Useful if user makes a mistake
    while True:
        try:
            subprocess.run(command, check=True)
            break
        except subprocess.CalledProcessError:
            if not repeat:
                raise


def remove(path):
    try:
        os.remove(path)
    except IOError:
        pass


def symlink(real, link, *, link_is_dir=True, root_own=False):

    # Expand user paths
    real = os.path.expanduser(real)
    link = os.path.expanduser(link)

    # Add name of real file to link if link is merely a directory
    if link_is_dir:
        link = os.path.join(link, os.path.basename(real))

    # Expand potentially relative path to be absolute
    real = os.path.abspath(real)

    # Create directory link will reside in if it does not exist
    link_dir = os.path.dirname(link)
    if not os.path.exists(link_dir):
        os.makedirs(link_dir)

    # Delete target if it exists
    remove(link)

    # Change the owner to root if desired
    if root_own:
        shutil.chown(real, "root", "root")

    # Create symlink
    os.symlink(real, link)


def begin_chroot(path):
    """Note that this chroot cannot be escaped normally"""

    os.chdir(path)

    print("Mounting /proc")
    run(["mount", "-t", "proc", "/proc", "proc/"])

    print("Mounting /sys")
    run(["mount", "--rbind", "/sys", "sys/"])

    print("Mounting /dev")
    run(["mount", "--rbind", "/dev", "dev/"])

    print("Mounting /run")
    run(["mount", "--rbind", "/run", "run/"])

    print("Copying resolv.conf")
    shutil.copyfile("/etc/resolv.conf", "etc/resolv.conf")

    print(f"Chrooting to {path}")
    os.chroot(path)


def mount(name, location):
    run(["mount", name, location])


def curl(address, quiet=True):
    quiet_flag = "-s" if quiet else ""
    return subprocess.check_output(["curl", quiet_flag, address]).decode()


def file_sub(pattern, replacement, filename):
    with open(filename, encoding="utf-8") as fi:
        text = fi.read()

    with open(filename, "w", encoding="utf-8") as fi:
        fi.write(re.sub(pattern, replacement, text))


def pipe(command: List[str], string: str):
    subprocess.run(command, input=string.encode(), check=True)


def create_group(groupname):
    run(["groupadd", groupname])


def create_user(username, sudoer=True):

    run(["useradd", "-m", username])

    if sudoer:
        run(["gpasswd", "-a", username, "sudo"])


def set_password(username):
    print(f"Setting password for user {username}")
    run(["passwd", username], repeat=True)


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


def git_get_remote_url(file_in_clone):
    try:
        run(["pacman", "-Qi", "git"])
    except subprocess.CalledProcessError:
        run(["pacman", "-S", "--noconfirm", "--needed", "git"])

    prev_cwd = os.getcwd()

    os.chdir(os.path.dirname(os.path.abspath(file_in_clone)))

    remote_url = subprocess.check_output(
        ["git", "config", "--get", "remote.origin.url"]
    ).decode().strip()

    # username = input("GitHub username to clone dotfiles repo using SSH: ")
    #
    # remote_url = f"git@github.com:{username}{remote_url.split('/')[-1]}.git"
    #
    # os.chdir(prev_cwd)

    return remote_url


def git_clone_repo(remote_url, dst=None):
    try:
        run(["pacman", "-Qi", "git"])
    except subprocess.CalledProcessError:
        print("Installing git package")
        run(["pacman", "-S", "--noconfirm", "--needed", "git"])

    print(f"Cloning {remote_url} to {dst}")

    commands = ["git", "clone", remote_url]

    if dst:
        commands.append(dst)
    run(commands)


def recv_gpg_keys(username: str, keys: List[str]):
    run(["sudo", "-u", username, "gpg", "--recv-keys"] + keys)


def add_root(command: List[str]):
    if os.geteuid != 0:
        command.insert(0, "sudo")
    return command
