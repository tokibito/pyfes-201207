# coding: utf-8
import os
import sqlite3


DATABASE_FILE = os.path.join(os.path.dirname(__file__), 'database.sqlite')

def main():
    connection = sqlite3.connect(DATABASE_FILE)
    connection.execute("CREATE TABLE items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, cost INTEGER);")
    connection.close()

if __name__ == '__main__':
    main()
