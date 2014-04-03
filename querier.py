#!/usr/bin/env python
import csv
import constants
import helper
from datetime import datetime
import psycopg2
import sys

# Returns an open psql connection
def run_psql_query(conn_string, query, title):
    db = psycopg2.connect(conn_string)
    try:
        cur = db.cursor()
        cur.execute(query)
        records = cur.fetchall()
        write_csv_results(records, title)

    except Exception,e:
        print str(e)

    db.close()

# Writes results for records
def write_csv_results(records, title):
    csv_title = "%s%s.csv" % (constants.get_csv_path(),title)

    with open(csv_title, 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for record in records:
            csvwriter.writerow(record)