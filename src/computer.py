from typing import Any, Dict

import keyboard
import mouse


def send_keyboard_press(action: str, *, kwargs: Dict[str, Any]):
    keyboard.press_and_release(action)


def send_mouse_click(action: str, *, kwargs: Dict[str, Any]):
    mouse.click(action)


def send_mouse_move(action: str, *, kwargs: Dict[str, Any]):
    px_speed = kwargs["value"] * kwargs["speed"]
    if action == "x":
        movement = (px_speed, 0)
    elif action == "y":
        movement = (0, px_speed)
    mouse.move(*movement, absolute=False, duration=0)


ACTIONS = {
    "press": send_keyboard_press,
    "click": send_mouse_click,
    "move": send_mouse_move,
}


def send(key: str, *, config: Dict[str, Any], kwargs: Dict[str, Any]):
    if key in config:
        action, arg = config[key]

        if action not in ACTIONS:
            print(f"Unknown action '{action}'...")
            exit(0)

        ACTIONS[action](arg, kwargs=kwargs)
