#!/bin/sh -

gpu=$(/usr/bin/lspci)

if grep -q 1070 <<< "$gpu" ; then
    echo "eGPU Found"
    ln -sf /etc/X11/xorg.conf.d/display.egpu /etc/X11/xorg.conf.d/20-display.conf
else
    echo "eGPU Not Found"
    ln -sf /etc/X11/xorg.conf.d/display.internal /etc/X11/xorg.conf.d/20-display.conf
fi

