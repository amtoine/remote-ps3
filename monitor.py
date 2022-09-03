#!/usr/bin/env python

import evdev

from rich import print
from rich.prompt import IntPrompt
from rich.prompt import Confirm


def rich_range_prompt(a: int, b: int) -> int:
    """Ask for an index in a range of numbers with rich."""
    while True:
        index = IntPrompt.ask(
                f":rocket: Enter a number between [b]{a}[/b] and [b]{b}[/b]"
            )
        if index >= a and index <= b:
            break
        print(f":pile_of_poo: [prompt.invalid]Number must be between {a} and {b}")

    return index


def get_device() -> evdev.device.InputDevice:
    """Get a device by listing all of them and prompting the user."""
    print("Fetching all the devices...")
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

    # ask the user.
    for i, device in enumerate(devices):
        print(f"{i+1}: {device.path} {device.name} {device.phys}")

    if len(devices) == 0:
        print("There is no device connected...\nPlease connect a device.")
        exit(2)
    elif len(devices) == 1:
        if Confirm.ask("Connect to the [i]prompt[/i]?", default=True):
            index = 0
        else:
            print("[b]OK :loudly_crying_face:")
            exit(0)
    else:
        index = rich_range_prompt(1, len(devices)) - 1

    print(f"Connecting to {device}...")
    device = evdev.InputDevice(devices[index])
    print(f"Connected to {device}!")
    return device


def main():
    device = get_device()

    print(f"Listening to {device}...")
    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            print(evdev.categorize(event))


if __name__ == "__main__":
    main()
