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
        keys = evdev.ecodes.keys[event.scancode]
        key_name = (
            sorted(keys, key=lambda x: len(x))[1]
            if isinstance(keys, list)
            else keys
        )
        self.keys[key_name] = event.keystate

    def update_axis(self, event: evdev.events.AbsEvent) -> None:
        self.axes[evdev.ecodes.ABS[event.event.code]] = event.event.value

    def __repr__(self, *, ommit_none: bool = False) -> str:
        if ommit_none:
            keys = {
                key: value
                for key, value in self.keys.items()
                if value is not None
            }
            axes = {
                key: value
                for key, value in self.axes.items()
                if value is not None
            }
        else:
            keys = self.keys
            axes = self.axes

        return f"KEYS: {keys}\nAXES: {axes}"
