from rich import print

from src import state

OMMIT_NONE = True


def DEFAULT_CONTROLLER_HOOK(controller_state: state.ControllerState) -> None:
    """Print the state of the controller."""
    print(controller_state.__repr__(ommit_none=OMMIT_NONE))


def remote_hook(controller_state: state.ControllerState) -> None:
    """Procees the state the controller to emulate keyboard presses."""
    for key in controller_state.get_down_keys():
        print(f"{key} is pressed")
        controller_state.keys[key] = 0
    for axis, value in controller_state.get_off_center_axes():
        print(f"{axis} is at {value}")
