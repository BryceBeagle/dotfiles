import os
import shutil
import subprocess

import util


def ensure_boot_mounted():
    if not os.path.ismount("/boot"):
        subprocess.check_output(["mount", "-a"])
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
    shutil.copyfile("arch.conf", entry_conf)
    util.file_sub("%INSTALL_DIR%", install_dir, entry_conf)
    util.file_sub("%PART_LABEL%", partition_label, entry_conf)


def setup(partition_label, conf_name="arch", default=True):
    install_dir = f"/installs/{conf_name}/"
    print(f"Creating directory '{install_dir}' for bootloader")
    os.makedirs(f"/boot/{install_dir}")

    print(f"Installing systemd-boot to /boot/{install_dir}")
    subprocess.check_output([f"bootctl --path=/boot/{install_dir} install"])

    print("Creating loader.conf")
    create_loader_conf(conf_name, default)

    print("Creating boot loader entry")
    create_loader_entry(partition_label, install_dir, conf_name)
