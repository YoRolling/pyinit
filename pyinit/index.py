# -*- coding: utf-8 -*-
import click
import os
from commands import create


@click.group()
@click.pass_context

def cli(ctx):
    '''
    a command line tool helps u to init module with boilerplate
    '''

cli.add_command(create, 'create')

if __name__ == '__main__':
	# pylint: disable=E1123,E1120
    cli(obj={})
