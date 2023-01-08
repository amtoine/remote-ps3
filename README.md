# remote-ps3
A remote emulator for a linux-ps3 system.

## installation
### using `PKGBUILD`s
> see the [goatfiles `PKGBUILD`s](https://github.com/goatfiles/pkgbuilds)

### from source
change to your liking
- the installation configuration in [`config/install.sh`]
- the keybindings in [`config/remote.json`]

then run the following
```bash
./scripts/install.sh
```

## usage
```bash
remote-PS3
```
or more generally the `exe` field defined in [`config/remote.json`]

[`config/install.sh`]: config/install.sh
[`config/remote.json`]: config/remote.json
