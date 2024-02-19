#!/usr/bin/python3
""" This is a python script that selects
stuff from a db
"""
import MySQLdb
import sys

conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                       port=3306, db=sys.argv[3])
cursor = conn.cursor()
cursor.execute('SELECT id, name FROM states ORDER BY states.id ASC')
res = cursor.fetchall()
for state in res:
    print(state)
