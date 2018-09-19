import os
import shutil

import util


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
        shutil.copyfile("loader.conf", loader_conf)
        util.file_sub("%DEFAULT_CONF%", conf_name, loader_conf)


def create_loader_entry(partition_label, install_dir, conf_name):
    entry_conf = f"/boot/loader/entries/{conf_name}.conf"
    shutil.copyfile("boot/arch.conf", entry_conf)
    util.file_sub("%INSTALL_DIR%", install_dir, entry_conf)
    util.file_sub("%PART_LABEL%", partition_label, entry_conf)


def mkinitcpio(install_dir):
    print("Running mkinitcpio for updated kernel modules")
    util.run(["mkinitcpio",
              "-p", "linux",
              "-d", install_dir])


def setup(partition_label, conf_name="arch", default=True):

    ensure_boot_mounted()

    install_dir = f"installs/{conf_name}/"
    print(f"Creating directory /boot/'{install_dir}' for bootloader")
    os.makedirs(f"/boot/{install_dir}", exist_ok=True)

    print(f"Installing systemd-boot to /boot/{install_dir}")
    util.run([f"bootctl", "install"])

    print("Creating loader.conf")
    create_loader_conf(conf_name, default)

    print("Creating boot loader entry")
    create_loader_entry(partition_label, install_dir, conf_name)

    print(f"Running mkinitcpio with generatedir=/'{install_dir}")
    mkinitcpio(install_dir)
