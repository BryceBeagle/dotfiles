import getpass
import util


def setup():

    print(f"Symlinking .zshrc to ~/")
    util.symlink("config/zsh/.zshrc", "~/")

    print("Setting default terminal to zsh")
    util.run(["chsh", "-s", "/usr/bin/zsh", getpass.getuser()])
