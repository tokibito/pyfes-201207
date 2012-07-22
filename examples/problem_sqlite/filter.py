# coding: utf-8
import os
import sys
import sqlite3


DATABASE_FILE = os.path.join(os.path.dirname(__file__), 'database.sqlite')

def main():
    if len(sys.argv) < 2:
        print "filter.py cost"
        sys.exit()
    cost = int(sys.argv[1])
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT name, cost FROM items WHERE cost >= ?;", [cost])
    print "%d円以上の品物は、" % cost
    for rows in cursor:
        print u"%s %s円" % rows
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
