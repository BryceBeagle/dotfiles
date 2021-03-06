"""
qtile calls i3-style workspaces `groups`.

Groups are a little more powerful as we can specify additional config
to apply to each group if we want:

NOTE :: Match is imported from libqtile.config
>>> Group(
...    # Display name for the group
...    name="my-workspace",
...    # Capture spawned programs and move them to this group
...    matches=[Match(wm_class=["FireFox"])],
...    # Spawn these programs on start
...    spawn=["my-program", "my-other-program"],
...    # Layout to use (must be in the listed layouts)
...    layout="MonadTall",
...    # Should this group exist even when there are no windows?
...    persist=True,
...    # Create this group when qtile starts?
...    init=True
...)
"""
from libqtile.config import Group, ScratchPad, DropDown

# Named Groups copied from i3
# >>> See https://fontawesome.com/cheatsheet for more fontawesome icons
groups = [
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
    Group("8"),
    Group("9"),
    Group("10"),
    # Scratchpads on M-- and M-S--
    ScratchPad("scratchpad", [
        # NOTE :: Need to force spawning as a new process so that
        #         qtile can capture the new terminal by pid.
        DropDown("term", "mate-terminal --disable-factory",
                 on_focus_lost_hide=False, x=0.1, y=0.1,
                 width=0.8, height=0.8),
        DropDown("ipython", "python3.6 -m qtconsole",
                 on_focus_lost_hide=False, x=0.1, y=0.1,
                 width=0.8, height=0.8)
    ]),
]
