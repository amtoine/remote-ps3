import evdev
from rich import print

from remote import hooks, prompt, state, utils


def get_device() -> evdev.device.InputDevice:
    """Get a device by listing all of them and prompting the user."""
    print("Fetching all the devices...")
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

    # ask the user.
    for i, device in enumerate(devices):
        print(f"{i + 1}: {device.path} {device.name} {device.phys}")

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


def listen_to(
    device: evdev.device.InputDevice,
    config: utils.Config,
    profile: str,
    filename: str,
    hook: hooks.Hook = hooks.DEFAULT_CONTROLLER_HOOK,
) -> None:
    """Listen to a device and execute a hook at each event."""
    # initialize the state of the controller
    keys = {}
    for key in evdev.ecodes.keys.values():
        real_key = key[0] if isinstance(key, list) else key
        keys[real_key] = None
    axes = {axis: None for axis in evdev.ecodes.ABS.values()}
    controller_state = state.ControllerState(keys=keys, axes=axes)

    print(f"Listening to {device}...")
    for event in device.read_loop():

        # update the controller given the type of event
        if event.type == evdev.ecodes.EV_KEY:
            controller_state.update_keys(evdev.categorize(event))

        elif event.type == evdev.ecodes.EV_ABS:
            controller_state.update_axis(evdev.categorize(event))

        if hook is not None:
            new_profile = hook(
                controller_state, config=config, profile=profile
            )
            # update the controller profile if changed in the event
            if profile != new_profile:
                profile = new_profile
                config = utils.get_config_with_profile(
                    profile, filename=filename
                )
