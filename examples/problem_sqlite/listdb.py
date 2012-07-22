# coding: utf-8
import os
import sys
import sqlite3


DATABASE_FILE = os.path.join(os.path.dirname(__file__), 'database.sqlite')

def main():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT name, cost FROM items;")
    for rows in cursor:
        print u"%s %s円" % rows
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
