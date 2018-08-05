from . import bash
from . import nvim
from . import ssh
from . import x
from . import xdg
from . import zsh
from . import fonts


def setup():
    x.setup()
    nvim.setup()
    xdg.setup()
    bash.setup()
    zsh.setup()
    ssh.setup()
    fonts.setup()
