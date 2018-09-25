#!/usr/bin/env python

import argparse
import pacman
import config


def main(no_official, aur, no_config):
    # Set up environment
    pacman.setup_environment(official=not no_official, aur=aur)
    if not no_config:
        config.setup()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("no-official", action="store_true")
    parser.add_argument("aur", action="store_true")
    parser.add_argument("no-config", action="store_true")

    args = parser.parse_args()
    main(args.no_official, args.aur, args.no_config)
