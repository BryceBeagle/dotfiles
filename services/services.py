import util

services = [
    "dhcpcd"
]


def setup():
    for service in services:
        util.run(["systemctl", "enable", service])
