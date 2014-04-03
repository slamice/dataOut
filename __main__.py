import sys, os
import constants
import helper
import emailer, gecko, gdocs
import querier
import yaml_parser
import glob, json

def process_geckoboard_info(outputs):
    api_key = outputs['api_key']
    for w in outputs['widgets']:
        csv_file = helper.get_csv_file(w['label'])
        widget_key = w['widget_key']
        data = gecko.format_csv_data(csv_file)
        gecko.push_to_geckoboard(api_key,widget_key,data)

def process_google_spreadsheet_info(outputs):
    email = outputs['email']
    password = outputs['password']
    for s in outputs['sheets']:
        filepath = helper.get_csv_file(s['label'])
        wrksht_key = s['wrksht_key']
        sheet_num = s['sheet_num']
        gdocs.run(filepath, email, password, wrksht_key, sheet_num)

# TODO replace with better yaml parsing
def process_json(json_result):
    inputs = json_result['input']

    #TODO Replace with polymorphic design 
    if inputs['type'] == 'postgres':
        conn = inputs['connection_string']
        for q in inputs['queries']:
            query = q['query']
            label = q['label']
            querier.run_psql_query(conn, query, label)

    outputs = json_result['output']

    #TODO Replace with polymorphic design
    if outputs['type'] == 'geckoboard':
        # TODO validate geckoboard options
        process_geckoboard_info(outputs)
    elif outputs['type'] == 'google-spreadsheet':
        # TODO validate geckoboard options
        process_google_spreadsheet_info(outputs)


# Clears all csv data before running new code
def clear_csvs():
    files = glob.glob(helper.get_csv_path()+'/*.csv')
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