import keyboard
import mouse
from rich import print

from src import state

OMMIT_NONE = True
MOUSE_SPEED = 10


def DEFAULT_CONTROLLER_HOOK(controller_state: state.ControllerState) -> None:
    """Print the state of the controller."""
    print(controller_state.__repr__(ommit_none=OMMIT_NONE))


def remote_hook(controller_state: state.ControllerState) -> None:
    """Procees the state the controller to emulate keyboard presses."""
    for key in controller_state.get_down_keys():
        if key == "BTN_SOUTH":
            keyboard.press_and_release("windows+space")
        elif key == "BTN_WEST":
            keyboard.press_and_release("windows+1")
        elif key == "BTN_NORTH":
            keyboard.press_and_release("windows+2")
        elif key == "BTN_EAST":
            keyboard.press_and_release("windows+3")
        controller_state.keys[key] = 0

    for axis, value in controller_state.get_off_center_axes():
        if axis == "ABS_X":
            mouse.move(value * MOUSE_SPEED, 0, absolute=False, duration=0)
        if axis == "ABS_Y":
            mouse.move(0, value * MOUSE_SPEED, absolute=False, duration=0)
