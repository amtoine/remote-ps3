# remote-ps3
A remote emulator for a linux-ps3 system.

## Usage
- edit the `config.sh` file to change the name of the command and the paths
- run `./install.sh` to
  - install a `python` virtual environment with `virtualenv`
  - install the dependencies from `requirements.txt` inside it
  - build an executable script which runs the source
  - move this script to some location in the `$PATH`
- run `./clean.sh` to
  - remove the virtual environment
  - remove the executable from the `$PATH`
  - remove the executable from the source
