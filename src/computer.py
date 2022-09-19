from typing import Any, Dict, List, Union

from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key, KeyCode
from pynput.mouse import Button
from pynput.mouse import Controller as MouseController

from src import utils

mouse = MouseController()
keyboard = KeyboardController()


def convert_action_to_key(action: Union[str, int]):
    if isinstance(action, int):
        key = KeyCode(action)
    elif isinstance(action, str):
        if action in Key.__dict__:
            key = Key.__dict__[action]
        else:
            key = action
    return key


def cycle_through_profiles(arg: str, kwargs: Dict[str, Any]) -> str:
    profile = kwargs["profile"]
    idx = utils.PROFILES.index(profile)
    new_idx = (idx + 1) % len(utils.PROFILES)
    new_profile = utils.PROFILES[new_idx]

    return new_profile


def send_keyboard_press(
    actions: List[Union[str, int]], *, kwargs: Dict[str, Any]
) -> None:
    keys = [convert_action_to_key(action) for action in actions]
    for key in keys:
        keyboard.press(key)

    for key in keys[::-1]:
        keyboard.release(key)


def send_mouse_click(action: str, *, kwargs: Dict[str, Any]) -> None:
    mouse.click(Button.__dict__[action])


def send_mouse_move(action: str, *, kwargs: Dict[str, Any]) -> None:
    px_speed = kwargs["value"] * kwargs["speed"]
    if action == "x":
        movement = (px_speed, 0)
    elif action == "y":
        movement = (0, px_speed)
    mouse.move(*movement)


ACTIONS = {
    "profile": cycle_through_profiles,
    "press": send_keyboard_press,
    "click": send_mouse_click,
    "move": send_mouse_move,
}


def send(key: str, *, config: Dict[str, Any], kwargs: Dict[str, Any]) -> Union[None, str]:
    if key in config:
        action, arg = config[key]

        if action not in ACTIONS:
            print(f"Unknown action '{action}'...")
            exit(0)

        return ACTIONS[action](arg, kwargs=kwargs)
