from libqtile.command import lazy
from libqtile.config import EzKey

from helpers import script

# qtile actually has an emacs style `EzKey` helper that makes specifying
# key bindings a lot nicer than the default.
keys = [EzKey(k[0], *k[1:]) for k in [

    # Switch focus between windows on screen(s?)
    ("M-<Up>", lazy.layout.up()),
    ("M-<Down>", lazy.layout.down()),
    ("M-<Left>", lazy.layout.left()),
    ("M-<Right>", lazy.layout.right()),

    # Swap windows relative to active
    ("M-S-<Up>", lazy.layout.shuffle_up()),
    ("M-S-<Down>", lazy.layout.shuffle_down()),
    ("M-S-<Left>", lazy.layout.shuffle_left(), lazy.layout.swap_left()),
    ("M-S-<Right>", lazy.layout.shuffle_right(), lazy.layout.swap_right()),

    # Swap the position of the master/child panes
    ("M-<backslash>", lazy.layout.flip()),
    ("M-<minus>", lazy.layout.shrink()),
    ("M-<equal>", lazy.layout.grow()),

    # .: Program Launchers :. #
    ("M-<Return>", lazy.spawn("dbus-launch gnome-terminal")),
    ("M-r", lazy.spawncmd()),  # Quick execution of shell commands
    ("M-e", lazy.spawn("nautilus")),

    # Scratchpad toggles
    ("M-<slash>", lazy.group['scratchpad'].dropdown_toggle('term')),
    ("M-S-<slash>", lazy.group['scratchpad'].dropdown_toggle('ipython')),

    # Toggle fullscreen for active window
    ("M-f", lazy.window.toggle_fullscreen()),

    # Toggle between the available layouts.
    ("M-<grave>", lazy.next_layout()),
    ("A-<grave>", lazy.prev_layout()),
    # Switch focus between two screens
    ("M-<bracketleft>", lazy.to_screen(0)),
    ("M-<bracketright>", lazy.to_screen(1)),

    # Toggle between the two most recently used groups
    ("M-<Tab>", lazy.screen.toggle_group()),

    # Close the current window: NO WARNING!
    ("M-S-q", lazy.window.kill()),
    ("M-S-<BackSpace>", lazy.window.kill()),

    # Restart qtile in place and pull in config changes (check config before
    # doing this with `check-qtile-conf` script to avoid crashes)
    ("M-A-r", lazy.restart()),
    # Shut down qtile.
    ("M-A-<Escape>", lazy.shutdown()),
    ("M-A-l", lazy.spawn("lock-screen")),
    ("M-A-s", lazy.spawn("screenshot")),
    ("M-A-<Delete>", lazy.spawn(script("power-menu.sh"))),
]]
