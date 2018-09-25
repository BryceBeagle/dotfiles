from . import bash
from . import fonts
from . import nvim
from . import ssh
from . import x
from . import xdg
from . import zsh


def setup():
    x.setup()
    nvim.setup()
    xdg.setup()
    bash.setup()
    zsh.setup()
    ssh.setup()
    fonts.setup()
