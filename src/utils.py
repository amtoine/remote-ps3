from typing import Any, Dict

import json


def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.

    val: float or int
    src: tuple
    dst: tuple

    example: print(scale(99, (0.0, 99.0), (-1.0, +1.0)))
    """
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[
        0
    ]


def scale_stick(value):
    return scale(value, (0, 255), (-100, 100))


def get_config_with_profile(profile: str, *, filename: str) -> Dict[str, Any]:
    """Extract a profile from the global configuration."""
    with open(filename, "r") as remote_config_file:
        config = json.load(remote_config_file)

    common = config["common"]
    profile_config = config["profiles"][profile]
    profile_config.update(common)

    return profile_config
