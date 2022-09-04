#!/usr/bin/env python

import json
from typing import Dict

import evdev
from rich import print

from src import device, hooks


def main():
    with open("remote.json", "r") as remote_config_file:
        config = json.load(remote_config_file)

    configured_remote_hook = lambda s: hooks.remote_hook(s, config=config)
    device.listen_to(device.get_device(), hook=configured_remote_hook)


if __name__ == "__main__":
    main()
