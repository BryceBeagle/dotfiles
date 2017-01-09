#!/bin/bash

# Source: http://unix.stackexchange.com/a/11891

# setting up new mode for my VGA
#xrandr --newmode "1920x1080" 148.5 1920 2008 2052 2200 1080 1089 1095 1125 +hsync +vsync
#xrandr --addmode VGA1 1920x1080

# default monitor is eDP-1
MONITOR=eDP1

# functions to switch from LVDS1 to VGA and vice versa
function ActivateMonitors {
    echo "Connecting Monitors"
    xrandr --output eDP1 --off
    xrandr --output DP2-1-2 --mode 3440x1440 --primary
    xrandr --output DP2-2 --mode 1920x1080 --right-of DP2-1-2
    xrandr --output DP2-1-1 --mode 1920x1080 --left-of DP2-1-2
    MONITOR=DP2-1-2
}
function DeactivateMonitors {
    echo "Disconnecting Monitors"
    xrandr --output DP2-1-2 --off
    xrandr --output DP2-2 --off
    xrandr --output DP2-1-1 --off
    --output eDP1 --auto
    MONITOR=eDP1
}

# functions to check if VGA is connected and in use
function MonitorsActive {
    [ $MONITOR = "DP2-1-2" ]
}
function MonitorsConnected {
    ! xrandr | grep "^DP2-1-2" | grep disconnected
}

# actual script
while true
do
    if ! MonitorsActive && MonitorsConnected
    then
        ActivateMonitors
    fi

    if MonitorsActive && ! MonitorsConnected
    then
        DeactivateMonitors
    fi

    sleep 1s
done
