from enum import Enum

# noinspection PyArgumentList
Repo = Enum("Repo", ["official", "multilib", "aur"])

packages = [

    # Editors
    ("nvim", Repo.official),
    ("pycharm-professional", Repo.aur),
    ("clion", Repo.official),
    ("bcompare", Repo.aur),

    # Desktop Environment
    ("budgie-desktop", Repo.official),
    ("paper-icon-theme-git", Repo.aur),

    # Steam
    ("steam", Repo.multilib),
    ("steam-native-runtime", Repo.multilib),
    ("lib32-gtk-engines", Repo.aur),
    ("lib32-gtk-engine-murrine", Repo.aur),
    ("lib32-gnome-themes-standard", Repo.aur),

    # Dell XPS 9550
    ("b43-firmware", Repo.aur),
    ("bluez-utils-compat", Repo.aur),
    ("bcm20703a1-firmware", Repo.aur),  # Bluetooth driver
    ("nvidia", Repo.official),          # Graphics card

    # Networking
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

]
