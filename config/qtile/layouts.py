"""
My group/workspace layouts.

The built in layouts can be found here:
    http://docs.qtile.org/en/latest/manual/ref/layouts.html

Look at porting some Xmonad layouts to qtile:
    https://github.com/xmonad/xmonad-contrib/blob/master/XMonad/Layout/Circle.hs
    https://github.com/xmonad/xmonad-contrib/blob/master/XMonad/Layout/Cross.hs

>>  Try cribbing from what the XmonadTall layout does:
        http://qtile.readthedocs.io/en/latest/_modules/libqtile/layout/xmonad.html#MonadTall
"""
from settings import COLS
from libqtile import layout


# Annoyingly, there isn't a common subset of parameters for all layouts that
# can be passed as a dict splat. There _are_ some common ones for multiple
# layouts, so they are defined here and used where possible to give a
# consistent UI.
BORDER_NORMAL = COLS["dark_2"]
# BORDER_FOCUS = COLS["blue_2"]
BORDER_FOCUS = COLS["red_1"]
BORDER_WIDTH = 3
MARGIN = 12


layouts = [
    # XXX : My default layout. Single window fills the screen and it can
    #       keep a stack of secondary windows off to the side quite easily.
    layout.MonadTall(
        border_normal=BORDER_NORMAL,
        border_focus=BORDER_FOCUS,
        border_width=BORDER_WIDTH,
        margin=MARGIN,
        ratio=0.7,
    ),
    # XXX : Same idea as MonadTall but the smaller windows are along the
    #       top/bottom of the main window
    layout.MonadWide(
        border_normal=BORDER_NORMAL,
        border_focus=BORDER_FOCUS,
        border_width=BORDER_WIDTH,
        margin=MARGIN,
        ratio=0.7,
    )
]

# Specification for auto floating windows: this isn't a layout in the same
# way as the ones listed above.
floating_layout = layout.Floating(
    border_normal=BORDER_NORMAL,
    border_focus=BORDER_FOCUS,
    border_width=BORDER_WIDTH,
    float_rules=[
        {'wmclass': 'confirm'},
        {'wmclass': 'dialog'},
        {'wmclass': 'download'},
        {'wmclass': 'error'},
        {'wmclass': 'file_progress'},
        {'wmclass': 'notification'},
        {'wmclass': 'splash'},
        {'wmclass': 'toolbar'},
        {'wmclass': 'gcr-prompter'},
        {'wmclass': 'confirmreset'},
        {'wmclass': 'makebranch'},
        {'wmclass': 'maketag'},
        {'wmclass': 'peek'},
        {'wname': 'branchdialog'},
        {'wname': 'pinentry'},
        {'wmclass': 'ssh-askpass'},
    ]
)
