#!/usr/bin/env python

from typing import Dict

import evdev
from rich import print

from src import device


def remote_hook(key: evdev.events.KeyEvent, joysticks: Dict[str, int]) -> None:
    """Procees the state the controller to emulate keyboard presses."""
    print("remote control of the keyboard...")


def main():
    device.listen_to(device.get_device(), hook=remote_hook)


if __name__ == "__main__":
    main()
