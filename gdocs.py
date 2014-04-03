import time, csv, re, time, sys
from pprint import pprint
import gdata.spreadsheet.service

#### Examples from http://pseudoscripter.wordpress.com/2011/05/09/automatically-update-spreadsheets-and-graphs/ ####
def _CellsUpdateAction(spr_client, row,col,inputValue,key,wksht_id):
    try:
        entry = spr_client.UpdateCell(row=row, col=col, inputValue=inputValue,key=key, wksht_id=wksht_id)
        if isinstance(entry, gdata.spreadsheet.SpreadsheetsCell):
            print row,",", col, 'updated:', inputValue
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

    
def get_data_from_file(filepath):
    #'This should work, not tested it.'
    f = open(filepath)
    data = f.read()
    f.close()
    data = data.decode("utf-8")
    return data
    
def write_data( dict ):
    entry = spr_client.InsertRow(dict, spreadsheet_key, worksheet_id)
    if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
      print "Insert row succeeded."
    else:
      print "Insert row failed."

def run(filepath, email, password,wrksheet_key, sheet_id):

    # TODO Replace with OAuth 2.0
    spr_client = gdata.spreadsheet.service.SpreadsheetsService()
    spr_client.email = email
    spr_client.password = password
    spr_client.source = 'Example CSV To Spreadsheet Writing Application'
    spr_client.ProgrammaticLogin( )
    worksheet_key = wrksheet_key

    data = get_data_from_file(filepath)

    ## Now write the data, cell by cell
    data = data.split("\n")
    for l, line in enumerate(data):
        if l == 0:
            pass
        else:
            items = line.split(",")

            for i, item in enumerate(items):
                try:
                    the_value = item.replace('"', '') #Strip quotes off the beginning/end  
                    print the_value                  
                    _CellsUpdateAction(spr_client,l,i+1,the_value,worksheet_key,sheet_id)
                except Exception, err:
                        print "\t Line", l, "only has", len(item), "items", items
                        print err
                        pass
        
    
if __name__ == '__main__':
    
    if len(sys.argv) <= 1:
        print "usage: gdocs.py [file_path] [email] [password] [worksheet_key] [sheet_id]"
        sys.exit(1)

    filepath = sys.argv[1]
    email = sys.argv[2]
    password = sys.argv[3]
    worksheet_key = sys.argv[4]
    sheet_id = sys.argv[5]

    run(filepath, email, password, worksheet_key, sheet_id)