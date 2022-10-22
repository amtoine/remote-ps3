#!/usr/bin/env python

from src import device


def main():
    device.listen_to(device.get_device(), None, None, None)


if __name__ == "__main__":
    main()
