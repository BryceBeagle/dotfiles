import util


def setup():
    print(f"Symlinking .zshrc to ~/")
    util.symlink("config/zsh/.zshrc", "~/")
