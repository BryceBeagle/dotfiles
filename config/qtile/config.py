"""
My config files for qtile
>> qtile docs can be found @ http://qtile.readthedocs.io/en/latest/

There are probably some more good hooks to make use of in here:
    http://qtile.readthedocs.io/en/latest/manual/ref/hooks.html
"""
import os

# qtile internals
from libqtile import bar, widget
from libqtile.config import Screen, hook

# Settings/helpers
from settings import COLS, FONT_PARAMS
from helpers import run_script

# Import the parts of my config defined in other files
from layouts import layouts, floating_layout    # NOQA
import bindings
from groups import groups                       # NOQA


@hook.subscribe.screen_change
def restart_on_randr(qtile, ev):
    """Restart and reload config when screens are changed"""
    qtile.cmd_restart()


def make_screen(systray=False):
    """Defined as a function so that I can duplicate this on other monitors"""
    blocks = [
        # Marker for the start of the groups to give a nice bg: ◢■■■■■■■◤
        widget.TextBox(
            font="Arial", foreground=COLS["dark_4"],
            text="◢"
        ),
        widget.GroupBox(
            other_current_screen_border=COLS["orange_0"],
            this_current_screen_border=COLS["blue_0"],
            other_screen_border=COLS["orange_0"],
            this_screen_border=COLS["blue_0"],
            highlight_color=COLS["blue_0"],
            urgent_border=COLS["red_1"],
            background=COLS["dark_4"],
            highlight_method="block",  # Highlight (border, block, text, or line)
            inactive=COLS["dark_2"],  # Inactive group font color
            active=COLS["light_2"],  # Active group font color
            disable_drag=True,
            borderwidth=2
        ),
        # Marker for the end of the groups to give a nice bg: ◢■■■■■■■◤
        widget.TextBox(
            font="Arial", foreground=COLS["dark_4"],
            text="◤"
        ),

        widget.Spacer(),

        # Allow for quick command execution
        widget.Prompt(
            cursor_color=COLS["light_3"],
            # ignore_dups_history=True,
            bell_style="visual",
            prompt="λ : "
        ),

        widget.BatteryIcon(),
        widget.Volume(emoji=True),

        # Current time
        widget.Clock(format="%H:%M"),

        # Visual indicator of the current layout for this workspace.
        widget.CurrentLayoutIcon(),
    ]

    if systray:
        # Add in the systray and additional separator
        blocks.insert(-1, widget.Systray())

    return Screen(top=bar.Bar(blocks, 25, background=COLS["dark_2"]))


# XXX : When I run qtile inside of mate, I don"t actually want a qtile systray
#       as mate handles that. (Plus, if it _is_ enabled then the mate and
#       qtile trays both crap out...)
screens = [make_screen(systray=True)]

# ----------------------------------------------------------------------------
# .: Assorted additional config :
focus_on_window_activation = "smart"
dgroups_key_binder = None
follow_mouse_focus = True
bring_front_click = False
auto_fullscreen = True
dgroups_app_rules = []
cursor_warp = True
# main = None
keys = bindings.keys
mouse = bindings.mouse

# XXX :: Horrible hack needed to make grumpy java apps work correctly.
#        (This is from the default config)
wmname = "LG3D"


# ----------------------------------------------------------------------------
def main(qtile):
    """Optional entry point for the config"""
    # Make sure that we have a screen / bar for each monitor that is attached
    while len(screens) < len(qtile.conn.pseudoscreens):
        screens.append(make_screen())
