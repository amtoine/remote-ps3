#!/usr/bin/env python
from typing import Dict, List, Any

import evdev

from rich import print

from src import prompt, device


def main():
    joysticks = {axis: None for axis in device.AXES}
    device.listen_to(device.get_device(), joysticks)


if __name__ == "__main__":
    main()
