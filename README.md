# Projsort

_stupid simple utility for sorting project files_

Made this for a friend to automate a rediculously tedious task he was working on

## Installation

Clone the repo into the `.local/bin/` directory
```bash
git clone https://github.com/DavidHoenisch/projsort.git ~/.local/bin/projsort
```

Create a virtualenv for the utility
```bash
virtualenv ~/.local/bin/projsort/env
```

Add an alias for the script
```bash
echo "alias projsort='~/.local/bin/projsort/env/bin/python3 ~/.local/bin/projsort/projsort.py" >> ~/.bashrc && source ~/.bashrc
```

Configured this way, you can run `projsort` from anywhere in a file system on you local machine.

## Usage

From anywhere in a file tree, run the projsort command.  Projsort takes one
command line argument and that is the parent folder where you want the files to
be sorted into.

## Updates

from time to time, this utility may receive updates. To update the utility, 
cd into `~/.local/bin/projsort/` and run:

```bash
git pull
```
