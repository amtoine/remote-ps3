#!/usr/bin/env python

import json
import argparse
from typing import Dict

import evdev
from rich import print

from src import device, hooks, utils


def main(*, profile: str):
    profile_config = utils.get_config_with_profile(
        profile, filename="remote.json"
    )

    configured_remote_hook = lambda s: hooks.remote_hook(
        s, config=profile_config
    )
    device.listen_to(device.get_device(), hook=configured_remote_hook)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    profiles = ["qutebrowser", "mpv", "firefox"]
    parser.add_argument(
        "--profile",
        "-p",
        choices=profiles,
        required=True,
        help=(
            "A different profile will send different keys to "
            "the host machine, e.g. `qutebrowser` requires to "
            "enter insert mode with 'i' and exit it afterwards "
            "with <esc>, 'firefox' and 'mpv' do not."
            "`mpv` was designed to watch local videos. "
            "`qutebrowser` for youtube in mind only. "
            "and `firefox` for all the rest (netflix, primevideos, ...)"
        ),
    )

    args = parser.parse_args()
    main(profile=args.profile)
