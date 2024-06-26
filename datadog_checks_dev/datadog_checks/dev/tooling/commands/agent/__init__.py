# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import click

from ..console import CONTEXT_SETTINGS
from .requirements import requirements

ALL_COMMANDS = (requirements,)


@click.group(context_settings=CONTEXT_SETTINGS, short_help='A collection of tasks related to the Datadog Agent')
def agent():
    pass


for command in ALL_COMMANDS:
    agent.add_command(command)
