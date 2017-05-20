""" Main module """

import argparse
import logging
import os
from os.path import expanduser
import yaml
import argcomplete

CONFIG_PATH = expanduser('~/.sytssh.yaml')

def load_yaml(path):
    """Load a yaml as dict"""
    with open(path, 'r') as stream:
        return yaml.safe_load(stream)

def parse_args(doc):
    """ Setup the app arguments """
    parser = argparse.ArgumentParser(prog='sytssh')
    subparsers = parser.add_subparsers(help='Choose the project you want to connect', \
        dest='project')

    for project, attr in doc.items():
        parser_project = subparsers.add_parser(project)
        parser_project.add_argument('environment', choices=attr['host'].keys(), \
            help='Choose the environment')
        parser_project.add_argument('-n', help='Which instance of the host')

    argcomplete.autocomplete(parser)
    return parser.parse_args()

def connect(doc, args):
    """ Connect to the server via SSH """
    hostname = doc[args.project]["host"][args.environment]
    os.system('ssh root@{host} -p 32768'.format(host=hostname))

def main():
    try:
        doc = load_yaml(CONFIG_PATH)
        args = parse_args(doc)
        connect(doc, args)
    except FileNotFoundError:
        logging.error("You need to configure %s file", CONFIG_PATH)

if __name__ == '__main__':
    main()
