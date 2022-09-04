from dataclasses import dataclass
from typing import Dict

import evdev

from src import device


@dataclass
class ControllerState:
    """Class for keeping track of the state of a controller."""

    keys: Dict[int, int]
    axes: Dict[str, int]

    def update_keys(self, event: evdev.events.KeyEvent) -> None:
        self.keys[event.scancode] = event.keystate

    def update_axis(self, event: evdev.events.AbsEvent) -> None:
        for axis in device.AXES:
            if evdev.ecodes.bytype[event.event.type][event.event.code] == axis:
                self.axes[axis] = event.event.value
