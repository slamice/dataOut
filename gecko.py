#!/usr/bin/env python
import requests, json
import constants
import helper
import csv

def push_to_geckoboard(api_key, widget_key, data):
    ret = requests.post("https://push.geckoboard.com/v1/send/%s" % widget_key, json.dumps({'api_key' : api_key, 'data' : data}), verify=False)
    if not (ret.status_code == 200 and ret.json().get('success') == True):
        raise ValueError(ret.content)

# Formats csv data into gecko data {"item":[{"label":"EXAMPLE MESSAGE","value":1234}]}
def format_csv_data(csv_file):
    items = []
    with open(constants.get_csv_file(csv_file), 'rb') as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quotechar='\'', escapechar='\\')
        for i, row in enumerate(rows):
            items.append({'label':row[0],'value':row[1]})

    data = {'item':items}
    return data
