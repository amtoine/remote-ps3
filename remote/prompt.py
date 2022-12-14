from typing import List, Any

from rich import print

from rich.prompt import IntPrompt
from rich.prompt import Confirm


def rich_range_prompt(a: int, b: int) -> int:
    """Ask for an index in a range of numbers with rich."""
    while True:
        index = IntPrompt.ask(
            f":rocket: Enter a number between [b]{a}[/b] and [b]{b}[/b]"
        )
        if index >= a and index <= b:
            break
        print(f":pile_of_poo: [prompt.invalid]Number must be between {a} and {b}")

    return index


def rich_get_array_index_prompt(array: List[Any], *, binary_prompt: str) -> int:
    """Get an index in an array."""
    if len(array) == 0:
        index = -2
    elif len(array) == 1:
        if Confirm.ask(binary_prompt, default=True):
            index = 0
        else:
            index = -1
    else:
        index = rich_range_prompt(1, len(array)) - 1

    return index
