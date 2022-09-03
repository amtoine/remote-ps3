#!/usr/bin/env python
from typing import Dict, List, Any

import evdev

from rich import print
from rich.prompt import IntPrompt
from rich.prompt import Confirm

AXES = [
    "ABS_RZ",
    "ABS_Z",
    "ABS_RX",
    "ABS_X",
    "ABS_RY",
    "ABS_Y"
]


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


def rich_get_array_index_prompt(array: List[Any], *, binary_prompt: str) -> int:
    """Get an index in an array."""
    if len(array) == 0:
        index = -2
    elif len(array) == 1:
        if Confirm.ask(binary_prompt, default=True):
            index = 0
        else:
            index = -1
    else:
        index = rich_range_prompt(1, len(array)) - 1

    return index


def get_device() -> evdev.device.InputDevice:
    """Get a device by listing all of them and prompting the user."""
    print("Fetching all the devices...")
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

    # ask the user.
    for i, device in enumerate(devices):
        print(f"{i+1}: {device.path} {device.name} {device.phys}")

    index = rich_get_array_index_prompt(devices, binary_prompt="Connect to the [i]device[/i]?")
    if index == -1:
        print("[b]OK :loudly_crying_face:")
        exit(1)
    elif index == -2:
        print("There is no device connected...\nPlease connect a device.")
        exit(2)

    print(f"Connecting to {device}...")
    device = evdev.InputDevice(devices[index])
    print(f"Connected to {device}!")
    return device


def listen_to(device: evdev.device.InputDevice, joysticks: Dict[str, int]) -> None:
    """Listen to a device and print the key presses and the axes state."""
    print(f"Listening to {device}...")
    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            print(evdev.categorize(event))
        elif event.type == evdev.ecodes.EV_ABS:
            absevent = evdev.categorize(event)
            for axis in AXES:
                if evdev.ecodes.bytype[absevent.event.type][absevent.event.code] == axis:
                    joysticks[axis] = absevent.event.value
            print(joysticks)


def main():
    joysticks = {axis: None for axis in AXES}
    device = get_device()
    listen_to(device, joysticks)


if __name__ == "__main__":
    main()
