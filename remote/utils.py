from typing import Any, Dict

from plyer import notification
import json

PROFILES = ["qutebrowser", "mpv", "firefox"]

Config = Dict[str, Any]


def get_config_with_profile(profile: str, *, filename: str) -> Config:
    """Extract a profile from the global configuration."""
    with open(filename, "r") as remote_config_file:
        config = json.load(remote_config_file)

    common = config["common"]
    profile_config = config["profiles"][profile]
    profile_config.update(common)

    notification.notify(
        title="PS3 remote.py",
        message=f"Profile: {profile}",
        app_icon=None,
        timeout=3,
    )

    return profile_config
