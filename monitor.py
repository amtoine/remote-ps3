#!/usr/bin/env python

from src import device


def main():
    joysticks = {axis: None for axis in device.AXES}
    device.listen_to(device.get_device(), joysticks)


if __name__ == "__main__":
    main()
