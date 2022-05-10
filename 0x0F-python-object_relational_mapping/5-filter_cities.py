#!/usr/bin/python3
"""Write a script that
lists all states from the
database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM \
                 cities LEFT JOIN states ON cities.state_id=states.id \
                 WHERE states.name = %s ORDER BY \
                 cities.id ASC", (argv[4],))
    query_rows = cur.fetchall()
    SEP = ""
    for row in query_rows:
        print("{}{}".format(SEP, row[0]), end="")
        SEP = ", "
    print()
    cur.close()
    conn.close()
