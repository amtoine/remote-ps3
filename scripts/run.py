#!/usr/bin/env python

import argparse

from remote import device, hooks, utils


def main(*, profile: str, config: str):
    connected_device = device.get_device()
    profile_config = utils.get_config_with_profile(profile, filename=config)

    device.listen_to(
        connected_device,
        hook=hooks.remote_hook,
        config=profile_config,
        profile=profile,
        filename=config,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--profile",
        "-p",
        choices=utils.PROFILES,
        default=utils.PROFILES[0],
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
    default = "config/remote.json"
    parser.add_argument(
        "--config",
        "-c",
        type=str,
        default=default,
        help=f"the path to the JSON config file (defaults to '{default}')."
    )

    args = parser.parse_args()
    main(profile=args.profile, config=args.config)
