# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import json
import os
import re
from itertools import imap
from subprocess import check_output
import shutil
from distutils import dir_util

import click
import whaaaaat
from whaaaaat import print_json, prompt

licenses = check_output(['licen', '-l'])
licenses = re.sub(r'\s', '', licenses).split(',')
licenseChoices = map(lambda x: {'name': x, 'value': x}, licenses)
click.disable_unicode_literals_warning = True
questions = [
    {
        'type': 'input',
        'name': 'name',
        'message': 'package name: ',
        'default':  os.path.basename(os.getcwd()).decode('utf-8')
    },
    {
        'type': 'confirm',
        'name': 'isMerge',
        'message': 'the folder is exists,Continue:',
        'when': lambda ans: os.path.exists(os.path.join(os.getcwd(), ans['name'])),
        'default': False
    },
    {
        'type': 'input',
        'name': 'version',
        'message': 'version ',
        'default': '1.0.0',
        'when': lambda ans: ans.get('isMerge', True),
    },
    {
        'type': 'input',
        'name': 'description',
        'message': 'description ',
        'when': lambda ans: ans.get('isMerge', True),
    },
    {
        'type': 'input',
        'name': 'repro',
        'message': 'git repository',
        'when': lambda ans: ans.get('isMerge', True),
    },
    {
        'type': 'input',
        'name': 'author',
        'message': 'author',
        'default': os.getlogin().decode('utf-8'),
        'when': lambda ans: ans.get('isMerge', True),
    },
    {
        'type': 'list',
        'name': 'license',
        'message': 'license',
        'choices': licenseChoices,
        'when': lambda ans: ans.get('isMerge', True)
    }
]


@click.command()
@click.option('--template', default='default', help='''
    which package template should use.
    For current, it does not implement and will be ignore.
''')
@click.pass_context
def create(ctx, template):
    '''
        create package folder with config you special
    '''
    config = prompt(questions)
    if len(config) == 0:
        ctx.abort()

    isMerge = config.pop('isMerge', True)

    if isMerge is True:
        configJson = json.dumps(config, sort_keys=False,
                                indent=4, separators=(',', ':'))
        click.echo(configJson)

        isOk = click.confirm('Is this OK? ', default=True)
        if isOk is True:
            name = config.get('name')

            if not os.path.exists('%s' % (name)):
                os.mkdir(name)

            with open('%s/.gitkeep' % name, 'w'):
                pass

            # copy template to cwd
            try:
                cwd = os.path.dirname(__file__)
                src = os.path.join(cwd, '../templates/%s/' % template)
                dir_util.copy_tree(src, './', False)
            except:
                pass
            finally:
                pass
                # @todo  manully copy template

            # generate LICENSE file
            with open('./LICENSE', 'w') as f:
                args = ['licen', '-f', config.get('author'), config['license']]
                licenseContent = check_output(args)
                f.write(licenseContent)

            with open('./README.md', 'r') as f:
                content = f.read()
                reg = r'\{\{(.*?)\}\}'
                content = re.sub(reg, lambda m: config.get(
                    m.groups()[0], ''), content, flags=re.IGNORECASE)

            with open('./README.md', 'w') as f:
                f.write(content)

            with open('./setup.py', 'r') as f:
                content = f.read()
                reg = r'\{\{(.*?)\}\}'
                content = re.sub(reg, lambda m: config.get(
                    m.groups()[0], ''), content, flags=re.IGNORECASE)

            with open('./setup.py', 'w') as f:
                f.write(content)
