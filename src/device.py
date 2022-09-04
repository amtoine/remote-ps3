from typing import Callable, Dict

import evdev
from rich import print

from src import prompt, state

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


def DEFAULT_CONTROLLER_HOOK(controller_state: state.ControllerState) -> None:
    """Print the state of the controller."""
    print(controller_state)


def listen_to(
    device: evdev.device.InputDevice,
    hook: Callable = DEFAULT_CONTROLLER_HOOK,
) -> None:
    """Listen to a device and print the key presses and the axes state."""
    controller_state = state.ControllerState(
        keys={}, axes={axis: None for axis in AXES}
    )

    print(f"Listening to {device}...")
    for event in device.read_loop():

        if event.type == evdev.ecodes.EV_KEY:
            controller_state.update_keys(evdev.categorize(event))

        elif event.type == evdev.ecodes.EV_ABS:
            controller_state.update_axis(evdev.categorize(event))

        if hook is not None:
            hook(controller_state=controller_state)
