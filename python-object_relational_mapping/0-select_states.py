#!/usr/bin/python3
"""Lists all states from the hbtn_0e_0_usa database, sorted by id."""
import sys
import MySQLdb


def list_states(username, password, database):
    """Connect to MySQL and print every row of the states table by id."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])