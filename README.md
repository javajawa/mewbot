<!--
SPDX-FileCopyrightText: 2021 Benedict Harcourt <ben.harcourt@harcourtprogramming.co.uk>

SPDX-License-Identifier: BSD-2-Clause
-->

# MewBot

MewBot is an automation framework intended to simplify building cross-platform
text/chat-bots.
The design is intended to be modular with configuration separated from code,
allowing users and developers to build out custom logic and behaviours with
minimal coding experience.

### Status

> :warning: This project is still in the very early stages. Some basic bots can be built
> and run, but we currently consider all parts of the framework to be unstable.

### Packages and Modules

| Package                   | Modules                             | Description                                                                                                                                |
|---------------------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `mewbot-core`             | `mewbot.core`                       | Base interfaces for all modules                                                                                                            |
| `mewbot-dev`              | `mewbot.component`, `mewbot.api.v1` | Development libraries + component registry system. This is the package that all 3rd party libraries should depend on for their interfaces. |
| `mewbot-runner`           | `mewbot.loader`, `mewbot.bot`       | Tools to load a bot, and run that bot.                                                                                                     |
| `mewbot-[discord/twitch]` | `mewbot.io.[discord/twitch]`        | The bindings to connect MewBot to a given service.                                                                                         |

![module dependency graph](./mewbot.svg)

### Development

Contributions to the project are made via GitHub pull requests, which will
enforce the code style and linting requirements of this project.

#### Setting up project for local development

The recommended way to set this project up is using python 3.9 (or higher) with
a venv setup.
The setup is mostly standard, but we do have to add `./src` to the `PYTHONPATH`
so that python correctly detects all the source files.
The following example will get you started in bash-like shells.

```shell
# Get the source code
git clone git@github.com:mewler/mewbot
cd mewbot

# Set up the virtual environment
python3 -m venv venv
printf 'PYTHON_PATH=./src:$PYTHON_PATH\n' >>venv/bin/activate

# Activate the virtual environment
source venv/bin/activate

# Install all dependencies (including development dependencies)
pip install requirements-dev.txt

# Run a demo!
python3 -m examples examples/trivial_socket.yaml
```

#### Running the tests and linters

> :warning: We currently have no test framework (see #11)

You can run the linters via the convenience script `tools/lint.sh`.
