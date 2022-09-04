from typing import Any, Dict

import keyboard
import mouse
from rich import print

from src import computer, state

OMMIT_NONE = True
MOUSE_SPEED = 10


def DEFAULT_CONTROLLER_HOOK(controller_state: state.ControllerState) -> None:
    """Print the state of the controller."""
    print(controller_state.__repr__(ommit_none=OMMIT_NONE))


def remote_hook(
    controller_state: state.ControllerState, *, config: Dict[str, Any]
) -> None:
    """Procees the state the controller to emulate keyboard presses."""
    for key in controller_state.get_down_keys():
        computer.send(key, config=config, kwargs={})
        controller_state.keys[key] = 0

    for axis, value in controller_state.get_off_center_axes():
        computer.send(
            axis, config=config, kwargs={"value": value, "speed": MOUSE_SPEED}
        )
