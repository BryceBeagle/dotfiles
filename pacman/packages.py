from enum import Enum

# noinspection PyArgumentList
Repo = Enum("Repo", ["official", "multilib", "aur"])

packages = [

    # Desktop Environment
    ("xorg-server", Repo.official),
    ("budgie-desktop", Repo.official),
    ("arc-gtk-theme", Repo.official),
    ("paper-icon-theme-git", Repo.aur),

    # Editors
    ("nvim", Repo.official),
    ("pycharm-professional", Repo.aur),
    ("clion", Repo.official),
    ("bcompare", Repo.aur),

    # Browser
    ("chromium", Repo.official),

    # Steam
    # ("steam", Repo.multilib),
    # ("steam-native-runtime", Repo.multilib),
    # ("lib32-gtk-engines", Repo.aur),
    # ("lib32-gtk-engine-murrine", Repo.aur),
    # ("lib32-gnome-themes-standard", Repo.aur),

    # Dell XPS 9550
    ("b43-firmware", Repo.aur),
    ("bluez-utils-compat", Repo.aur),
    ("bcm20703a1-firmware", Repo.aur),  # Bluetooth driver
    ("nvidia", Repo.official),          # Graphics card
    # ("acpi", Repo.official),            # Prevents some startup error messages

    # Networking
    ("wpa_supplicant", Repo.official),
    ("private-internet-access-vpn", Repo.aur),

    # Communication
    ("slack-desktop", Repo.aur),

    # ZSH
    ("zsh", Repo.official),
    ("antigen-git", Repo.aur),

    # Fonts
    ("noto-fonts", Repo.official),
    ("noto-fonts-emoji", Repo.official),
    ("noto-fonts-sc", Repo.aur),  # Chinese symbols

    # Other
    ("pacman-contrib", Repo.official),  # Brings in paccache
    ("eagle", Repo.aur),
    ("arandr", Repo.official),
    ("vlc", Repo.official),
    ("sl", Repo.official),
    ("gparted", Repo.official),
    ("deluge", Repo.official),

]
