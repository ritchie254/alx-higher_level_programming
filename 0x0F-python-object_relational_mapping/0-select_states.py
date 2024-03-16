#!/usr/bin/python3
"""
	the mysqld
"""

import MySQLdb
import sys

if __name__ == "__main__":
	mysql_us = sys.argv[1]
	pass_w = sys.argv[2]
	d_b = sys.argv[3]

	connection = MySQLdb.connect(user=mysql_us, passwd=pass_w, db=d_b)
	cur = connection.cursor()
	cur.execute("SELECT states FROM hbtn_0e_0_usa ORDER BY id")
	q_row = cur.fetchall()

	for state in q_row:
		print(state)

	cur.close()
	connection.close()
