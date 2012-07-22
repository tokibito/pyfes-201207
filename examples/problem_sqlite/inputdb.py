# coding: utf-8
import os
import sys
import sqlite3


DATABASE_FILE = os.path.join(os.path.dirname(__file__), 'database.sqlite')

def main():
    if len(sys.argv) < 3:
        print "inputdb.py name cost"
        sys.exit()
    name = sys.argv[1].decode('utf-8')
    cost = int(sys.argv[2])
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO items (name, cost) values (?, ?);',
        [name, cost],
    )
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
