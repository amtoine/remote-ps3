from dataclasses import dataclass
from typing import Any, Dict

import evdev

AXIS_CENTER = 128
AXIS_OFF_CENTER_TOLERANCE = 50


def is_axis_off_center(value: int) -> bool:
    return abs(value - AXIS_CENTER) > AXIS_OFF_CENTER_TOLERANCE


def compute_normalized_axis_offset(value: int) -> float:
    return (value - AXIS_CENTER) / AXIS_CENTER


def remove_none_from_dict(dictionary: Dict[Any, Any]) -> Dict[Any, Any]:
    return {
        key: value for key, value in dictionary.items() if value is not None
    }


@dataclass
class ControllerState:
    """Class for keeping track of the state of a controller."""

    keys: Dict[int, int]
    axes: Dict[str, int]

    def update_keys(self, event: evdev.events.KeyEvent) -> None:
        """Update the keys of the controller based on an event."""
        keys = evdev.ecodes.keys[event.scancode]
        # get the appropriate key state
        if isinstance(keys, list):
            key_name = sorted(keys, key=lambda x: len(x))[1]
        else:
            key_name = keys
        # and set the internal controller key to the keystate
        self.keys[key_name] = event.keystate

    def update_axis(self, event: evdev.events.AbsEvent) -> None:
        """Update the axes of the controller based on an event."""
        axis = evdev.ecodes.ABS[event.event.code]
        self.axes[axis] = event.event.value

    def get_down_keys(self):
        """Get the list of all the keys currently held down."""
        return [key for key, pressed in self.keys.items() if pressed]

    def get_off_center_axes(self):
        """Get the list of off-centered axes, with the normalized offset."""
        return [
            (axis, compute_normalized_axis_offset(value))
            for axis, value in self.axes.items()
            if value is not None and is_axis_off_center()
        ]

    def __repr__(self, *, ommit_none: bool = False) -> str:
        if ommit_none:
            keys = remove_none_from_dict(self.keys)
            axes = remove_none_from_dict(self.axes)
        else:
            keys = self.keys
            axes = self.axes

        return f"KEYS: {keys}\nAXES: {axes}"
