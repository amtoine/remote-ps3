from typing import Any, Dict, List, Union

from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key, KeyCode
from pynput.mouse import Button
from pynput.mouse import Controller as MouseController

mouse = MouseController()
keyboard = KeyboardController()


def convert_action_to_key(action: Union[str, int]):
    if isinstance(action, int):
        key = KeyCode(action)
    elif isinstance(action, str):
        key = Key.__dict__[action]
    return key


def send_keyboard_press(
    actions: List[Union[str, int]], *, kwargs: Dict[str, Any]
):
    keys = [convert_action_to_key(action) for action in actions]
    for key in keys:
        keyboard.press(key)

    for key in keys[::-1]:
        keyboard.release(key)


def send_mouse_click(action: str, *, kwargs: Dict[str, Any]):
    mouse.click(Button.__dict__[action])


def send_mouse_move(action: str, *, kwargs: Dict[str, Any]):
    px_speed = kwargs["value"] * kwargs["speed"]
    if action == "x":
        movement = (px_speed, 0)
    elif action == "y":
        movement = (0, px_speed)
    mouse.move(*movement)


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
