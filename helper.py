#!/usr/bin/env python
import os
import constants

def get_csv_path():
    return os.path.dirname(os.path.realpath(__file__))+'/'+constants.CSV_FOLDER

# Retrieves csv
def get_csv_file(file):
    return get_csv_path()+file+'.csv';