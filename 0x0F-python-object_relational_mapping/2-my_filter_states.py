#!/usr/bin/python3
""" This is a python script that selects
stuff from a db with a filter
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           port=3306, db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute('SELECT * from states WHERE name LIKE  "{}";'.format(sys.argv[4]))
    res = cursor.fetchall()
    for state in res:
        print(state)
    cursor.close()
    conn.close()
