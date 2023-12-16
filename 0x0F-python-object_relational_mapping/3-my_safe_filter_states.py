#!/usr/bin/python3
""" takes in an argument and displays all values in the states
     table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys


if __name__ == "__main__":
    databas = MySQLdb.connect(host="localhost", user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = databas.cursor()
    mt = sys.argv[4]
    c.execute("SELECT * FROM states WHERE name LIKE %s", (mt, ))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    databas.close()
