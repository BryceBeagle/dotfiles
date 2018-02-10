When the external GPU is attached, `10-nvidia.conf` needs to be placed in `/etx/X11/xorg.conf.d/`. Otherwise it should not exist or be named to not end in .conf

File destinations:

10-nvidia.conf -> /etc/X11/xorg.conf.d/
egpu-detect.service -> 
