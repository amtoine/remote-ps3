from typing import Dict, Callable

import evdev
from rich import print

from src import prompt

AXES = ["ABS_RZ", "ABS_Z", "ABS_RX", "ABS_X", "ABS_RY", "ABS_Y"]


def get_device() -> evdev.device.InputDevice:
    """Get a device by listing all of them and prompting the user."""
    print("Fetching all the devices...")
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

    # ask the user.
    for i, device in enumerate(devices):
        print(f"{i+1}: {device.path} {device.name} {device.phys}")

    index = prompt.rich_get_array_index_prompt(
        devices, binary_prompt="Connect to the [i]device[/i]?"
    )
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


def DEFAULT_CONTROLLER_HOOK(
    key: evdev.events.KeyEvent, joysticks: Dict[str, int]
) -> None:
    """Print the state of the controller."""
    if key is not None:
        print(key)
    print(joysticks)


def listen_to(
    device: evdev.device.InputDevice,
    joysticks: Dict[str, int],
    hook: Callable = DEFAULT_CONTROLLER_HOOK,
) -> None:
    """Listen to a device and print the key presses and the axes state."""
    print(f"Listening to {device}...")
    for event in device.read_loop():
        key = None
        if event.type == evdev.ecodes.EV_KEY:
            key = evdev.categorize(event)
        elif event.type == evdev.ecodes.EV_ABS:
            absevent = evdev.categorize(event)
            for axis in AXES:
                if (
                    evdev.ecodes.bytype[absevent.event.type][absevent.event.code]
                    == axis
                ):
                    joysticks[axis] = absevent.event.value
        if hook is not None:
            hook(key=key, joysticks=joysticks)
