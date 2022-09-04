#!/usr/bin/env python

from src import device


def main():
    device.listen_to(device.get_device())


if __name__ == "__main__":
    main()
