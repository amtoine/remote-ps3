from typing import Callable

from rich import print

from remote import computer, state, utils

OMMIT_NONE = True
MOUSE_SPEED = 10

Hook = Callable[[state.ControllerState, utils.Config, str], str]


def DEFAULT_CONTROLLER_HOOK(
    controller_state: state.ControllerState, *, config: utils.Config, **kwargs
) -> None:
    """Print the state of the controller."""
    print(controller_state.__repr__(ommit_none=OMMIT_NONE))


def remote_hook(
    controller_state: state.ControllerState,
    *,
    config: utils.Config,
    profile: str
) -> str:
    """Procees the state the controller to emulate keyboard presses."""
    new_profile = profile
    for key in controller_state.get_down_keys():
        result = computer.send(key, config=config, kwargs={"profile": profile})
        if result is not None:
            new_profile = result
        controller_state.keys[key] = 0

    for axis, value in controller_state.get_off_center_axes():
        computer.send(
            axis, config=config, kwargs={"value": value, "speed": MOUSE_SPEED}
        )

    return new_profile
