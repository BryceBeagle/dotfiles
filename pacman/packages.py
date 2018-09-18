from dataclasses import dataclass, field
from enum import Enum
from typing import List

# noinspection PyArgumentList
Repo = Enum("Repo", ["official", "multilib", "aur"])


@dataclass
class Package:
    name: str
    repo: Repo = Repo.official
    gpg_keys: List[str] = field(default_factory=lambda: [])


packages = [Package(
    *package
    if isinstance(package, tuple)
    else (package,))
    for package in [

        # Prerequisites
        "wpa_supplicant",
        "dialog",
        "openssh",
        "git",

        # Desktop Environment
        "xorg-server",
        "budgie-desktop",
        "arc-gtk-theme",
        # ("paper-icon-theme-git", Repo.aur),

        # Editors
        "neovim",
        # ("pycharm-professional", Repo.aur),
        # ("clion", Repo.aur),
        # ("bcompare", Repo.aur),

        # Browser
        "chromium",

        # Steam
        # ("steam", Repo.multilib),
        # ("steam-native-runtime", Repo.multilib),
        # ("lib32-gtk-engines", Repo.aur),
        # ("lib32-gtk-engine-murrine", Repo.aur),
        # ("lib32-gnome-themes-standard", Repo.aur),

        # Dell XPS 9550
        ("b43-firmware", Repo.aur),
        ("bluez-utils-compat", Repo.aur, ["06CA9F5D1DCF2659"]),
        ("bcm20703a1-firmware", Repo.aur),  # Bluetooth driver
        "nvidia",  # Graphics card
        # "acpi",  # Prevents some startup error messages

        # Networking
        "wpa_supplicant",
        # ("private-internet-access-vpn", Repo.aur),

        # Communication
        ("slack-desktop", Repo.aur),

        # ZSH
        "zsh",
        ("antigen-git", Repo.aur),

        # Fonts
        "noto-fonts",
        "noto-fonts-emoji",
        # ("noto-fonts-sc", Repo.aur),  # Chinese symbols
        "ttf-hack",  # Terminal font

        # Other
        "pacman-contrib",  # Brings in paccache
        # ("eagle", Repo.aur),
        "arandr",
        "vlc",
        "sl",
        "gparted",
        "deluge",
        "intel-ucode",
        "sudo",

    ]
]
