eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)
export SSH_AUTH_SOCK

export XDG_CURRENT_DESKTOP=Budgie:GNOME
exec budgie-desktop
