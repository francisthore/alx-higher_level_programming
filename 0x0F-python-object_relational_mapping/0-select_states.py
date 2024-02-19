#!/usr/bin/python3
""" This is a python script that selects
stuff from a db
"""
import MySQLdb
import sys

conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                       port=3306, db=sys.argv[3])
cursor = conn.cursor()
res = cursor.execute('SELECT id, name FROM {}.states'.format(sys.argv[3]))
