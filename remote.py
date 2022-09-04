#!/usr/bin/env python

from typing import Dict

import evdev
from rich import print

from src import device, hooks, state


def main():
    device.listen_to(device.get_device(), hook=hooks.remote_hook)


if __name__ == "__main__":
    main()
