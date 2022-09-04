from typing import Dict

import keyboard
import mouse


def send_to_keyboard(key: str, *, config: Dict[str, str]):
    for controller_key, computer_key in config.items():
        if key == controller_key:
            keyboard.press_and_release(computer_key)


def send_to_mouse(
    axis: str, value: int, *, config: Dict[str, str], mouse_speed: int
):
    for controller_axis, computer_mouse in config.items():
        if axis == controller_axis:
            if computer_mouse == "x":
                movement = (value * mouse_speed, 0)
            elif computer_mouse == "y":
                movement = (0, value * mouse_speed)
            mouse.move(*movement, absolute=False, duration=0)
