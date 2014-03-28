#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

CSV_FOLDER = 'csvs/'

def get_csv_path():
    return os.path.dirname(os.path.realpath(__file__))+'/'+CSV_FOLDER

# Retrieves csv
def get_csv_file(file):
    return get_csv_path()+file+'.csv';