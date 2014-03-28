import sys, os
import constants
import emailer
import gecko
import querier
import yaml_parser
import glob
import json

def process_json(json_result):
    inputs = json_result['input']

    print json_result

    if inputs['type'] == 'postgres':
        conn = inputs['connection_string']
        query = inputs['query']
        label = inputs['label']
        querier.run_psql_query(conn, query, label)

    outputs = json_result['output']

    if outputs['type'] == 'geckoboard':
        api_key = outputs['api_key']
        label = outputs['label']
        widget_key = outputs['widget_key']

        data = gecko.format_csv_data(label)
        gecko.push_to_geckoboard(api_key,widget_key,data)

# Clears all csv data before running new code
def clear_csvs():
    files = glob.glob(constants.get_csv_path()+'/*.csv')
    for f in files:
        os.remove(f)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "usage: __main__.py [yaml_file]"
        sys.exit(1)

    yaml_file = sys.argv[1]

    clear_csvs()
    results = yaml_parser.parse_yaml_file(yaml_file)
    process_json(results)