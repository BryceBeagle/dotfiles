from . import bash
from . import fonts
from . import nvim
from . import ssh
from . import x
from . import xdg
from . import zsh


def setup(username):
    x.setup(username)
    nvim.setup(username)
    xdg.setup(username)
    bash.setup(username)
    zsh.setup(username)
    ssh.setup(username)
    fonts.setup(username)
