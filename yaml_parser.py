#!/usr/bin/env python

import yaml #pyyaml

def parse_yaml_file(file):
    stream = open(file, 'r')
    return yaml.load(stream)

# Validates that every input has a proper output in the yml file
def validate_yaml_file():
    return 0