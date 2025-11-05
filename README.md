# autoscripter

A basic shell script writer for python and bash.

Currently supports common linux shell commands (mkdir, touch, ls, cd, rm, mv).

## Install

Clone the repo and set up dependencies:
```bash
git clone https://github.com/RynSingleton/autoscripter.git
cd autoscripter
make install
```

## Usage

Run the program with:
```bash
make run
```

The program will prompt you through creating your scripts. Generated scripts end up in the `output/` directory.

Example session:
```
Script type [python/bash]: python
Output filename: my_script.py

Operations include:
  1. mkdir
  2. touch
  3. ls
  4. cd
  5. rm
  6. mv

Operations to include: 1 2

--- Config for 'mkdir' ---
  Directory path to create: /tmp/test
  Create parent directories? [Y/n]: y

--- Config for 'touch' ---  
  File path to create: /tmp/test/file.txt

Add error handling? [Y/n]: y

Script generated: output/my_script.py
```

## Project structure
```
src/autoscripter.py    - main entry point
src/prompts.py         - handles user input
src/generator.py       - generates scripts from templates
src/templates/         - jinja2 templates for python/bash
```

## Requirements

Python 3.8+, tested on WSL/Linux.

Uses click for CLI and jinja2 for templating.

## Development
```bash
make clean    # clean cache and output
make help     # show all commands
```

---
### Next Steps

Adding network commands (ssh, curl) soon!

## License

MIT