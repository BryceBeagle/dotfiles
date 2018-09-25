import os
import shutil

import util
from pacman import pacman


def ensure_boot_mounted():
    if not os.path.ismount("/boot"):
        util.run(["mount", "-L", "BOOT", "/boot"])
    assert os.path.ismount("/boot"), \
        "Error: Could not copy systemd-boot configuration: " \
        "/boot is not mounted"


def create_loader_conf(conf_name, default):
    loader_conf = f"/boot/loader/loader.conf"
    if not os.path.exists(loader_conf) or default:
        # Create loader.conf
        shutil.copyfile("boot/loader.conf", loader_conf)
        util.file_sub("%DEFAULT_CONF%", conf_name, loader_conf)


def create_loader_entry(partition_label, install_dir, conf_name):
    entry_conf = f"/boot/loader/entries/{conf_name}.conf"
    shutil.copyfile("boot/arch.conf", entry_conf)
    util.file_sub("%INSTALL_DIR%", install_dir, entry_conf)
    util.file_sub("%PART_LABEL%", partition_label, entry_conf)


def mkinitcpio(install_dir):
    print("Running mkinitcpio for updated kernel modules")

    command = ["mkinitcpio", "-p", "linux"]
    if install_dir:
        command += ["-d", install_dir]

    util.run(command)


def setup(partition_label, conf_name="arch", default=True):

    ensure_boot_mounted()

    # Remove ucode file if installing ucode package
    # Not doing this will cause pacman to error out
    ucode_path = "/boot/intel-ucode.img"
    if os.path.exists(ucode_path):
        os.remove(ucode_path)

    pacman.install_packages(["intel-ucode"])

    # install_dir = f"installs/{conf_name}/"
    install_dir = ""  # install to root of boot for now
    print(f"Creating directory /boot/{install_dir} for bootloader")
    os.makedirs(f"/boot/{install_dir}", exist_ok=True)

    print(f"Installing systemd-boot to /boot/{install_dir}")
    util.run([f"bootctl", f"--path=/boot/{install_dir}", "install"])

    print("Creating loader.conf")
    create_loader_conf(conf_name, default)

    print("Creating boot loader entry")
    create_loader_entry(partition_label, install_dir, conf_name)

    print(f"Running mkinitcpio")
    mkinitcpio(install_dir)
